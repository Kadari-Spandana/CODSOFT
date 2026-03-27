# ----------------------------------
# SIMPLE RECOMMENDATION SYSTEM
# (Collaborative Filtering - Pure Python)
# ----------------------------------

# Ratings Data
# 0 means the movie is not rated by the user
ratings = {
    "User1": {"Movie_A": 5, "Movie_B": 4, "Movie_C": 0, "Movie_D": 0, "Movie_E": 3},
    "User2": {"Movie_A": 4, "Movie_B": 0, "Movie_C": 0, "Movie_D": 3, "Movie_E": 0},
    "User3": {"Movie_A": 0, "Movie_B": 0, "Movie_C": 5, "Movie_D": 4, "Movie_E": 0},
    "User4": {"Movie_A": 0, "Movie_B": 2, "Movie_C": 4, "Movie_D": 0, "Movie_E": 5},
    "User5": {"Movie_A": 3, "Movie_B": 3, "Movie_C": 0, "Movie_D": 0, "Movie_E": 4},
}

# ----------------------------------
# Function to calculate similarity
# ----------------------------------

def calculate_similarity(user1, user2):
    common_movies = []

    # Find commonly rated movies
    for movie in ratings[user1]:
        if ratings[user1][movie] != 0 and ratings[user2][movie] != 0:
            common_movies.append(movie)

    # If no common movies, similarity is 0
    if len(common_movies) == 0:
        return 0

    score = 0

    # Calculate similarity score
    for movie in common_movies:
        difference = abs(ratings[user1][movie] - ratings[user2][movie])
        score += (5 - difference) / 5  # Normalize similarity

    return score / len(common_movies)


# ----------------------------------
# Recommendation Function
# ----------------------------------

def recommend_movies(user_name):
    scores = {}

    for other_user in ratings:
        if other_user != user_name:
            similarity = calculate_similarity(user_name, other_user)

            for movie in ratings[other_user]:
                if ratings[user_name][movie] == 0 and ratings[other_user][movie] > 0:
                    if movie not in scores:
                        scores[movie] = 0
                    scores[movie] += similarity * ratings[other_user][movie]

    # Sort movies by highest recommendation score
    recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return recommended


# ----------------------------------
# MAIN PROGRAM
# ----------------------------------

print("---- Movie Recommendation System ----\n")

user = input("Enter user name (User1 - User5): ")

if user in ratings:
    recommendations = recommend_movies(user)

    if recommendations:
        print("\nRecommended Movies for", user)
        print("-----------------------------------")
        for movie, score in recommendations:
            print(movie, " (Score:", round(score, 2), ")")
    else:
        print("No recommendations available.")
else:
    print("User not found.")