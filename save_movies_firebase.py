from firebase import firebase
import json, pickle


def filter_tags(tagjson, movietitle):

  moviewords = set(movietitle.lower().split())
  alltags = [tag['term'] for tag in tagjson['tags']]
  return filter(lambda tag: len(moviewords.intersection(tag.lower().split())) == 0, alltags)

def main():

  f = open('imdb_movies.pickle','r')
  imdb_movies = pickle.load(f)
  f.close()

  f = open('neofonie_movies.pickle','r')
  neofonie_movies = pickle.load(f)
  f.close()

  mm_movies = []

  for i in imdb_movies:
    mm_movie = {}
    try:
      neofonie_movie = neofonie_movies[i.getID()]
      title = i['title']
      mm_movie['Title'] = title
      mm_movie['Tags'] = filter_tags(neofonie_movie, title)
      mm_movie['Cover_Url'] = i['full-size cover url']
      mm_movie['IMDB_Id'] = i.getID()
      mm_movies.append(mm_movie)
    except:
      print "Failed:", i.getID()

    #write to firebase
    firebase = firebase.FirebaseApplication('https://popping-heat-9121.firebaseio.com/', None)
    for m in mm_movies:
      result = firebase.post('/movies', m)
      print result


if __name__ == "__main__":
  main()
