#!/usr/bin/env python
'''
If this fails to work correctly, open the database txt files
and save them explicitly as utf-8.
'''
import os,zipfile,sys,glob
from random import randint
from datetime import datetime
sys.path.append(os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'tripme.settings'

from django.contrib.web_design import lorem_ipsum as lorem
from django.contrib.auth.models import User
from tripme.apps.guides.models import *
from tripme.apps.users.models import *

# -------------------------------------------------------- #
# helper functions for formatting locations
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

# -------------------------------------------------------- #
# helper functions for formatting user data
# -------------------------------------------------------- #
def _user_generator(count):
    ''' Generate a collection of users given a count

    :input count: The number of users to create
    :returns: A user generator
    '''
    for id in xrange(2, count):
        yield return {
#            'id':id,
            'username':'tripuser%s' % id,
            'password':'tripuser%s' % id,
            'email':'tripuser%s@trip.me' % id,
            'first_name':lorem.words(1, common=False),
            'last_name':lorem.words(1, common=False),
        }

def _user_profile_generator(count):
    ''' Generate a collection of users given a count

    :input count: The number of users to create
    :returns: A user generator
    '''
    gender = ['M','F']
    for id in xrange(2, count):
        yield return {
#            'id':id,
            'city':lorem.words(1, common=False),
            'country':lorem.words(1, common=False),
            'zipcode':'%s' % randint(10000, 60000),
            'gender':gender[randint(0,1)],
            'birthdate':datetime.now(),
            'description':lorem.paragraph(),
#            'image':hmmm,
        }

# -------------------------------------------------------- #
# helper functions for formatting user data
# -------------------------------------------------------- #
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
class UserDatabase(object):
    ''' A helper to wrap the user generated objects
    '''
    __user_count = 25

    def __init__(self, **kwargs):
        ''' Initialize a new instance of the database class
        '''
        self.count = kwargs.get('count', self.__user_count)

    def load(self):
        ''' Load all of the database information into django
        '''
        self.save_user(self.count)

    def save_user(self, count):
        ''' Store all the countries from the database into django
        '''
        collection = zip(_user_generator(count),_user_profile_generator(count))
        for user, profile in collection:
            u = User(**user)
            u.save()
            profile.update({'user':u})
            p = UserProfile(**profile)
            p.save()

class LocationDatabase(object):
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

    def load(self):
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
def populate_locations():
    ''' main runner script '''
    if len(glob.glob("*.txt")) == 0:
        zipfile.ZipFile('geo-world-map.zip').extractall('.')

    handle = LocationDatabase()
    print "starting location database load..."
    handle.load()
    print "finished loading (countries:%s), (regions:%s), (cities:%s)" % (
        len(handle.countries),
        len(handle.regions),
        len(handle.cities)
    )

def populate_users():
    ''' main runner script '''
    handle = UserDatabase()
    print "starting location database load..."
    handle.load()
    print "finished loading (users:%s)" % handle.count

def main():
    #populate_locations()
    #populate_users()
    pass

if __name__ == "__main__":
    sys.exit(main())
