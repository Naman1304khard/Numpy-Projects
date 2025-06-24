# NumPy Project Idea: Movie Rating Analytics

import numpy as np
import matplotlib.pyplot as plt

# Parameter
num_user = 100
num_movies = 10

# generating random rating brtween 1 and 5
np.random.seed(42)
rating = np.random.randint(1,6,size=(num_user,num_movies))

print("Rating matrix:\n", rating)

# Average rating per movie
avg_movie_rating = np.mean(rating, axis=0)
print("\nAverage rating per movie :\n", avg_movie_rating)

#movie with highest average rating 
top_movie = np.argmax(avg_movie_rating)
print(f"\nMost loved movie is Movie {top_movie} with avg rating {avg_movie_rating[top_movie]:.2f}")


# Movie with most 5-star rating
five_star_count = np.sum(rating == 5, axis=0)
most_five_stars = np.argmax(five_star_count)
print(f"\nMovie {most_five_stars} has the most 5-star rating: {five_star_count[most_five_stars]}")

#Visualization
plt.figure(figsize=(8, 5))
plt.bar(range(num_movies), avg_movie_rating, color='skyblue')
plt.xlabel('Movie ID')
plt.ylabel('Average Rating')
plt.title('Average Rating per Movie')
plt.show()