# <div align="center"> :movie_camera: deep_film </div>


![Alt](docs/images/movies_collage.jpg "Movies")



## :scroll: Table of Contents

* [About](#newspaper-about)
* [Movie Recommender](#film_strip-movie-recommender-system)
* [API](#bulb-api)
* [Streamlit](#clipboard-dashboard)
* [Resources](#notebook_with_decorative_cover-useful-resources)
* [Contact](#envelope-contact)
* [License](#key-license)

## :newspaper: About

This project consists of a Movie Recommender System using [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) from kaggle. This dataset contains metadata for all 45,000 movies listed in the Full MovieLens Dataset. As well as 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

The deep_film recommender system is supplemented by its very own MongoAtlas database, where all movie and user data is stored, an API for better connectivity and a Streamlit Dashboard for user interaction. Down below you will find instructions to use both the Streamlit Dashboard as well as the API.

deep_film uses a Singular Value Decomposition (SVD) algorithm as it harnessed the best results in the least amount of time. K-Nearest Neighbours (KNN) was also tested, as well as other matrix factorization based algorithms. SVD++ and NMF are both implemented but are not used in the final recommendation system for different reasons. SVD++ yielded better results than SVD however took an impractical amount of time to recommend films to new users. NMF gave objectively worse and fewer recommendations than SVD.

Singular Value Decomposition (SVD) is a method used in linear algebra that is used as a dimensionality reduction technique in machine learning. SVD is a matrix factorisation technique, which reduces the number of features of a dataset. In the context of this movie recommender system, SVD is used as a collaborative filtering technique. It uses a matrix structure where each row represents a user, and each column represents an item. The elements of this matrix are the ratings that are given to items by users.

Both the API and the Dashboard are hosted on heroku servers, urls can be found in their respective sections.

If you wish to know more about this project and the development process don't hesitate to send me an [email](#envelope-contact).

## :film_strip: Movie Recommender System


To use my recommendation system you must first rate twenty movies on a scale from 1 to 5. After completion, the algorithm will calculate up to 10 movies that fit your preferences. Head over to the [Streamlit Dashboard](#streamlit-dashboard) section to learn more on how to use my recommender system.


## :bulb:  [API](https://deep-film-api.herokuapp.com)


This project is complemented by its own API acting as an intermmediary between the MongoAtlas database and the Streamlit dashboard. If you wish to use the API directly, you may query the endpoints listed down below.

## Movie endpoint : Returns all movie data
### Method: GET
>```
>/movies
>```



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Search movie endpoint : Returns info of searched movie
### Method: GET
>```
>/movies/search?name
>```
### Query Params

|Param|value|
|---|---|
|name (REQUIRED)|{desired movie}|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Poster endpoint: Returns desired movie poster
### Method: GET
>```
>/movies/poster?name
>```
### Query Params

|Param|value|
|---|---|
|name (REQUIRED)|{desired movie}|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## User addition endpoint: Adds new user ratings
### Method: GET & POST
>```
>/add?rating&userId&movieId
>```
### Query Params

|Param|value|
|---|---|
|rating (REQUIRED)| {Rating from 1 to 5} |
|userId (OPTIONAL)| {Corresponding UserId}|
|movieId (REQUIRED)| {Corresponding MovieId}|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Predictions endpoint: Returns all predictions in database
### Method: GET
>```
>/predictions
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Ratings endpoint: Returns all past user ratings
### Method: GET
>```
>/ratings
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## New ratings endpoint: Returns all new user ratings
### Method: GET
>```
>/ratings/new
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


## :clipboard:  [Dashboard](https://deep-film-dashboard.herokuapp.com/)

The implementation of Deep Film is hosted on a Streamlit dashboard.

Click on the header above to visit dashboard.

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