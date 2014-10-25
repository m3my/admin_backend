#!/usr/bin/python
from __future__ import unicode_literals
import json, requests
import pickle, urllib

_titles_ = [

  'Avatar_%E2%80%93_Aufbruch_nach_Pandora',
  'Titanic_(1997)',
  'Marvel%E2%80%99s_The_Avengers',
  'Harry_Potter_und_die_Heiligt%C3%BCmer_des_Todes:_Teil_2',
  'Die_Eisk%C3%B6nigin_%E2%80%93_V%C3%B6llig_unverfroren',
  'Iron_Man_3',
  'Transformers_3',
  'Der_Herr_der_Ringe:_Die_R%C3%BCckkehr_des_K%C3%B6nigs_(Film)',
  'James_Bond_007_%E2%80%93_Skyfall',
  'The_Dark_Knight_Rises',
  'Transformers:_%C3%84ra_des_Untergangs',
  'Pirates_of_the_Caribbean_%E2%80%93_Fluch_der_Karibik_2',
  'Toy_Story_3',
  'Pirates_of_the_Caribbean_%E2%80%93_Fremde_Gezeiten',
  'Jurassic_Park',
  'Star_Wars:_Episode_I_%E2%80%93_Die_dunkle_Bedrohung',
  'Alice_im_Wunderland_(2010)',
  'Der_Hobbit:_Eine_unerwartete_Reise',
  'The_Dark_Knight',
  'Der_K%C3%B6nig_der_L%C3%B6wen',
  'Harry_Potter_und_der_Stein_der_Weisen_(Film)',
  'Ich_%E2%80%93_Einfach_Unverbesserlich_2',
  'Pirates_of_the_Caribbean_%E2%80%93_Am_Ende_der_Welt',
  'Harry_Potter_und_die_Heiligt%C3%BCmer_des_Todes:_Teil_1',
  'Der_Hobbit:_Smaugs_Ein%C3%B6de',
  'Harry_Potter_und_der_Orden_des_Ph%C3%B6nix_(Film)',
  'Findet_Nemo',
  'Harry_Potter_und_der_Halbblutprinz_(Film)',
  'Der_Herr_der_Ringe:_Die_zwei_T%C3%BCrme_(Film)',
  'Shrek_2_%E2%80%93_Der_tollk%C3%BChne_Held_kehrt_zur%C3%BCck',
  'Harry_Potter_und_der_Feuerkelch_(Film)',
  'Spider-Man_3',
  'Ice_Age_3:_Die_Dinosaurier_sind_los',
  'Harry_Potter_und_die_Kammer_des_Schreckens_(Film)',
  'Ice_Age_4_%E2%80%93_Voll_verschoben',
  'Der_Herr_der_Ringe:_Die_Gef%C3%A4hrten_(Film)',
  'Die_Tribute_von_Panem_%E2%80%93_Catching_Fire',
  'Star_Wars:_Episode_III_%E2%80%93_Die_Rache_der_Sith',
  'Transformers_%E2%80%93_Die_Rache',
  'Breaking_Dawn_%E2%80%93_Bis(s)_zum_Ende_der_Nacht_%E2%80%93_Teil_2',
  'Inception',
  'Spider-Man_(Film)',
  'Independence_Day_(1996)',
  'Shrek_der_Dritte',
  'Harry_Potter_und_der_Gefangene_von_Askaban_(Film)',
  'E._T._%E2%80%93_Der_Au%C3%9Ferirdische',
  'Fast_%26_Furious_6',
  'Indiana_Jones_und_das_K%C3%B6nigreich_des_Kristallsch%C3%A4dels',
  'Spider-Man_2',
  'Krieg_der_Sterne',
  '2012_(Film)',
  'The_Da_Vinci_Code_%E2%80%93_Sakrileg',
  'The_Amazing_Spider-Man_(2012)',
  'Maleficent_%E2%80%93_Die_dunkle_Fee',
  'F%C3%BCr_immer_Shrek',
  'Madagascar_3:_Flucht_durch_Europa',
  'X-Men:_Zukunft_ist_Vergangenheit',
  'Die_Chroniken_von_Narnia:_Der_K%C3%B6nig_von_Narnia_(2005)',
  'Die_Monster_Uni',
  'Matrix_Reloaded',
  'Guardians_of_the_Galaxy',
  'Oben',
  'Gravity_(Film)',
  'The_Return_of_the_First_Avenger',
  'Breaking_Dawn_%E2%80%93_Bis(s)_zum_Ende_der_Nacht_%E2%80%93_Teil_1',
  'New_Moon_%E2%80%93_Bis(s)_zur_Mittagsstunde',
  'Transformers_(Film)',
  'The_Amazing_Spider-Man_2:_Rise_of_Electro',
  'Planet_der_Affen:_Revolution',
  'Eclipse_%E2%80%93_Bis(s)_zum_Abendrot',
  'Mission:_Impossible_%E2%80%93_Phantom_Protokoll',
  'Die_Tribute_von_Panem_%E2%80%93_The_Hunger_Games',
  'Forrest_Gump',
  'The_Sixth_Sense',
  'Man_of_Steel_(Film)',
  'Kung_Fu_Panda_2',
  'Ice_Age_2:_Jetzt_taut%E2%80%99s',
  'Fluch_der_Karibik',
  'Star_Wars:_Episode_II_%E2%80%93_Angriff_der_Klonkrieger',
  'Thor_%E2%80%93_The_Dark_Kingdom',
  'Kung_Fu_Panda',
  'Die_Unglaublichen_%E2%80%93_The_Incredibles',
  'Fast_%26_Furious_Five',
  'Hancock_(Film)',
  'Men_in_Black_3',
  'Iron_Man_2',
  'Ratatouille_(Film)',
  'Vergessene_Welt:_Jurassic_Park',
  'Drachenz%C3%A4hmen_leicht_gemacht_2',
  'Die_Passion_Christi',
  'Mamma_Mia!_(Film)',
  'Life_of_Pi:_Schiffbruch_mit_Tiger',
  'Madagascar_2',
  'James_Bond_007:_Casino_Royale',
  'Rapunzel_%E2%80%93_Neu_verf%C3%B6hnt',
  'Krieg_der_Welten_(Film)',
  'Men_in_Black_(Film)',
  'Die_Croods',
  'Hangover_2'
]

def get_imdb_id(title):
  base = 'http://de.wikipedia.org/wiki/' + title
  r = requests.get(base)
  result = None
  if r.status_code == 200:
    start = r.text.find('http://www.imdb.com/title/tt')+28
    result = r.text[start:start+7]
    print result
  else:
    print "There's something wrong! Expected code 200, got " + str(r.status_code) + "."

  return result

def get_plot_wiki(title):
  base = 'http://de.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&rvsection=1&redirects=&titles=' + title
  r = requests.get(base)
  result = None
  if r.status_code == 200:
    try:
      result = json.loads(r.text)['query']['pages'].values()[0]['revisions'][0]['*']
    except:
      print json.loads(r.text)['query']['pages'].values()[0]
  else:
    print "There's something wrong! Expected code 200, got " + str(r.status_code) + "."

  return result

def main():
  wiki_movies = {}
  for t in _titles_:
    p = get_plot_wiki(t)
    if p:
      imdbid = get_imdb_id(t)
      if imdbid:
        wiki_movies[imdbid] = p

  f = open('wiki_movies.pickle','w')
  f.write(pickle.dumps(wiki_movies))
  f.close()

if __name__ == "__main__":
  main()
