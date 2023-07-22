from django.core.management.base import BaseCommand, CommandError
import requests
from metrics.utils import download_zipfile, extract_csv_from_zip, parser_dgt_data
import csv
import os

class Command(BaseCommand):
    help = "Pull all metrics data from dgt server"


    
    def handle(self, *args, **options):
        # Example usage: Download ZIP file for January 2023 and open the CSV inside
        zipfile_path = download_zipfile(year=2023, month=1)
        if zipfile_path:
            csv_filename = f'{os.path.splitext(zipfile_path)[0]}.txt'
            output_dir = os.getcwd()  # Set the output directory to the current working directory
            csv_path = extract_csv_from_zip(zipfile_path, csv_filename, output_dir)
            if csv_path:
                print(f'Success: CSV file "{csv_filename}" extracted to "{csv_path}".')
                df = parser_dgt_data(csv_path)
                print(df)
            else:
                print('Error: Failed to extract the CSV file.')


        self.stdout.write(
            self.style.SUCCESS('Cambios: successfully pulled all data from dgt')
        )