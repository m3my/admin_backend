import json, pickle, re


def filter_tags(tagjson, movietitle):

  moviewords = set(movietitle.lower().split())
  alltags = [re.sub(r'[^a-zA-Z0-9 ]', '', tag['term']) for tag in tagjson['tags']]
  return list(set(filter(lambda tag: len(tag) > 0 and len(moviewords.intersection(tag.lower().split())) == 0, alltags)))

def main():

  f = open('imdb_movies.pickle','r')
  imdb_movies = pickle.load(f)
  f.close()

  f = open('neofonie_movies.pickle','r')
  neofonie_movies = pickle.load(f)
  f.close()

  mm_movies = {}

  for i,m in imdb_movies.items():
    mm_movie = {}
    title = m['Title']
    try:
      neofonie_movie = neofonie_movies[i]
      mm_movie['imdbId'] = i
      mm_movie['title'] = title
      mm_movie['coverUrl'] = 'http://ampelmann.webfactional.com/images/'+i+'.jpg'
      mm_movie['tags'] = filter_tags(neofonie_movie, title)
      #write to firebase
      mm_movies[i] = mm_movie
    except:
      print "Failed: Id",i , "not in German Wiki Top 100 grossing, Title:", title

  f = open('movies.json','w')
  f.write(json.dumps(mm_movies))
  f.close()

if __name__ == "__main__":
  main()
