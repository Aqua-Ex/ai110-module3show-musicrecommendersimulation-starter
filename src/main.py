"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, Recommender, UserProfile


def test_profile(profile_name: str, user: UserProfile, recommender: Recommender, k: int = 5) -> None:
    """Test and display recommendations for a given user profile."""
    print(f"\n{'='*60}")
    print(f"Profile: {profile_name}")
    print(f"Preferences: Genre={user.favorite_genre}, Mood={user.favorite_mood}, Energy={user.target_energy}")
    print(f"{'='*60}\n")
    
    recommendations = recommender.recommend(user, k=k)
    
    print("Top recommendations:\n")
    for i, rec in enumerate(recommendations, 1):
        explanation = recommender.explain_recommendation(user, rec)
        print(f"{i}. {rec.title} - {rec.artist}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    recommender = Recommender(songs)
    
    # Define three distinct user preference profiles
    high_energy_pop = UserProfile(
        favorite_genre="pop", 
        favorite_mood="happy", 
        target_energy=0.85, 
        likes_acoustic=False
    )
    
    chill_lofi = UserProfile(
        favorite_genre="lofi", 
        favorite_mood="chill", 
        target_energy=0.4, 
        likes_acoustic=True
    )
    
    deep_intense_rock = UserProfile(
        favorite_genre="rock", 
        favorite_mood="intense", 
        target_energy=0.9, 
        likes_acoustic=False
    )
    
    # Test all profiles
    test_profile("High-Energy Pop", high_energy_pop, recommender)
    test_profile("Chill Lofi", chill_lofi, recommender)
    test_profile("Deep Intense Rock", deep_intense_rock, recommender)


if __name__ == "__main__":
    main()
