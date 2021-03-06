import pandas as pd
import numpy as np

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
    ["GoldenEye", "710", "https://m.media-amazon.com/images/I/81mgxYNdvuL._AC_SL1500_.jpg"],
    ["Pulp Fiction", "660", "https://static.posters.cz/image/750/posters/pulp-fiction-cover-i1288.jpg"],
    ["Back to the Future Part II", "165", "https://m.media-amazon.com/images/I/91utm9FZ7eL._AC_SL1500_.jpg"],
    ["Saving Private Ryan", "857", "https://m.media-amazon.com/images/I/51FiFegjEXL._AC_.jpg"],
    ["Kramer vs. Kramer", "12102", "https://m.media-amazon.com/images/I/51EGUm40MDL._AC_.jpg"],
    ["The Little Mermaid", "10144", "https://m.media-amazon.com/images/I/51PgfGVZiNL._AC_.jpg"],
    ["American History X ", "73", "https://m.media-amazon.com/images/I/51UsXlBAaPL._AC_.jpg"],
    ["A Bug's Life", "9487", "https://m.media-amazon.com/images/I/51s8DeODbmL._AC_.jpg"],
    ["The Karate Kid", "1885", "https://m.media-amazon.com/images/I/61FSCCDZF6S._AC_SX466_.jpg"],
    ["Fight Club", "550", "https://m.media-amazon.com/images/I/71YFxhhSRPL._SY445_.jpg"],
    ["Star Wars: Episode I - The Phantom Menace", "1893", "https://m.media-amazon.com/images/I/71RnVVa7AlL._AC_SY679_.jpg"],
    ["Ghostbusters", "620", "https://m.media-amazon.com/images/I/81Pz44xom+L._AC_SY879_.jpg"],
    ["Big", "2280", "https://m.media-amazon.com/images/I/719-Gr9WKVL._AC_SY500_.jpg"],
    ["The Beach", "1907", "https://m.media-amazon.com/images/I/511NF34BftL._AC_.jpg"],
    ["X-Men", "36657", "https://m.media-amazon.com/images/I/51swWuzY0tL._AC_.jpg"],
    ["Wall Street", "10673", "https://m.media-amazon.com/images/I/51x4YZPo9WL._AC_.jpg"],
    ["Memento", "77", "https://m.media-amazon.com/images/I/51jojzqpkPL._AC_.jpg"],
    ["Blow", "4133", "https://m.media-amazon.com/images/I/71MfSnqITnL._AC_SY679_.jpg"],
    ["Shrek", "808", "https://m.media-amazon.com/images/I/71HPEO8IJTL._AC_SY679_.jpg"],
    ["A Beautiful Mind", "453", "https://m.media-amazon.com/images/I/71AHkwimfJL._AC_SY679_.jpg"],
    ["Monsters, Inc.", "585", "https://m.media-amazon.com/images/I/51Y3UST2tBL._AC_SY450_.jpg"],
    ["The Pianist", "423", "https://www.movienco.co.uk/carteles/4800/4844/001.jpg"],
    ["Spider-Man", "557", "https://m.media-amazon.com/images/I/516CPJtfhTL._AC_.jpg"],
    ["Scarface", "111", "https://m.media-amazon.com/images/I/61luAu5kqTL._AC_SY550_.jpg"],

]),
columns = ['title', 'movieId', 'poster_path'])