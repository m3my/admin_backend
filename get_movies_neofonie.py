#!/usr/bin/python
import json, requests
import pickle, urllib

def pprint(j):
  """Pretty-print a JSON object"""
  print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))

def askneofonie(text):
  """Ask the neofonie TXT Werk API to extract important tags from a text."""

  apikey = 'b128bbe8-c7d5-47a1-2389-dafb2b8127cb'
  headers = {'X-Api-Key': apikey}
  services = 'tags' # 'categories,date,entities'

  params = urllib.urlencode({'text': unicode(text).encode('utf-8'), 'services':services})
  r = requests.post('https://api.neofonie.de/rest/txt/analyzer', params=params, headers=headers)
  if r.status_code == 200:
    return json.loads(r.text)
  else:
    print "There's something wrong! Expected code 200, got " + str(r.status_code) + "."
    print r.reason
    return None

def main():
  f = open('wiki_movies.pickle','r')
  src_movies = pickle.load(f)
  f.close()

  neofonie_movies = {}
  keys = src_movies.keys()
  keys.sort()
  for k in keys:
    neofonie_movies[k] = askneofonie(src_movies[k][:6500])

  f = open('neofonie_movies.pickle','w')
  f.write(pickle.dumps(neofonie_movies))
  f.close()




if __name__ == "__main__":
  main()
