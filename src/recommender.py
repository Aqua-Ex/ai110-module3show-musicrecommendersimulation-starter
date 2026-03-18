from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return top k songs matching user preferences based on genre, mood, and energy."""
        scored_songs = []
        for song in self.songs:
            # Categorical score (0-1)
            # Genre importance halved (0.5x), mood remains 1x: (0.5*genre + mood)/1.5
            genre_match = 1.0 if song.genre == user.favorite_genre else 0.0
            mood_match = 1.0 if song.mood == user.favorite_mood else 0.0
            categorical_score = (0.5 * genre_match + mood_match) / 1.5

            # Audio score (0-1), focusing on energy
            audio_score = 1.0 - abs(user.target_energy - song.energy)

            # Total score (weighted average)
            # w_categorical = 0.25 (halved), w_audio = 0.75 (doubled)
            total_score = 0.25 * categorical_score + 0.75 * audio_score

            scored_songs.append((song, total_score))

        # Sort by score descending
        scored_songs.sort(key=lambda x: x[1], reverse=True)

        # Return top k songs
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate a human-readable explanation for why a song is recommended."""
        explanation_parts = []
        if song.genre == user.favorite_genre:
            explanation_parts.append(f"matches your preferred genre '{user.favorite_genre}'")
        if song.mood == user.favorite_mood:
            explanation_parts.append(f"matches your preferred mood '{user.favorite_mood}'")
        energy_diff = abs(user.target_energy - song.energy)
        if energy_diff < 0.1:
            explanation_parts.append(f"has energy level close to your preference ({song.energy:.1f} vs {user.target_energy:.1f})")
        elif energy_diff < 0.3:
            explanation_parts.append(f"has somewhat similar energy ({song.energy:.1f})")
        explanation = " and ".join(explanation_parts) if explanation_parts else "general match"
        return explanation

def load_songs(csv_path: str) -> List[Song]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = Song(
                id=int(row['id']),
                title=row['title'],
                artist=row['artist'],
                genre=row['genre'],
                mood=row['mood'],
                energy=float(row['energy']),
                tempo_bpm=float(row['tempo_bpm']),
                valence=float(row['valence']),
                danceability=float(row['danceability']),
                acousticness=float(row['acousticness'])
            )
            songs.append(song)
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        # Categorical score (0-1)
        genre_match = 1.0 if song['genre'] == user_prefs.get('genre') else 0.0
        mood_match = 1.0 if song['mood'] == user_prefs.get('mood') else 0.0
        categorical_score = (genre_match + mood_match) / 2.0

        # Audio score (0-1), focusing on energy
        user_energy = user_prefs.get('energy', 0.5)
        audio_score = 1.0 - abs(user_energy - song['energy'])

        # Total score (weighted average)
        total_score = 0.5 * categorical_score + 0.5 * audio_score

        # Explanation
        explanation_parts = []
        if genre_match:
            explanation_parts.append(f"matches your preferred genre '{user_prefs['genre']}'")
        if mood_match:
            explanation_parts.append(f"matches your preferred mood '{user_prefs['mood']}'")
        if audio_score > 0.8:
            explanation_parts.append(f"has energy level close to your preference ({song['energy']:.1f} vs {user_energy:.1f})")
        elif audio_score > 0.5:
            explanation_parts.append(f"has somewhat similar energy ({song['energy']:.1f})")
        explanation = " and ".join(explanation_parts) if explanation_parts else "general match"

        scored_songs.append((song, total_score, explanation))

    # Sort by score descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)

    # Return top k
    return scored_songs[:k]
