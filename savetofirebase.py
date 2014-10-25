from firebase import firebase
import json

# Get movie data
moviesfile = open('50movies.json')

moviesstring = moviesfile.read()
moviesjson = json.loads(moviesstring)
movieslist = moviesjson['results']['bindings']

#write to firebase
firebase = firebase.FirebaseApplication('https://popping-heat-9121.firebaseio.com/', None)

for movie in movieslist[:2]:
   result = firebase.post('/movies', movie['film_title']['value'])
   print result
