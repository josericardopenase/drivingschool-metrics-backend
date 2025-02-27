import requests
from bs4 import BeautifulSoup



class DGTGradeChecker(GradeCheckerInterface):
    def __init__(self):
        self.url = "https://sedeclave.dgt.gob.es/WEB_NOTP_CONSULTA/consultaNota.faces"
        self.session = requests.Session()

    def _get_view_state(self) -> str:
        response = self.session.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('input', {'name': 'javax.faces.ViewState'})['value']

    def _submit_form(self, payload: dict) -> BeautifulSoup:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.session.post(self.url, data=payload, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")

    def fetch_grade(self, DNI: str, fechaExamen: str, clasePermiso: str, nacimiento: str) -> dict:
        view_state = self._get_view_state()
        payload = {
            "formularioBusquedaNotas": "formularioBusquedaNotas",
            "formularioBusquedaNotas:nifnie": DNI,
            "formularioBusquedaNotas:fechaExamen": fechaExamen,
            "formularioBusquedaNotas:clasepermiso": clasePermiso,
            "formularioBusquedaNotas:fechaNacimiento": nacimiento,
            "formularioBusquedaNotas:honeypot": "",
            "formularioBusquedaNotas:j_id51": "Buscar",
            "javax.faces.ViewState": view_state,
        }
        soup = self._submit_form(payload)
        try:
            calificacion = soup.find(id="formularioResultadoNotas:j_id38:0:j_id70").text.strip()
            errores = soup.find(id="formularioResultadoNotas:j_id38:0:j_id78").text.strip()
            return {"calificacion": calificacion, "errores": errores}
        except AttributeError:
            raise ValueError("Unable to fetch grade details. Please check the input data or the page structure.")