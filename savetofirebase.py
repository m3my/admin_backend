from firebase import firebase
import json, pickle


f = open('imdb_movies.pickle','r')
imdb_movies = pickle.load(f)
f.close()

f = open('neofonie_movies.pickle','r')
neofonie_movies = pickle.load(f)
f.close()

mm_movies = []

for i in imdb_movies:
  mm_movie = {}
  neofonie_movie = neofonie_movies[i.getID()]
  mm_movie['Title'] = i['title']
  mm_movie['Tags'] = [tag['term'] for tag in neofonie_movie['tags']]
  mm_movie['Cover_Url'] = i['full-size cover url']
  mm_movie['IMDB_Id'] = i.getID()
  mm_movies.append(mm_movie)

#write to firebase
firebase = firebase.FirebaseApplication('https://popping-heat-9121.firebaseio.com/', None)
for m in mm_movies:
  result = firebase.post('/movies', m)
  print result
