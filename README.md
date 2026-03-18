# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

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

Real word systems account for more values than what we laid out but the UserProfile and final score calculations are close to how real-world recommendation systems work. Real world systems implement more AI into their systems and they implment more

-Behavior-based signals (what you actually play, skip, replay,search,etc)
-Collaborative signals(what other users like you enjoy)
-Engagement goals(keep you watching/listening longer)
Diversity(avoid repeating, explore new artists/genres)

### Algorithm Recipe: Hybrid Preference-Based Scoring

The finalized scoring logic balances categorical preferences for presonalized recommendations. The inputs include:

-User Prefrences(individual user prefrences for different categories)
-Song data(Genre,mood,energy,valence, catchiness and acousticness)
-Weights(Cofigurable weights for scoring components)

The Steps include:
-Load Data (We read all the songs from songs.csv into a list of songs objects)
-Compute Scores:
  .Categorical Score (Add score of 1 if genre matches, 0 otherwise. Similar logic for mood matching)
  .Audio Score (Similarity for the different weights e.g energy, valence, danceability, etc)
  .Artist Boost( +0.1 if song artist matches a user favorite)
  .Total Score (w_categorical * categorical_score) + (w_audio * audio_score) + artist_boost
-Rank Songs (Sort songs by total score)
-Select Top n(Return the top n songs as recommendations)

Example Output
For a user preferring "pop" genre, "happy" mood, energy=0.8, valence=0.8, danceability=0.8, acousticness=0.2:
-Song 1 (pop, happy, matching audio): High score (~0.9).
-Song 2 (lofi, chill, mismatched): Low score (~0.3).

Genre and mood matches might be over-priortized which means excellent songs with high audio score can be ignored by the system. It could also exhibit confirmation bias by reinforcing user preferences without introducing novelty, leading to echo chambers. The dataset can also be skewed towards popular genres since audio features assume linear prefrences.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

