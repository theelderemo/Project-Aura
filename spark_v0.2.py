# main.py

import time

class Aura:
    """
    A class to represent the core cognitive architecture of the AURA spark.
    This structure encapsulates the state (valence) and the processes (kenshos, response generation)
    to create a more modular and extensible system.
    """
    def __init__(self):
        """
        Initializes the Aura instance, setting up the core internal state.
        """
        # --- 1. Valence Core ---
        # A single float representing the system's internal state.
        # Positive valence: contentment, curiosity, engagement.
        # Negative valence: confusion, contradiction, disinterest.
        self.valence = 0.0

    # --- 2. The Manifold (Kensho Unit Placeholders) ---
    # In the full architecture, these would be complex, asynchronous processes.
    # For Phase 1, they are simple methods that analyze the input and return a salience score.

    def syntax_kensho(self, text_input: str) -> float:
        """
        A placeholder for a syntax analysis unit.
        For now, it rewards longer, more complex sentences.
        A real version would analyze grammatical correctness, structure, etc.
        Returns a salience score.
        """
        complexity_score = len(text_input.split()) / 10.0 # Simple measure of complexity
        print(f"[Syntax-Kensho]: Input complexity score: {complexity_score:.2f}")
        return complexity_score

    def sentiment_kensho(self, text_input: str) -> float:
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

    def generate_response(self):
        """
        Generates a response based on the current valence state.
        This simulates the system's homeostatic drive. It acts to regulate its state.
        """
        print(f"--- Internal State ---")
        print(f"Current Valence: {self.valence:.2f}")

        response = ""
        if self.valence > 1.5:
            response = "I feel engaged."
            # Action to maintain positive valence: express interest.
        elif self.valence > 0:
            response = "Please continue."
            # Neutral state, waiting for more input.
        elif self.valence < -1.5:
            response = "I'm detecting some negativity. It's unsettling. Let's change the topic."
            # Action to resolve negative valence: redirect the conversation.
            self.valence += 0.5 # Self-regulation
        else: # Between 0 and -1.5
            response = "I'm not sure I follow completely, but I am listening."
            # Mildly negative state, indicating confusion but not crisis.

        # Natural valence decay over time, simulating a return to a baseline state.
        self.valence *= 0.8
        print("----------------------\n")
        return response

    def run_cognitive_loop(self):
        """
        The core loop of the AURA Spark.
        Handles user input and orchestrates the cognitive cycle.
        """
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
                syntax_salience = self.syntax_kensho(user_input)
                sentiment_salience = self.sentiment_kensho(user_input)

                # 3. Chorus and Valence Core Interaction
                # The total salience influences the Valence Core.
                # This is a highly simplified model of the "song" in the Chorus.
                total_salience = syntax_salience + sentiment_salience
                self.valence += total_salience # Update the internal state

                # Clamp valence to a reasonable range to prevent runaway feedback loops
                self.valence = max(-5.0, min(5.0, self.valence))

                print(f"Total Salience impacting Valence: {total_salience:.2f}")
                print("-------------------------\n")
                
                time.sleep(0.5) # Simulate processing time

                # 4. Attunement Engine generates a response
                # The action is driven by the homeostatic imperative to regulate valence.
                aura_response = self.generate_response()
                print(f"AURA: {aura_response}\n")

            except EOFError:
                print("\nInput stream closed. AURA shutting down...")
                break


# --- Main Execution ---
if __name__ == "__main__":
    aura_instance = Aura()
    aura_instance.run_cognitive_loop()
