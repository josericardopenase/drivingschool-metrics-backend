import requests
import io
import zipfile
import os
import csv
import tempfile

def get_key_file_path():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    key_file_path = os.path.join(script_directory, 'dgtkey.txt')
    return key_file_path

def read_key_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def download_zipfile(year, month):
    url = 'https://sedeapl.dgt.gob.es/WEB_IEST_CONSULTA/microdatos.faces'
    payload = {
        'configuracionInfPersonalizado': 'configuracionInfPersonalizado',
        'configuracionInfPersonalizado:filtroMesAnyo': str(year),
        'configuracionInfPersonalizado:filtroMesMes': str(month),
        'configuracionInfPersonalizado:j_id131': 'Descargar',
        'javax.faces.ViewState': read_key_from_file(get_key_file_path())
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        # Check if the response is a ZIP file
        # Extract the filename from the response headers
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            filename = content_disposition.split('filename=')[1].strip('\"')
        else:
            filename = f'export_auto_{year}{month:02d}_data.zip'  # Generate a default filename

        # Save the file
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    else:
        print(f'Error: POST request failed with status code {response.status_code}.')

    return None

def extract_csv_from_zip(zipfile_path, csv_filename, output_dir):
    with zipfile.ZipFile(zipfile_path, 'r') as zip_file:
        if csv_filename in zip_file.namelist():
            zip_file.extract(csv_filename, output_dir)
            csv_path = os.path.join(output_dir, csv_filename)
            return csv_path
        else:
            print(f'Error: CSV file "{csv_filename}" not found in the ZIP file.')

    return None
