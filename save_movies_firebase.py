# from firebase import firebase
import json, pickle, re


def filter_tags(tagjson, movietitle):

  moviewords = set(movietitle.lower().split())
  regex = r'(?u)[^\w\s-]'
  alltags = [re.sub(regex, '', tag['term'], re.UNICODE).strip() for tag in tagjson['tags']]
  return list(set(filter(lambda tag: len(tag) > 0 and len(moviewords.intersection(tag.lower().split())) == 0, alltags)))

def main():

  f = open('imdb_movies.pickle','r')
  imdb_movies = pickle.load(f)
  f.close()

  f = open('neofonie_movies.pickle','r')
  neofonie_movies = pickle.load(f)
  f.close()

  mm_movies = []

  fb = firebase.FirebaseApplication('https://popping-heat-9121.firebaseio.com/', None)

  for i,m in imdb_movies.items():
    mm_movie = {}
    title = m['Title']
    try:
      neofonie_movie = neofonie_movies[i]
      mm_movie['Title'] = title
      mm_movie['Tags'] = filter_tags(neofonie_movie, title)
      mm_movie['Cover_Url'] = 'http://ampelmann.webfactional.com/images/'+i+'.jpg'
      mm_movie['IMDB_Id'] = i
      mm_movies.append(mm_movie)
      #write to firebase
      result = fb.post('/movies', mm_movie)
      print result
    except:
      print "Failed: Id",i , "not in German Wiki Top 100 grossing, Title:", title

if __name__ == "__main__":
  main()
