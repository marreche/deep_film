import pandas as pd
import numpy as np

movies = pd.read_csv("/home/marrechea/deep_film/data/movies_metadata.csv")
movies_df = pd.DataFrame(np.array([
    ["The Shawshank Redemption","278", "https://m.media-amazon.com/images/I/71AzwgLT2WL._AC_SY679_.jpg"],
    ["Toy Story", "862", "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_FMjpg_UX1000_.jpg"],
    ["Jumanji", "8844", "https://cdn.shopify.com/s/files/1/0037/8008/3782/products/jumanji-DoubleSidedOneSheet-VeryGoodtoFine_framed1-805948.jpg?v=1611688061"],
    ["The 40 Year Old Virgin", "6957", "https://m.media-amazon.com/images/I/51F1M8eR+mL._AC_.jpg"],
    ["Titanic", "597", "https://m.media-amazon.com/images/I/91J0KtuFMAL._AC_SY606_.jpg"],
    ["Se7en", "807", "https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"],
    ["Forrest Gump", "13", "https://m.media-amazon.com/images/I/61F7SuvJ58L._AC_SL1000_.jpg"],
    ["Dazed and Confused", "9571", "https://m.media-amazon.com/images/M/MV5BMTM5MDY5MDQyOV5BMl5BanBnXkFtZTgwMzM3NzMxMDE@._V1_.jpg"],
    ["Jurassic Park", "329", "https://static.posters.cz/image/1300/posters/jurassic-park-i75969.jpg"],
    ["Home Alone", "771", "https://m.media-amazon.com/images/I/717la8Z17sL._AC_SL1000_.jpg"],
    ["Pretty Woman", "114", "https://m.media-amazon.com/images/I/515WwjbjAtL._AC_.jpg"],
    ["Space Jam", "2300", "https://m.media-amazon.com/images/I/51Fi7cGqjCL._AC_.jpg"],
    ["Trainspotting", "627", "https://m.media-amazon.com/images/I/512vQ8mAGEL._AC_.jpg"],
    ["The Godfather", "238", "https://m.media-amazon.com/images/I/61ehu0M3T+L._AC_SY741_.jpg"],
    ["The Parent Trap", "9820", "https://m.media-amazon.com/images/I/51BtxVYq91L._AC_SY450_.jpg"],
    ["Cool Runnings", "864", "https://m.media-amazon.com/images/I/51Llq9AfPCL._AC_.jpg"],
    ["Mary Poppins", "433", "https://m.media-amazon.com/images/I/51rJLvRdSoL._AC_.jpg"],
    ["The Dark Knight", "155", "https://m.media-amazon.com/images/I/81pgKxHzBDL._AC_SY679_.jpg"],
    ["Mulan", "10674", "https://lumiere-a.akamaihd.net/v1/images/p_mulan_20529_83d3893a.jpeg"],
    ["Good Will Hunting", "489", "https://m.media-amazon.com/images/I/51OV3-6n+pL._AC_.jpg"],
]),
columns = ['title', 'movieId', 'poster_path'])