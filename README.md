# <div align="center"> :movie_camera: deep_film </div>

![Alt](/images/movies_collage.jpg "Movies")



## :scroll: Table of Contents

* [About](#newspaper-about)
* [Movie Recommender](#film_strip-movie-recommender)
* [API](#bulb-api)
    * [Endpoints](#endpoints)
* [Dashboard](#streamlit-dashboard)
* [Resources](#notebook_with_decorative_cover-resources)
* [Contact](#envelope-contact)
* [License](#key-license)

## :newspaper: About

This project consists of a Movie Recommender System using [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) from kaggle. This dataset contains metadata for all 45,000 movies listed in the Full MovieLens Dataset. As well as 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

The deep_film recommender system is supplemented by its very own MongoAtlas database, where all movie and user data is stored, an API for better connectivity and a Streamlit Dashboard. Down below you will find instructions to use both the Streamlit Dashboard as well as the API.

deep_film uses a Singular Value Decomposition (SVD) model as it harnessed the best results. K-Nearest Neighbours (KNN) was also tested. 

If you wish to know more about this project and the development process don't hesitate to send me an [email](#envelope-contact).

## :film_strip: Movie Recommender System

To use my recommendation system you must first rate twenty movies on a scale from 1 to 5. After completion, the model will calculate up to 5 best rated movies that fit your preferences. Head over to the [Streamlit Dashboard](#streamlit-dashboard) section to learn more on how to use the recommender system.

## :bulb: API 

This project is complemented by its own API acting as an intermmediary between the MongoAtlas database and the Streamlit dashboard. If you wish to use the API directly, you may query the endpoints listed down below.

### Endpoints

1. /movies - Returns all movies in the database.
2. /movies/search - GET
- Params
    - name -> Introduce name of desired movie to search. (Required)
3. /movies/poster - GET
- Params
    - name -> Introduce name of desired movie to get link to poster. (Required)
4. /add - GET, POST
- Params
    - rating -> Introduce rating. (Required)
    - userId -> Introduce userId. (Optional)
    - movieId -> Introduce movieId. (Required)

## Streamlit Dashboard

The implementation of the Deep Film recommender system is hosted on a Streamlit dashboard.

Click on link below to visit the dashboard where the recommender system is hosted :

## [Deep Film Dashboard]()

## :notebook_with_decorative_cover: Resources

[Surprise](https://surprise.readthedocs.io/en/stable/)

[Ibtesam Ahmed's "Getting Started with a Movie Recommendation System"](https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system)  

[Rounak Banik's "Movie Recommender Systems"](https://www.kaggle.com/rounakbanik/movie-recommender-systems)
## :envelope: Contact

mauriarrechea@gmail.com
## :key: License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="right"><a href="#scroll-table-of-contents">&#11014; Back to contents</a></div>