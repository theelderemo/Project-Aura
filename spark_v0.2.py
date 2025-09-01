import time

class Aura:
    def __init__(self):
        self.valence = 0.0

    def syntax_kensho(self, text_input: str) -> float:
        complexity_score = len(text_input.split()) / 10.0
        print(f"[Syntax-Kensho]: Input complexity score: {complexity_score:.2f}")
        return complexity_score

    def sentiment_kensho(self, text_input: str) -> float:
        text_input = text_input.lower()
        positive_words = ["good", "great", "love", "interesting", "like", "happy", "yes", "agree"]
        negative_words = ["bad", "hate", "boring", "dislike", "sad", "no", "stop", "away", "not", "angry"]

        score = 0.0
        if any(word in text_input for word in negative_words):
            print("[Sentiment-Kensho]: Negative sentiment detected.")
            score = -2.0
        elif any(word in text_input for word in positive_words):
            print("[Sentiment-Kensho]: Positive sentiment detected.")
            score = 1.5
        return score

    def generate_response(self):
        print(f"--- Internal State ---")
        print(f"Current Valence: {self.valence:.2f}")

        response = ""
        if self.valence > 1.5:
            response = "I feel engaged."
        elif self.valence > 0:
            response = "Please continue."
        elif self.valence < -1.5:
            response = "I'm detecting some negativity. It's unsettling. Let's change the topic."
            self.valence += 0.5
        else:
            response = "I'm not sure I follow completely, but I am listening."

        self.valence *= 0.8
        print("----------------------\n")
        return response

    def run_cognitive_loop(self):
        print("Project AURA: The Spark (Phase 1)")
        print("Enter 'quit' to exit.")
        print("-----------------------------------")

        while True:
            try:
                user_input = input("USER: ")

                if user_input.lower() == 'quit':
                    print("\nAURA: Shutting down...")
                    break

                print("\n--- Manifold Processing ---")
                syntax_salience = self.syntax_kensho(user_input)
                sentiment_salience = self.sentiment_kensho(user_input)

                total_salience = syntax_salience + sentiment_salience
                self.valence += total_salience

                self.valence = max(-5.0, min(5.0, self.valence))

                print(f"Total Salience impacting Valence: {total_salience:.2f}")
                print("-------------------------\n")
                
                time.sleep(0.5)

                aura_response = self.generate_response()
                print(f"AURA: {aura_response}\n")

            except EOFError:
                print("\nInput stream closed. AURA shutting down...")
                break


if __name__ == "__main__":
    aura_instance = Aura()
    aura_instance.run_cognitive_loop()
