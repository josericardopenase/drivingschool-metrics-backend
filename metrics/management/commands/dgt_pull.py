from yaspin import yaspin
from django.core.management.base import BaseCommand, CommandError
import requests
from metrics.utils import download_zipfile, extract_csv_from_zip, parser_dgt_data
import csv
import os
from locations.models import Province
from drivingschools.models import DrivingSchoolSection, DrivingSchool, DrivingPermission
from tests.models import Test, TestCenter, TestType
from tqdm import tqdm

class Command(BaseCommand):
    help = "Pull all metrics data from dgt server"

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, help='The year for which to pull the data')
        parser.add_argument('month', type=int, help='The month for which to pull the data')
    
    def handle(self, *args, **options):
        year = options['year']
        month = options['month']

        # Example usage: Download ZIP file for January 2023 and open the CSV inside

        self.stdout.write(
            self.style.SUCCESS('\nStarted import of DGT DATA year={}, month={}\n'.format(year, month))
        )
        

        with yaspin(text="Downloading data CSV from dgt") as spinner:
            try:
                zipfile_path = download_zipfile(year=year, month=month)
            except:
                spinner.fail("❌")
                return;
            spinner.ok("✅")

        if zipfile_path:
            csv_filename = f'{os.path.splitext(zipfile_path)[0]}.txt'
            output_dir = os.getcwd()  # Set the output directory to the current working directory
            csv_path = extract_csv_from_zip(zipfile_path, csv_filename, output_dir)
            if csv_path:

                print("")
                with yaspin(text="Parsing DGT data") as spinner:
                    try:
                        df = parser_dgt_data(csv_path)
                    except:
                        spinner.fail("❌")
                        return;
                    spinner.ok("✅")

                self.stdout.write(
                    self.style.SUCCESS('\nImporting row by row to the database models: \n'.format(year, month))
                )
                for index, row in tqdm(df.iterrows(), total=df.shape[0]):
                    try:
                        province = Province.objects.get_or_create(name=row['DESC_PROVINCIA'])[0]
                        permission = DrivingPermission.objects.get_or_create(name=row['NOMBRE_PERMISO'])[0]
                        driving_school = DrivingSchool.objects.get_or_create(code=row['CODIGO_AUTOESCUELA'], name=row['NOMBRE_AUTOESCUELA'])[0]
                        driving_school_section = DrivingSchoolSection.objects.get_or_create(driving_school=driving_school, code=row['CODIGO_SECCION'])[0]
                        test_center = TestCenter.objects.get_or_create(name=row['CENTRO_EXAMEN'], province=province)[0]
                        test_type = TestType.objects.get_or_create(name=row['TIPO_EXAMEN'])[0]
                        test = Test.objects.get_or_create(test_center=test_center, test_type=test_type, school_section=driving_school_section, permission_type=permission, 
                                    num_aptos=row['NUM_APTOS'],
                                    num_presentados=row['NUM_PRESENTADOS'],
                                    num_aptos_1_conv=row['NUM_APTOS_1conv'],
                                    month=row['MES'],
                                    year=row['ANYO'])
                    except:
                        pass
        else:
            self.stdout.write(
                self.style.ERROR('\nError extracting CSV: \n'.format(year, month))
            )

            return;

        self.stdout.write(
            self.style.SUCCESS('Cambios: successfully pulled all data from dgt')
        )