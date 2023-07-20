from django.core.management.base import BaseCommand, CommandError
import requests
from metrics.utils import download_zipfile, extract_csv_from_zip
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
                # Open and process the CSV file as needed
                with open(csv_path, 'r', encoding='latin-1') as csv_file:
                    csv_data = csv.reader(csv_file)
                    for row in csv_data:
                        print(row)
            else:
                print('Error: Failed to extract the CSV file.')

        self.stdout.write(
            self.style.SUCCESS('Successfully pulled all data from dgt')
        )