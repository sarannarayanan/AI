import streamlit as st
import datetime
import os

def get_scent_suggestion(mood):
    scent_suggestions = {
        "happy": "Lemon – Bright and refreshing 🍋",
        "sad": "Lavender – Calming and soothing 🌸",
        "stressed": "Peppermint – Refreshing and energizing 🌿",
        "tired": "Eucalyptus – Awakens the senses 🌱",
        "bored": "Jasmine – Uplifts and inspires 🌼",
        "anxious": "Rose – Comforting and balancing 🌹",
        "confused": "Sandalwood – Grounds and centers 🌳"
    }
    return scent_suggestions.get(mood.lower(), "Sorry, we don't have a suggestion for that mood yet!")

def main():
    st.title("🌿✨ Aromatherapy Mood Matcher ✨🌿")
    st.write("Let's find the perfect scent to match your mood!")

    questions = [
        "Do you feel energized and ready to take on new challenges?",              # happy
        "Have you experienced a drop in your enthusiasm or interest lately?",      # sad
        "Are you finding it difficult to manage your daily responsibilities?",       # stressed
        "Do you feel physically or mentally drained?",                              # tired
        "Have you been feeling a lack of inspiration or creativity?",               # bored
        "Do you often feel uneasy or on edge?",                                     # anxious
        "Are you struggling to make sense of a situation or decision?"              # confused
    ]
    
    responses = []
    for question in questions:
        response = st.radio(question, ("Yes", "No"), key=question, index=None)
        responses.append(response)

    # Initialize mood scores
    mood_scores = {
        "happy": 0,
        "sad": 0,
        "stressed": 0,
        "tired": 0,
        "bored": 0,
        "anxious": 0,
        "confused": 0
    }

    # Update mood scores based on responses
    if responses[0] == "Yes":
        mood_scores["happy"] += 1
    if responses[1] == "Yes":
        mood_scores["sad"] += 1
    if responses[2] == "Yes":
        mood_scores["stressed"] += 1
    if responses[3] == "Yes":
        mood_scores["tired"] += 1
    if responses[4] == "Yes":
        mood_scores["bored"] += 1
    if responses[5] == "Yes":
        mood_scores["anxious"] += 1
    if responses[6] == "Yes":
        mood_scores["confused"] += 1

    if st.button("Get Scent Suggestion"):
        # Determine the mood with the highest score
        max_score = max(mood_scores.values())
        top_moods = [mood for mood, score in mood_scores.items() if score == max_score]

        # Tie-breaking logic: prioritize specific moods
        if len(top_moods) > 1:
            # Prioritize happy > stressed > anxious > confused > sad > bored
            priority_order = ["happy", "stressed", "anxious", "confused", "sad", "bored"]
            for mood in priority_order:
                if mood in top_moods:
                    mood = mood
                    break
        else:
            mood = top_moods[0]

        suggestion = get_scent_suggestion(mood)
        
        st.write("🌸 Your Aromatherapy Suggestion 🌸")
        st.write("--------------------------------")
        st.write(f"Mood: {mood.capitalize()}")
        st.write(f"Scent: {suggestion}\n\n")
        st.write("--------------------------------")

        st.write("💡 Disclaimer:")
        st.write("The aromatherapy used for influencing mental health, emotions, uplifting mood, and reducing stress is an alternative and complementary therapy. It cannot be used to treat chronic or acute diseases, allergies, or medical conditions.")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"🕒 Suggestion generated on: {current_time}\n")

        with open("aromatherapy_log.txt", "a", encoding="utf-8") as file:
            file.write(f"\nTime: {current_time}\n")
            file.write(f"Mood: {mood.capitalize()}\n")
            file.write(f"Scent: {suggestion}\n")
            file.write("Disclaimer: The aromatherapy used for influencing mental health, emotions, uplifting mood, and reducing stress is an alternative and complementary therapy. It is not a cure for chronic or acute diseases, allergies, or medical conditions.\n")
            file.write("-" * 60 + "\n")

def respond():
    satisfaction = st.radio("Did you like the suggestion?", ("Yes", "No"), index=None)
    if satisfaction == "No":
        st.write("🌟 Let's upgrade your experience! Try combining your scent with meditation, soft music, or a gratitude journal for extra positivity 💖")
    elif satisfaction == "Yes":
        st.write("We are glad that we found the perfect scent to elevate your mood! Have a 💖")

if __name__ == "__main__":
    main()
    if os.name == "nt":
        _ = os.system('cls')
    respond()