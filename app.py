import pickle
import streamlit as st

def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_l = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_l:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies = pickle.load(open("movies.pkl", "rb"))
movies_list = movies["title"].values
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox("Select a movie to recommend", movies_list)

if st.button("Recommend"):
    names = recommend(selected_movie_name)
    for i in names:
        st.write(i)