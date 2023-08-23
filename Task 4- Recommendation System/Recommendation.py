import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item ratings data (user, item, rating)
data = {'user': [1, 1, 1, 2, 2, 3, 3, 3],
        'item': ['A', 'B', 'C', 'A', 'B', 'B', 'C', 'D'],
        'rating': [5, 4, 4, 5, 3, 4, 2, 1]}

ratings_df = pd.DataFrame(data)

# Create a user-item matrix
user_item_matrix = ratings_df.pivot(index='user', columns='item', values='rating').fillna(0)

# Calculate cosine similarity between items
item_similarity = cosine_similarity(user_item_matrix.T)

# Function to recommend items to a user
def recommend_items(user_id, user_item_matrix, item_similarity, num_recommendations=3):
    user_ratings = user_item_matrix.loc[user_id]
    
    # Find unrated items
    unrated_items = user_ratings[user_ratings == 0].index
    
    # Calculate item scores for unrated items
    item_scores = np.dot(item_similarity, user_ratings)
    
    # Recommend top items
    recommendations = pd.Series(item_scores, index=user_item_matrix.columns)[unrated_items].nlargest(num_recommendations)
    return recommendations

# Get recommendations for a user
user_id = int(input("Enter user name (from 1 to 3): "))
recommended_items = recommend_items(user_id, user_item_matrix, item_similarity)

print("Recommended items for user", user_id)
print(recommended_items)