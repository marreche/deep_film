from support.mongo_connection import ratings
from surprise import SVD
from surprise import Dataset, Reader
from surprise.model_selection import cross_validate, train_test_split
from collections import defaultdict
import pandas as pd

##Create dataframe from JSON.

ratings_df = pd.DataFrame(list(ratings.find()))
ratings_df = ratings_df.drop(columns=['_id', 'timestamp'])

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings_df, reader)
trainset, testset = train_test_split(data, test_size = .25)
model = SVD(n_factors=100)
model.fit(trainset)
predictions = model.test(testset)

def get_top_n(predictions, n=10):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

top_n = get_top_n(predictions)

userId = []
movieId = []
for uid, user_ratings in top_n.items():
    userId.append(uid)
    movieId.append([iid for (iid, _) in user_ratings])

predictions_df = pd.DataFrame({
    'userId': userId,
    'movieId': movieId
},
    columns = ['userId', 'movieId']
)
