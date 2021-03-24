import imdb
from tabulate import tabulate


ia = imdb.IMDb()
list_movies = ["Minari","Sound of Metal","Mank","Promising Young Woman",
          "The Father", "Judas and the Black Messiah","The Trial of the Chicago 7", "Nomadland"]

#list_movies = ["Minari"]

data = []
for mov in list_movies:
  info = []
  movies = ia.search_movie(str(mov))
  year = movies[0]['year'] 

  rating = ia.get_movie(str(movies[0].movieID))
  rating = rating.data['rating']

  movie = ia.get_movie(str(movies[0].movieID))
  #print('Directors:')
  directors = []
  for director in movie['directors']:
      directors.append(str(director))

  plot = str(movie.get('plot'))

  #print(movie.get('plot')) 
  
  cast = movie.data['cast']
  cast = cast[:5]

  cast_names = []
  for i in range(0,5):
    cast_names.append(str(cast[i]))

  #print(cast_names)
  
  genre = str(movie.data['genres'])

  #print(genre)
  info = [year,rating,directors,plot,cast_names,genre]
  data.append(info)
  #print(info)

#print(tabulate(data,headers=["Year","Rating","Directos","Plot","Cast","Genre"]))

#escribir en un archivo
with open('output.txt','w') as archivo_n:
  archivo_n.writelines(tabulate(data,headers=["Year","Rating","Directos","Plot","Cast","Genre"]))
