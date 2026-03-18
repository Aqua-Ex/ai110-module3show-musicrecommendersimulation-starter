"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, Recommender, UserProfile


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user = UserProfile(favorite_genre="pop", favorite_mood="happy", target_energy=0.8, likes_acoustic=False)

    recommender = Recommender(songs)
    recommendations = recommender.recommend(user, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        explanation = recommender.explain_recommendation(user, rec)
        print(f"{rec.title} - {rec.artist}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
