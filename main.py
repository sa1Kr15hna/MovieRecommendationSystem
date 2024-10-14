import streamlit as st
import pickle
import requests
import api


moviesListdf = pickle.load(open('movies.pkl', 'rb'))
moviesList = moviesListdf['title'].values
similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movies Recommender System')


def fetchposter(movieId):
    url = f"https://api.themoviedb.org/3/movie/{movieId}?api_key={api.api_key}"
    response = requests.get(url)
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


def recommend(movie):
    movieIndex = moviesListdf[moviesListdf['title'] == movie].index[0]
    vecDistances = similarity_matrix[movieIndex]
    top5MoviesIndexes = sorted(list(enumerate(vecDistances)),reverse=True,key = lambda x:x[1])[1:6]

    recommendedMovies = []
    recommendedMoviePosters=[]
    for i in top5MoviesIndexes:
        recommendedMovies.append(moviesListdf.iloc[i[0]].title)
        recommendedMoviePosters.append(fetchposter(moviesListdf.iloc[i[0]].id))
    return recommendedMovies, recommendedMoviePosters

selectedMovie = st.selectbox(
    "Enter a movie you like",
    moviesList
)

if st.button("Recommend"):
    recs, posters = recommend(selectedMovie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(recs[0])

    with col2:
        st.image(posters[1])
        st.text(recs[1])
    with col3:
        st.image(posters[2])
        st.text(recs[2])

    with col4:
        st.image(posters[3])
        st.text(recs[3])
    with col5:
        st.image(posters[4])
        st.text(recs[4])
