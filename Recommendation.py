import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies = pd.DataFrame({
    'title': [
        'The Matrix', 'John Wick', 'Titanic', 'The Notebook',
        'Avengers', 'Frozen', 'Interstellar', 'Toy Story',
        'Inception', 'The Godfather', 'Shrek', 'Gladiator'
    ],
    'genres': [
        'Action Sci-Fi', 'Action Thriller', 'Romance Drama', 'Romance Drama',
        'Action Sci-Fi', 'Animation Family', 'Sci-Fi Drama', 'Animation Comedy',
        'Sci-Fi Thriller', 'Crime Drama', 'Animation Comedy', 'Action Thriller'
    ]
})

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title'])

def recommend_movies(title, num_recommendations=5):
    if title not in indices:
        return f"Movie '{title}' not found. Please check the spelling or list available movies."

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

def show_menu():
    while True:
        print("\n Movie Recommendation System")
        print("1. Get Recommendations by Movie Title")
        print("2. Show All Available Movies")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            movie_name = input("Enter a movie title: ")
            num = input("How many recommendations do you want? (default 5): ")
            num = int(num) if num.isdigit() else 5

            recommendations = recommend_movies(movie_name, num)
            print("\n Recommendations:")
            if isinstance(recommendations, list):
                for movie in recommendations:
                    print(f"- {movie}")
            else:
                print(recommendations)

        elif choice == '2':
            print("\n Available Movies:")
            for title in sorted(movies['title'].tolist()):
                print(f"- {title}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print(" Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    show_menu()
