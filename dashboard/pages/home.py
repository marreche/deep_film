import streamlit as st

def home():
    st.title("Deep Film Recommender System")
    st.write("Welcome to Deep Film, my own take on a movie recommender system")
    st.header("Usage")
    st.write("You can navigate this dashboard by cliclking the arrow at the top left of the page.")
    st.header("Pages")
    st.write("- Get a simple recommendation: Navigate to this page if you wish to get a simple content based recommendation")
    st.write("- Get a recommendations Naviagate to this page if you wish to get a more tailored and accurate recommendation")
    st.write("- Top Fifty Rated Movies: Navigate to this page if you wish to take a look at the top 50 best rated movies")
    st.write("- Docs : Navigate to this page if you wish to explore some useful links and documentation")