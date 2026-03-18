# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MusicVibe Recommender v1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender is for classroom exploration so that I can understand how normal recommendation algorithms work. It generates song recommendations based on user preferences for genre, mood, energy level, and acoustic preference. The model assumes users have clear preferences that can be matched to song attributes.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

You can include a simple diagram or bullet list if helpful.

The way how my system is works is that songs are described by mainly *what it sounds like* and *how it feels*. The main categories for songs in this system are

-Genre (e.g pop, rap, rock, etc)
-Mood (happy, sad, chill, etc)
-Energy (The energy is described using a number from 0-1 that describes how intense/high energy it feels)
-Tempo (beats per minute)
-Valence(This is described using a number from 0-1 that tells us how positive the song feels)
-Catchniess(This is described using a number from 0-1 that tells us how catchy the song is)
Acousticness(This is described using a number from 0-1 for how 'acoustic' vs 'electronic' it sounds)

For the UserProfile we categorize this based on 3 main preferences that represent what the user is looking for in a song. 

-Preferred genre 
-Preferred mood 
-Preferred energy level
-Temp/valence/catchiness/acousticness can be implemented to the profile as well but the three categories above provide the main amount of context needed for the system.


My recommender computes scores by checking how closely the song matches the user profile. 
For things like energy, valence and catchiness, the system gives higher scores to songs that are closer to the user's preferred values ( e.g if users base value is 0.7 energy score, then a score of 0.72 is more likely to be used that a score of 0.9). 
If the genre of the song matches user's preferred generes then the score gets a bonus, the same happens for mood just at a lower weight/scale. We account for all these values and then compute a final score that determies if we should recommend the song or not.

Once songs have a score, we sort songs from the highest score to lowest. The top N songs then go on to bemoce the recommendations (the n songs closest to the users bases values/profile are recommended).

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset consists of 18 songs loaded from a CSV file. It includes a variety of genres (pop, rock, lofi, electronic, etc.), moods (happy, chill, energetic), energy levels (from 1-10), and acoustic preferences (true/false). The dataset is small and curated for this simulation, so it may not represent the full diversity of music available.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with strong preferences for energy levels, as the audio features (energy and acoustic) are heavily weighted. It provides reasonable recommendations for profiles that match common combinations like high-energy pop or chill lofi. The hybrid scoring captures the intuition that audio characteristics are more important than exact genre matches in many cases. For example, it correctly ranked high-energy songs for energetic users and low-energy songs for relaxed users.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system priortizes matching energy above the other weighted options. This creates a situation where high energy songs  dominate regardless of genre. The 'likes_acoustic' field is barely accounted for in scoring, which unrepresents users who like acoustic songs. Additionaly, since genre matching is simple yes or no (1 or 0s) genres that a similar don't get credit or scores for being similar to a genre in user's profile. This hurts the chances of niche genres based on popular ones to be recommended. 
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the recommender with three user profiles: a pop enthusiast who likes high-energy, happy music; a lofi fan who prefers chill, low-energy acoustic songs; and a rock lover who likes energetic rock. I looked at the top recommendations and their scores to see if they matched the profiles intuitively. The system performed well for the pop and lofi profiles but showed some bias towards high-energy songs even for the rock profile. I ran weight shift experiments, doubling the energy weight, which significantly changed rankings and confirmed the sensitivity to weights. I also ran unit tests to ensure the scoring logic worked correctly.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

To improve the model, I would add more song features like tempo, danceability, and valence. Implement diversity in recommendations to avoid filter bubbles. Use more sophisticated genre similarity (e.g., genre embeddings) instead of binary matching. Add user history and collaborative filtering. Create a better explanation system that shows why songs were recommended. Consider a web UI for easier testing.
---

## 9. Personal Reflection  

This project taught me how recommender systems can have hidden biases, especially through weighting decisions that seem minor but have big impacts. I was surprised by how changing weights from 0.5/0.5 to 0.25/0.75 drastically altered recommendations, creating energy-focused filter bubbles. It changed my view of music apps, making me more aware of how algorithms might limit exposure to new music by over-optimizing for certain features. Overall, it was a great introduction to the challenges of building fair and effective recommendation systems.  


