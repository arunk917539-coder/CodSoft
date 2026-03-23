import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

movies = ["Avengers", "Batman", "Superman", "Spiderman", "Ironman"]

ratings = np.array([
[5,4,0,0,3],
[4,0,0,2,3],
[0,0,5,4,0],
[3,3,4,0,0]
])

similarity = cosine_similarity(ratings)

user = 0

recommended = np.argsort(similarity[user])[-2]

print("Recommended Movie:", movies[recommended])