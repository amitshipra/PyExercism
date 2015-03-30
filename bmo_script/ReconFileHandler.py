__author__ = 'agupt15'

import os
import shutil

SYSTEMS = ['RATES', 'FX']
QUALIFIERS = ['SOURCE', 'DTCC', 'DESTINATION']


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
                    ok_filename = file+".OK"
                abs_file = os.path.join(dtcc_folder, ok_filename)
                with open(abs_file, 'w') as f:
                    f.write('')


if __name__ == '__main__':
    FileHandler().process()