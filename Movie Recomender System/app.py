import streamlit as st
import joblib


# Load Data
df_movies_reco = joblib.load('data\df_movies_recommendation.pkl')
distinct_movies_list = df_movies_reco.title.unique().tolist()


def get_recomented_movies_list(query_movie):
    reco_movies = df_movies_reco[df_movies_reco.title == query_movie].reco_movies.iloc[0]
    return reco_movies

def get_movie_id(query_movie):
    movie_id = df_movies_reco[df_movies_reco.title == query_movie].id.iloc[0]
    return movie_id

# Set Up Title
st.title("MOVIE RECOMMENDER SYSTEM")
query_movie = st.selectbox('SELECT MOVIE',distinct_movies_list)

if st.button("Recommend"):
    reco_movies = get_recomented_movies_list(query_movie)
    for movie_name in reco_movies:
        st.write(movie_name)
    # st.write(reco_movies)
    # reco_movies_id_list = [get_movie_id(i) for i in reco_movies]
    # st.write(reco_movies_id_list)

