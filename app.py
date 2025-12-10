import pickle
import streamlit as st
import requests
import pandas as pd


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en=US".format(movie_id)

    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path

    return full_path






def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommend_movie_name = []
    recommend_movie_posters = []

    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movie_posters.append(fetch_poster(movie_id))

        recommend_movie_name.append(movies.iloc[i[0]].title)
    
    return recommend_movie_name, recommend_movie_posters
    
    
    
    

with st.sidebar:
    st.header("")

st.header('Sistemas de recomendación')
movies = pd.read_pickle('model/movie_list.pkl')
similarity = pd.read_pickle('model/similarity.pkl')
movie_list = movies['title'].values
selected_movie = st.selectbox(
        "Selecciona una película de la lista",
        movie_list
)

import streamlit as st
if st.button('Mostrar Recomendaciones'):
    recommend_movie_name, recommend_movie_posters = recommend(selected_movie)

    cols = st.columns(5)
    
    for i, col in enumerate(cols):
        col.text(recommend_movie_name[i])
        col.image(recommend_movie_posters[i])
    

