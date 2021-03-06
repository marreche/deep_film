import pandas as pd

from support.df_creation_streamlit import df_user, df_movies, last_user

from surprise import SVD, SVDpp, NMF
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split

from collections import defaultdict


##Prepare data for different model use
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df_user, reader)
trainset, testset = train_test_split(data, test_size = .25)



def get_top_n(predictions, userId, df_movies, df_user, n=20):
    '''
    Calculates predictions based on latest user ratings.
    Returns two DataFrames:
    - rated_user = ratings user has submitted.
    - pred_user = Predictions calculated using SVD, based on ratings user has submitted.
    '''
 
    ## Map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    ## Sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    
    ## Df with predictions. 
    preds_df = pd.DataFrame([(id, pair[0],pair[1]) for id, row in top_n.items() for pair in row],
                        columns=["userId" ,"movieId","rating_prediction"])
    
    
    ## Return pred_usr, i.e. top N recommended movies with (merged) titles and genres. 
    pred_user = preds_df[preds_df["userId"] == (userId)].merge(df_movies, how = 'left', left_on = 'movieId', right_on = 'movieId')
            
    ## Return hist_usr, returns already rated movies by user.
    rated_user = df_user[df_user.userId == (userId) ].sort_values("rating", ascending = False).merge\
    (df_movies, how = 'left', left_on = 'movieId', right_on = 'movieId')
    
    return rated_user, pred_user



def svd_prediction():
    '''
    Returns dataframe with top 10 predictions based on user preferences calculated with an SVD algorithm.
    '''
    
    algo_SVD = SVD()
    algo_SVD.fit(trainset)

    # Predict ratings for all pairs (i,j) that are NOT in the training set.
    testset = trainset.build_anti_testset()

    predictions_svd = algo_SVD.test(testset)

    hist_svd, pred_svd = get_top_n(predictions_svd, last_user, df_movies, df_user)
    pred_svd = pred_svd.dropna().reset_index().drop(columns=['genres', 'index'])
    
    return pred_svd[:10]



def svdpp_prediction():
    '''
    Returns dataframe with top 10 predictions based on user preferences calculated with an SVD++ algorithm.
    '''
    
    algo_svdpp = SVDpp()
    algo_svdpp.fit(trainset)

    # Predict ratings for all pairs (u, i) that are NOT in the training set.
    testset = trainset.build_anti_testset()
    predictions_svdpp = algo_svdpp.test(testset)
    
    hist_svdpp, pred_svdpp = get_top_n(predictions_svdpp, last_user, df_movies, df_user)
    pred_svdpp = pred_svdpp.dropna().reset_index().drop(columns=['userId', 'genres', 'index'])
    
    return pred_svdpp[:10]



def nmf_prediction():
    '''
    Returns dataframe with top 10 predictions based on user preferences calculated with an NMF algorithm.
    '''
    
    algo_NMF = NMF()
    algo_NMF.fit(trainset)


    # Predict ratings for all pairs (u, i) that are NOT in the training set.
    testset = trainset.build_anti_testset()
    predictions_nmf = algo_NMF.test(testset)
    
    hist_nmf, pred_nmf = get_top_n(predictions_nmf, last_user, df_movies, df_user)
    pred_nmf = pred_nmf.dropna().reset_index().drop(columns=['genres', 'index'])
    
    return pred_nmf[:10]


