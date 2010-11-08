#!/usr/bin/env python
'''
If this fails to work correctly, open the database txt files
and save them explicitly as utf-8.
'''
import os,zipfile,sys,glob
sys.path.append(os.path.join(os.path.abspath('..'), '.'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'tripme.settings'

from tripme.guides.models import *
# from django.core.management import setup_environ
# setup_environ(settings)
# from tripme import settings

# -------------------------------------------------------- #
# helper functions for manipulating files
# -------------------------------------------------------- #
def _country_formatter(line):
    ''' Convert a line in the country database to a dictionary

    :input line: The line to convert to a dictionary
    :returns: The converted dictionary
    '''
    fields = [value.replace('"','') for value in line.split(',')]
    return {
        'id':int(fields[0]),
        'name':fields[1],
        'code':fields[3],
        'capital':fields[7],
        'reference':fields[8],
    }

def _region_formatter(line):
    ''' Convert a line in the region database to a dictionary

    :input line: The line to convert to a dictionary
    :returns: The converted dictionary
    '''
    fields = [value.replace('"','') for value in line.split(',')]
    return {
        'id':int(fields[0]),
        'country_id':int(fields[1]),
        'name':fields[2],
        'code':fields[3],
    }

def _city_formatter(line):
    ''' Convert a line in the city database to a dictionary

    :input line: The line to convert to a dictionary
    :returns: The converted dictionary
    '''
    fields = [value.replace('"','') for value in line.split(',')]
    return {
        'id':int(fields[0]),
        'name':fields[3],
        'code':fields[8],
        'country_id':int(fields[1]),
        'region_id':int(fields[2]),
        'latitude':fields[4],
        'longitude':fields[5],
        'timezone':fields[6],
    }

def file_generator(filename):
    ''' Given a filename, return a generator over that file

    :input filename: The filename to convert to a generator
    :return: The generator over the given file
    '''
    import codecs
    with codecs.open(filename, mode="r", encoding="utf-8") as handle:
        handle.readline() # jump over header
        for line in handle:
            yield line

def format_file(file, formatter):
    ''' A helper function to supply a format function
    to every line of a file

    :input file: The file to format
    :input formatter: The format function to map each line to
    :returns: An array of convert lines in the file
    '''
    return [formatter(line) for line in file_generator(file)]

# -------------------------------------------------------- #
# manager classes
# -------------------------------------------------------- #
class Database(object):
    ''' A helper to wrap the file database objects
    '''
    __city_file    = "Cities.txt"
    __country_file = "Countries.txt"
    __region_file  = "Regions.txt"

    def __init__(self):
        ''' Initialize a new instance of the database class
        '''
        self.cities = format_file(self.__city_file, _city_formatter)
        self.regions = format_file(self.__region_file, _region_formatter)
        self.countries = format_file(self.__country_file, _country_formatter)

    def save_all(self):
        ''' Load all of the database information into django
        '''
        self.save_countries()
        self.save_regions()
        self.save_cities()

    def save_countries(self):
        ''' Store all the countries from the database into django
        '''
        for country in self.countries:
            c = Country(**country)
            c.save()

    def save_regions(self):
        ''' Store all the regions from the database into django
        '''
        for region in self.regions:
            r = Region(**region)
            r.save()

    def save_cities(self):
        ''' Store all the cities from the database into django
        '''
        for city in self.cities:
            c = City(**city)
            c.save()

# -------------------------------------------------------- #
# main runner script
# -------------------------------------------------------- #
def main():
    ''' main runner script '''
    if len(glob.glob("*.txt")) == 0:
        zipfile.ZipFile('geo-world-map.zip').extractall('.')

    handle = Database()
    print "starting database load..."
    handle.save_all()
    print "finished loading (countries:%s), (regions:%s), (cities:%s)" % (
        len(handle.countries),
        len(handle.regions),
        len(handle.cities)
    )

if __name__ == "__main__":
    sys.exit(main())
