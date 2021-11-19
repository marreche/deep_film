# <div align="center"> :movie_camera: deep_film </div>


![Alt](/images/movies_collage.jpg "Movies")



## :scroll: Table of Contents

* [About](#newspaper-about)
* [Movie Recommender](#film_strip-movie-recommender)
* [API](#bulb-api)
    * [Movie Endpoints](#movie-endpoints)
    * [User Endpoints](#user-endpoints)
    * [Rating Endpoints](#rating-endpoints)
* [Streamlit](#clipboard-streamlit-dashboard)
* [Resources](#notebook_with_decorative_cover-useful-resources)
* [Contact](#envelope-contact)
* [License](#key-license)

## :newspaper: About

This project consists of a Movie Recommender System using [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) from kaggle. This dataset contains metadata for all 45,000 movies listed in the Full MovieLens Dataset. As well as 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

The deep_film recommender system is supplemented by its very own MongoAtlas database, where all movie and user data is stored, an API for better connectivity and a Streamlit Dashboard for user interaction. Down below you will find instructions to use both the Streamlit Dashboard as well as the API.

deep_film uses a Singular Value Decomposition (SVD) algorithm as it harnessed the best results in the least amount of time. K-Nearest Neighbours (KNN) was also tested, as well as other matrix factorization based algorithms. SVD++ and NMF are both implemented but are not used in the final recommendation system for different reasons. SVD++ yielded better results than SVD however took an impractical amount of time to recommend films to new users. NMF gave objectively worse and fewer recommendations than SVD. 

Both the API and the Dashboard are hosted on heroku servers, urls can be found in their respective sections.

If you wish to know more about this project and the development process don't hesitate to send me an [email](#envelope-contact).

## :film_strip: Movie Recommender System


To use my recommendation system you must first rate twenty movies on a scale from 1 to 5. After completion, the algorithm will calculate up to 10 movies that fit your preferences. Head over to the [Streamlit Dashboard](#streamlit-dashboard) section to learn more on how to use my recommender system.

## :bulb: API 

## [Deep Film API](https://deep-film-api.herokuapp.com)


This project is complemented by its own API acting as an intermmediary between the MongoAtlas database and the Streamlit dashboard. If you wish to use the API directly, you may query the endpoints listed down below.

### Movie Endpoints
1. /movies
- Returns all movie data in the database.
2. /movies/search - GET
- Params
    - name -> Introduce name of desired movie to search. (Required)
3. /movies/poster - GET
- Params
    - name -> Introduce name of desired movie to get link to poster. (Required)

### User Endpoints
1. /add - GET, POST
- Params
    - rating -> Introduce rating. (Required)
    - userId -> Introduce userId. (Optional)
    - movieId -> Introduce movieId. (Required)

2. /predictions - GET
- Returns all recommended predictions for Streamlit users.


### Rating Endpoints
1. /ratings - GET
- Returns all past user ratings extracted from the "The Movies Dataset".

2. /ratings/new - GET
- Returns ratings added by users casting their ratings on streamlit dashboard.


## :clipboard: Streamlit Dashboard

The implementation of Deep Film is hosted on a Streamlit dashboard.

Click on link below to visit the dashboard:

## [Deep Film Dashboard](https://deep-film-dashboard.herokuapp.com/)

## :notebook_with_decorative_cover: Useful Resources

[Surprise](https://surprise.readthedocs.io/en/stable/)

[Ibtesam Ahmed's "Getting Started with a Movie Recommendation System"](https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system)  

[Rounak Banik's "Movie Recommender Systems"](https://www.kaggle.com/rounakbanik/movie-recommender-systems)
## :envelope: Contact

mauriarrechea@gmail.com
## :key: License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


<img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />


<div align="right"><a href="#top">&#11014; Back to code</a></div>