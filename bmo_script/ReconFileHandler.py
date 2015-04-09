__author__ = 'agupt15'

import os
import shutil
import datetime
import fnmatch
import argparse

SYSTEMS = ['Rates', 'FX', 'Equities', 'Commodities']
QUALIFIERS = ['SOURCE', 'DESTINATION']

# # Utility methods
DELIMITER = '||'
DATE_PATTERN = 'YYYYMMDD'


def pad_zero(x):
    if x is None:
        return ''
    elif x < 10:
        return '0' + str(x)
    return x


def get_formatted_date(date):
    if date is None or date.strip() == '':
        today = datetime.date.today()
    return '{0}{1}{2}'.format(today.year, pad_zero(today.month), pad_zero(today.day))


class AssetClassFileHandler:
    def __init__(self, date=None):
        self.process_date = get_formatted_date(date)
        print('Working for date: {0}'.format(self.process_date))
        self.config = ConfigFile()

    def process(self, asset_class):
        asset_class = asset_class.strip()
        print("Processing Asset Class [{1}] for date: {0}".format(self.process_date, asset_class))
        asset_class_working = 'FX'
        sources = self.config.get_properties_by_qualifier(asset_class_working, 'SOURCE')
        destination, ok_file = self.config.get_properties_by_qualifier(asset_class_working, 'DESTINATION')[0][1].split(
            DELIMITER)
        # # Little Deviation for Rates class.
        if asset_class in ['Rates']:
            ok_file = ok_file.replace(DATE_PATTERN, self.process_date)
        print('Asset Class [{1}] has destination {0}. OK File: {2}'.format(destination, asset_class, ok_file))
        source_status = []
        for source, value in sources:
            print('Processing source {0}'.format(source))
            value = value + DELIMITER + "False"
            src_tuple = src_path, src_pattern, dest_pattern, status = value.split('||')
            source_status.append(src_tuple)
            src_pattern = src_pattern.replace(DATE_PATTERN, self.process_date)
            for file in os.listdir(src_path):
                if fnmatch.fnmatch(file, src_pattern):
                    print('MATCH found for File: {0} Pattern {1}'.format(file, src_pattern))
                    src = os.path.join(src_path, file)
                    if self.copy_file(src, file, destination, dest_pattern):
                        src_tuple[3] = True
                    break

        if all([status[3] for status in source_status]):
            # If all statuses are True - Generate the OK file
            print('All transfers went OK - generating the OK FILE')
            abs_file = os.path.join(destination, ok_file)
            with open(abs_file, 'w') as f:
                f.write('')
            print('OK File Generated Successfully. {0} Asset class is completed'.format(asset_class))


    def copy_file(self, src, src_file_name, dest, dest_pattern):
        try:
            print('Trying to copy [{0} to [{1}]]'.format(src, dest))
            dest_file_name = src_file_name
            if DATE_PATTERN in dest_pattern:
                dest_file_name = dest_pattern.replace(DATE_PATTERN, self.process_date)
            elif dest_pattern != 'SAME':
                dest_file_name = dest_pattern
            print('Destination File Name: {0}'.format(dest_file_name))

            shutil.copy(src, dest)
            # Rename the file
            dst_file = os.path.join(dest, src_file_name)
            new_dst_file_name = os.path.join(dest, dest_file_name)
            os.rename(dst_file, new_dst_file_name)

            print('File copied successfully')
            return True
        except IOError:
            print('Could not process the file transfer/rename. OK File would not be generated')
            return False


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
    parser = argparse.ArgumentParser(
        description='Processing Files transfer for Recon for Single or all asset classes for today or a particular date')

    # ##
    # Usage:
    # >>  python ReconFileHandler.py -source Rates -date YYYYMMDD
    # ##
    parser.add_argument("-system", "--hostname", help="Asset Class from {Rates, FX, Commodities, Equities}",
                        default='ALL')
    default_dt = get_formatted_date()
    parser.add_argument("-date", "--username", help="Date in YYYYMMDD format", default=default_dt)

    args = parser.parse_args()

    print("Asset Class {} Date ".format(
        args.system,
        args.date
    ))
    AssetClassFileHandler().process('Rates')