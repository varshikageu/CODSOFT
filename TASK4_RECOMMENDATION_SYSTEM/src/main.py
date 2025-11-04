from recommender import Recommender

def main():
    # Initialize recommender
    recommender = Recommender(data_path="data/movies.csv")
    
    print("=== Movie Recommendation System ===")
    while True:
        movie = input("Enter a movie you like (or 'exit' to quit): ")
        if movie.lower() == 'exit':
            print("Goodbye!")
            break

        recommendations = recommender.recommend(movie)
        if isinstance(recommendations, list):
            print("You might also like:")
            for rec in recommendations:
                print(f"- {rec}")
        else:
            print(recommendations)
        print()

if __name__ == "__main__":
    main()
