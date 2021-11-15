import streamlit as st
from support.api_connection import get_movies

def recommender():
    title = st.title("Recommender")
    start = st.button("Start Rating Movies", key="start_button")
    if start:
        img =  "https://m.media-amazon.com/images/I/71AzwgLT2WL._AC_SY679_.jpg"
        if 'img' not in st.session_state:
            st.session_state.img = "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_FMjpg_UX1000_.jpg"
        st.image(img)
        slider = st.slider("Rate Movie", min_value=0, max_value=5, value=3, step=1, key= 'slider')
        next_movie = st.button('Next Movie')
        if next_movie:
            st.session_state.img = "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_FMjpg_UX1000_.jpg"
            st.image(st.session_state.img)
            slider_two = st.slider("Rate Movie", min_value=0, max_value=5, value=3, step=1, key= 'slider_two')
            next_movie = st.button('Next Movie',key="button_two")


    
    
    
    
    
    
    # if 'img' not in st.session_state:
    #     st.session_state.img = "https://m.media-amazon.com/images/I/71AzwgLT2WL._AC_SY679_.jpg"
    # slider = st.slider("Rate Movie", min_value=0, max_value=5, value=3, step=1, key= 'slider')
    # next = st.button("Next Movie")
    # if next:
    #     st.session_state.img = "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_FMjpg_UX1000_.jpg"
    # st.image(st.session_state.img)
    

        ##rating = value given by user


    ## toy story img = st.image("https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_FMjpg_UX1000_.jpg")
