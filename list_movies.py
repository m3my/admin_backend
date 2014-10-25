#!/usr/bin/python
#
# list_movies.py
#
# list movies retrieved from imdb
#
# Copyright (C) 2014 Jeremy Tammik, Autodesk Inc.
#
#from __future__ import unicode_literals
import json, requests
from optparse import OptionParser
from imdb import IMDb

_version = '1.0'

_keys = [
  'cast',
  'cover url',
  'director',
  'full-size cover url',
  'genres',
  #'long imdb title',
  'plot',
  'plot outline',
  'producer',
  'writer',
  'year']

_key_title = 'long imdb title'

_movie_ids = [
  '0111161',
  '0068646',
  '0071562',
  '0468569',
  '0110912',
  '0060196',
  '0108052',
  '0050083',
  '0167260',
  '0137523',
  '0120737',
  '0080684',
  '1375666',
  '0109830',
  '0073486',
  '0167261',
  '0099685',
  '0133093',
  '0076759',
  '0047478',
  '0317248',
  '0114369',
  '0114814',
  '0102926',
  '0038650',
  '0064116',
  '0110413',
  '0118799',
  '0034583',
  '0082971',
  '0120586',
  '0054215',
  '0120815',
  '0047396',
  '0021749',
  '0245429',
  '1675434',
  '0027977',
  '0103064',
  '0209144',
  '0253474',
  '0120689',
  '0043014',
  '0078788',
  '0057012',
  '0407887',
  '0172495',
  '0088763',
  '0078748',
  '1065073',
  '0482571',
  '1345836',
  '0405094',
  '1853728',
  '0032553',
  '0110357',
  '0081505',
  '0095765',
  '0050825',
  '0169547',
  '0910970',
  '2015381',
  '0053125',
  '0090605',
  '0033467',
  '0211915',
  '0052357',
  '0435761',
  '0022100',
  '0082096',
  '0364569',
  '0119698',
  '0066921',
  '0086190',
  '0095327',
  '0075314',
  '0087843',
  '0105236',
  '0036775',
  '2267998',
  '0180093',
  '0112573',
  '0056592',
  '0056172',
  '0338013',
  '0051201',
  '0093058',
  '0045152',
  '0070735',
  '0040522',
  '0086879',
  '0071853',
  '0208092',
  '0119488',
  '0042192',
  '0042876',
  '0053604',
  '0059578',
  '0040897',
  '0053291',
  '0012349',
  '0041959',
  '0361748',
  '0097576',
  '0062622',
  '1832382',
  '0372784',
  '0055630',
  '0017136',
  '0114709',
  '0105695',
  '0081398',
  '0086250',
  '0071315',
  '1049413',
  '0095016',
  '0363163',
  '0986264',
  '0057115',
  '0457430',
  '0031679',
  '0047296',
  '0113277',
  '0050212',
  '2106476',
  '1187043',
  '0993846',
  '0119217',
  '0050976',
  '0096283',
  '0080678',
  '0050986',
  '0015864',
  '0089881',
  '0083658',
  '0017925',
  '0120735',
  '0044741',
  '1205489',
  '1305806',
  '0112641',
  '0118715',
  '0032976',
  '1291584',
  '0434409',
  '0025316',
  '0077416',
  '0347149',
  '0061512',
  '1979320',
  '0892769',
  '0116282',
  '0031381',
  '0292490',
  '0117951',
  '0033870',
  '0758758',
  '0055031',
  '0405508',
  '0268978',
  '0395169',
  '0167404',
  '0046912',
  '0084787',
  '2024544',
  '0064115',
  '1877832',
  '0266543',
  '0477348',
  '0266697',
  '0046268',
  '0091763',
  '0978762',
  '0079470',
  '0401792',
  '0075686',
  '0074958',
  '0052311',
  '2278388',
  '1255953',
  '0046911',
  '0093779',
  '0092005',
  '0469494',
  '0052618',
  '0245712',
  '0032138',
  '0405159',
  '0848228',
  '0032551',
  '0053198',
  '1028532',
  '0107207',
  '0036868',
  '0440963',
  '0060827',
  '0246578',
  '0083987',
  '0044079',
  '0056801',
  '0087544',
  '0073195',
  '0338564',
  '0044706',
  '0114746',
  '1504320',
  '0038787',
  '0088247',
  '1130884',
  '0079944',
  '1201607',
  '0107048',
  '1220719',
  '0083922',
  '0075148',
  '0112471',
  '0048424',
  '0072890',
  '0169102',
  '0198781',
  '0113247',
  '0047528',
  '0325980',
  '0058946',
  '0072684',
  '0061184',
  '0353969',
  '0058461',
  '0038355',
  '1798709',
  '0092067',
  '0120382',
  '0061722',
  '1454029',
  '0046250',
  '0054997',
  '0107290',
  '0154420',
  '0118694',
  '0101414',
  '0046359',
  '0040746',
  '1010048',
  '0049406',
  '0085334',
  '0381681',
  '0070511',
  '0111495',
  '0450259',
  '0367110',
]

def get_string(a):
  "extract string form given object."
  if 'imdb.Person.Person' == str(type(a)): return a['name']
  if list == type(a): return ', '.join( [get_string(e) for e in a])
  return str(a)

def pprint(j):
    print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))

def askneofonie(text):
    
    apikey = 'b128bbe8-c7d5-47a1-2389-dafb2b8127cb'
    headers = {'X-Api-Key': apikey}
    services = 'tags' # 'categories,date,entities'

    params = urllib.urlencode({'text': text, 'services':services})
    r = requests.post('https://api.neofonie.de/rest/txt/analyzer', params=params, headers=headers)
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print "There's something wrong! Expected code 200, got " + str(r.status_code) + "."
        return None


def main():
  "list movies retrieved from imdb"

  progname = 'list_movies'
  usage = 'usage: %s [options]' % progname
  parser = OptionParser( usage, version = progname + ' ' + _version )
  parser.add_option( '-?', '--question', action='store_true', dest='question', default=False, help = 'show this help message and exit' )
  #parser.add_option( '-c', '--count', action='store_true', dest='count', default=False, help = 'show data set entry count' )
  #parser.add_option( '-e', '--elasticsearch', action='store_true', dest='elasticsearch', default=False, help = 'read data from ElasticSearch, not GeoJson' )
  #parser.add_option( '-l', '--list', action='store_true', dest='list', default=False, help = 'list data set entries' )
  #parser.add_option( '-p', '--precision', type='int', dest='precision', default=3, help = 'define precision, i.e. 3 or 4 digits' )
  #parser.add_option( '-u', '--url', action='store_true', dest='url', default=False, help = 'generate and list URLs to delete' )
  #parser.add_option( '-q', '--quiet', action='store_true', dest='quiet', help = 'reduce verbosity' )

  (options, args) = parser.parse_args()

  #print options
  #print args

  if options.question:
    raise SystemExit(parser.print_help() or 1)

  ia = IMDb()

  get_one_single_movie = False
  if get_one_single_movie:
    i = '0133093' # The Matrix (1999)
    m = ia.get_movie(i)
    print m[_key_title]+':'
    print '  ', '; '.join([k+'='+get_string(m[k]) for k in _keys])

  search_for_movies = False
  if search_for_movies:
    ids = ia.search_keyword(u'passion')
    print ids
    return

  for i in _movie_ids:
    m = ia.get_movie(i)
    print m[_key_title]+':',
    print '; '.join([k+'='+get_string(m[k]) for k in _keys])

  #for k in _keys:
  #  a = m[k]
  #  print k, a,

  #i += 1



if __name__ == "__main__":
  main()
