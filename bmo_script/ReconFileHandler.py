__author__ = 'agupt15'

import os
import shutil
import datetime
import fnmatch

SYSTEMS = ['Rates', 'FX', 'Equities', 'Commodities']
QUALIFIERS = ['SOURCE', 'DESTINATION']


class FileHandler:
    def __init__(self):
        self.config = {}
        for system in SYSTEMS:
            self.config[system] = []

    def read_config(self):
        print('------Reading Config')
        with open('recon-files.config') as config_file:
            for line in config_file:
                # Ignore comments and Blanks
                if line.startswith('#') or line.strip() is '':
                    continue
                line = line.strip()
                name, value = line.split('=')
                system, qualifier = name.split('_')
                self.config[system].append((value, system, qualifier))


    def process(self):
        self.read_config()
        for system in self.config:
            print("{} has values {}".format(system, self.config[system]))

        for system in SYSTEMS:
            properties = self.config[system]
            if properties == [] or properties is None:
                print("{} properties doesn't exists. Skipping".format(system))
                continue
            print("Working for {}".format(system))
            source_folders = []
            destination_folder = None
            dtcc_folder = None
            ok_filename = None
            for file_folder, system, qualifier in properties:
                if qualifier.startswith('SOURCE') is True:
                    source_folders.append(file_folder)
                elif qualifier.startswith('DESTINATION') is True:
                    destination_folder = file_folder
                elif qualifier.startswith('DTCC') is True:
                    dtcc_folder = file_folder
                elif qualifier.startswith('OKFILE') is True:
                    ok_filename = file_folder
                else:
                    raise Exception('Unknown Property Qualifier {}'.format(qualifier))
            print("Source Folders {} --> Destination [{}]".format(source_folders, destination_folder))

            # transfer the XML files from source to destination
            for source in source_folders:
                for source_file in os.listdir(source):
                    if not source_file.endswith('.xml'):
                        continue
                    source_file = os.path.join(source, source_file)
                    shutil.move(source_file, destination_folder)
                    print("{} moved to {}".format(source_file, destination_folder))

            # create OK file in dtcc folder
            for file in os.listdir(dtcc_folder):
                if ok_filename is None:
                    ok_filename = file + ".OK"
                abs_file = os.path.join(dtcc_folder, ok_filename)
                with open(abs_file, 'w') as f:
                    f.write('')


# # Utility methods


def pad_zero(x):
    if x is None:
        return ''
    elif x < 10:
        return '0' + str(x)
    return x


DELIMITER = '||'


class AssetClassFileHandler:
    def __init__(self, date=None):
        if date is None or date.strip() == '':
            today = datetime.date.today()
            date = '{0}{1}{2}'.format(today.year, pad_zero(today.month), pad_zero(today.day))
        self.process_date = date
        print('Working for date: {0}'.format(self.process_date))
        self.config = ConfigFile()

    def process(self, asset_class):
        asset_class = asset_class.strip()
        print("Processing Asset Class [{1}] for date: {0}".format(self.process_date, asset_class))
        asset_class_working = 'Rates'
        sources = self.config.get_properties_by_qualifier(asset_class_working, 'SOURCE')
        destination, ok_file = self.config.get_properties_by_qualifier(asset_class_working, 'DESTINATION')[0][1].split(
            DELIMITER)
        print('Asset Class [{1}] has destination {0}. OK File: {2}'.format(destination, asset_class, ok_file))
        for source, value in sources:
            print('Processing source {0}'.format(source))
            value = value + DELIMITER + "False"
            src_path, src_pattern, dest_pattern, status = value.split('||')
            src_pattern = src_pattern.replace('YYYYMMDD', self.process_date)
            for file in os.listdir(src_path):
                if fnmatch.fnmatch(file, src_pattern):
                    print('MATCH found for File: {0} Pattern {1}'.format(file, src_pattern))

                    break


class ConfigFile:
    def __init__(self, file_name='recon-files.config'):
        self.config = {system: [] for system in SYSTEMS}
        print('------Reading Config')

        with open(file_name) as config_file:
            for line in config_file:
                # Ignore comments and Blanks
                if line.startswith('#') or line.strip() is '':
                    continue
                name, property_val = line.strip().split('=')
                system, qualifier = name.split('_')
                self.config[system].append((qualifier, property_val))
            self.check_validity()
            print('------Config loaded and validated')

    def check_validity(self):
        for asset_class in self.config:
            properties = self.config[asset_class]
            for name, value in properties:
                dir_path = value.split('||')[0]
                if not os.path.isdir(dir_path):
                    raise ValueError(
                        'For System [{0}] Property [{1}]. Dir path doesnt exists {2}'.format(asset_class, name,
                                                                                             dir_path))
            # # check for duplicity of sources and uniqueness of destination
            print('[{0}] Properties look good'.format(asset_class))

    def get_properties_by_qualifier(self, asset_class, qualifier):
        return [(x, v) for x, v in self.config[asset_class] if x.startswith(qualifier)]


if __name__ == '__main__':
    AssetClassFileHandler().process('Rates')