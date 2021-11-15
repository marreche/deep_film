# <div align="center"> :movie_camera: deep_film </div>

![Alt](/images/movies_collage.jpg "Movies")



## :scroll: Table of Contents

* [About](#newspaper-about)
* [Movie Recommender](#film_strip-movie-recommender)
* [API](#bulb-api)
* [Resources](#notebook_with_decorative_cover-resources)
* [Contact](#envelope-contact)
* [License](#key-license)

## :newspaper: About

This project consists of a Movie Recommender System using [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) from kaggle. This dataset contains metadata for all 45,000 movies listed in the Full MovieLens Dataset. As well as 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

The deep_film recommender system is supplemented by its very own MongoAtlas database, where all movie and user data is stored, as well as an API for easier access. Down below you will find instructions to use both the recommender system as well as the API.

deep_film uses a Singular Value Decomposition (SVD) model as it harnessed the best results. Although K-Nearest Neighbours (KNN) was also tested.

## :film_strip: Movie Recommender System

To use my recommendation system you must first rate the five films on a scale from 1 to 5. After completion, the model will calculate the 5 best rated movies that fit your preferences. 

## :bulb: API 

### Endpoints

1. /movies - Returns all movies in the database.
2. /movies/search - GET
- Params
    - name -> Introduce name of desired movie to search.
3. /movies/poster - GET
- Params
    - name -> Introduce name of desired movie to get link to poster.
4. /add - POST
- Params
    - rating

## :notebook_with_decorative_cover: Resources

[Surprise](https://surprise.readthedocs.io/en/stable/)

[Ibtesam Ahmed's "Getting Started with a Movie Recommendation System"](https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system)  

[Rounak Banik's "Movie Recommender Systems"](https://www.kaggle.com/rounakbanik/movie-recommender-systems)
## :envelope: Contact

mauriarrechea@gmail.com
## :key: License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="right"><a href="#scroll-table-of-contents">&#11014; Back to contents</a></div>