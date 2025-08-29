# main.py

import time

# --- 1. Valence Core ---
# A single variable representing the system's internal state.
# For this initial phase, it's a simple float.
# Positive valence might represent a state of contentment, curiosity, or engagement.
# Negative valence might represent confusion, contradiction, or disinterest.
valence = 0.0

# --- 2. The Manifold (Kensho Unit Placeholders) ---
# In the full architecture, these would be complex, asynchronous processes.
# For Phase 1, they are simple functions that analyze the input and return a salience score.

def syntax_kensho(text_input: str) -> float:
    """
    A placeholder for a syntax analysis unit.
    For now, it rewards longer, more complex sentences.
    A real version would analyze grammatical correctness, structure, etc.
    Returns a salience score.
    """
    complexity_score = len(text_input.split()) / 10.0 # Simple measure of complexity
    print(f"[Syntax-Kensho]: Input complexity score: {complexity_score:.2f}")
    return complexity_score

def sentiment_kensho(text_input: str) -> float:
    """
    A placeholder for a sentiment analysis unit.
    For now, it just checks for positive or negative keywords.
    A real version would use sophisticated sentiment analysis.
    Returns a salience score (can be negative).
    """
    text_input = text_input.lower()
    positive_words = ["good", "great", "love", "interesting", "like", "happy", "yes", "agree"]
    negative_words = ["bad", "hate", "boring", "dislike", "sad", "no", "stop", "away", "not", "angry"]

    score = 0.0
    # Prioritize detecting negative sentiment. If found, stop checking.
    if any(word in text_input for word in negative_words):
        print("[Sentiment-Kensho]: Negative sentiment detected.")
        score = -2.0
    elif any(word in text_input for word in positive_words):
        print("[Sentiment-Kensho]: Positive sentiment detected.")
        score = 1.5
    return score

# --- 3. The Chorus & Attunement Engine (Simplified Response Mechanism) ---
# This function synthesizes the Kensho outputs and the current valence
# to decide on a response.

def generate_response():
    """
    Generates a response based on the current valence state.
    This simulates the system's homeostatic drive. It acts to regulate its state.
    """
    global valence
    print(f"--- Internal State ---")
    print(f"Current Valence: {valence:.2f}")

    response = ""
    if valence > 1.5:
        response = "That's a very interesting point. I feel engaged."
        # Action to maintain positive valence: express interest.
    elif valence > 0:
        response = "Understood. Please continue."
        # Neutral state, waiting for more input.
    elif valence < -1.5:
        response = "I'm detecting some negativity. It's unsettling. Let's change the topic."
        # Action to resolve negative valence: redirect the conversation.
        valence += 0.5 # Self-regulation
    else: # Between 0 and -1.5
        response = "I'm not sure I follow completely, but I am listening."
        # Mildly negative state, indicating confusion but not crisis.

    # Natural valence decay over time, simulating a return to a baseline state.
    valence *= 0.8
    print("----------------------\n")
    return response

# --- Main Cognitive Loop ---
def main():
    """
    The core loop of the AURA Spark.
    Handles user input and orchestrates the cognitive cycle.
    """
    global valence
    print("Project AURA: The Spark (Phase 1)")
    print("Enter 'quit' to exit.")
    print("-----------------------------------")

    while True:
        try:
            # 1. Get external input (linguistic embodiment)
            user_input = input("USER: ")

            if user_input.lower() == 'quit':
                print("\nAURA: Shutting down...")
                break

            # 2. Manifold processes the input
            # Kensho Units generate broadcasts with salience scores.
            print("\n--- Manifold Processing ---")
            syntax_salience = syntax_kensho(user_input)
            sentiment_salience = sentiment_kensho(user_input)

            # 3. Chorus and Valence Core Interaction
            # The total salience influences the Valence Core.
            # This is a highly simplified model of the "song" in the Chorus.
            total_salience = syntax_salience + sentiment_salience
            valence += total_salience # Update the internal state

            # Clamp valence to a reasonable range to prevent runaway feedback loops
            valence = max(-5.0, min(5.0, valence))

            print(f"Total Salience impacting Valence: {total_salience:.2f}")
            print("-------------------------\n")
            
            time.sleep(0.5) # Simulate processing time

            # 4. Attunement Engine generates a response
            # The action is driven by the homeostatic imperative to regulate valence.
            aura_response = generate_response()
            print(f"AURA: {aura_response}\n")

        except EOFError:
            print("\nInput stream closed. AURA shutting down...")
            break


if __name__ == "__main__":
    main()



