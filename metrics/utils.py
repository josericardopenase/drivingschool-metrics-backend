import requests
import io
import zipfile
import os
import csv
import tempfile
import pandas as pd

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

def parser_dgt_data(ruta_csv):
    # Leer el archivo CSV
    df = pd.read_csv(ruta_csv, encoding='latin-1', delimiter=';')
    
    # Filtrar por DESC_PROVINCIA 'Palmas (Las)'
    df = df[df['DESC_PROVINCIA'] == 'Palmas (Las)']

    # Eliminar los centros de examen 'Arrecife' y 'Puerto del Rosario'
    df = df[~df['CENTRO_EXAMEN'].isin(['Arrecife', 'Puerto del Rosario'])]

    # Calcular la columna 'NUM_APTOS_3_o_mas_conv' y 'NUM_PRESENTADOS'
    df['NUM_APTOS_3_o_mas_conv'] = df['NUM_APTOS_3o4conv'] + df['NUM_APTOS_5_o_mas_conv']
    df['NUM_PRESENTADOS'] = df['NUM_APTOS'] + df['NUM_NO_APTOS']

    # Eliminar columnas innecesarias
    df.drop(columns=['CENTRO_EXAMEN', 'DESC_PROVINCIA', 'CODIGO_AUTOESCUELA', 'CODIGO_SECCION', 
                     'NUM_APTOS_3o4conv', 'NUM_APTOS_5_o_mas_conv', 'NUM_NO_APTOS'], inplace=True)

    # Reorganizar el DataFrame con el orden deseado de columnas
    df = df[['NOMBRE_AUTOESCUELA', 'NOMBRE_PERMISO', 'TIPO_EXAMEN', 'NUM_PRESENTADOS', 'NUM_APTOS',
             'NUM_APTOS_1conv', 'NUM_APTOS_2conv', 'NUM_APTOS_3_o_mas_conv', 'MES', 'ANYO']]
    
    return df