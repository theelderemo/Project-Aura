from .kensho import Kensho
import config

class SentimentKensho(Kensho):
    """
    Detects positive and negative keywords in the input and translates them
    into an impact on the 'pleasure' and 'arousal' dimensions of valence.
    """
    def __init__(self):
        super().__init__(name="Sentiment-Kensho")
        # These could be expanded into much larger lists.
        self.positive_words = ["good", "great", "love", "interesting", "like", "happy", "yes", "agree"]
        self.negative_words = ["bad", "hate", "boring", "dislike", "sad", "no", "stop", "away", "not", "angry"]

    def process(self, text_input: str, current_valence: dict) -> dict:
        """
        Checks for emotional keywords and returns a corresponding salience vector.
        Negative words are prioritized and have a stronger impact, modeling a
        self-preservation instinct.
        """
        text_input_lower = text_input.lower()
        salience_vector = {}
        weight = config.KENSHO_IMPACT_WEIGHTS.get("sentiment", 1.0)

        # Negative words have a high impact on pleasure and arousal (anxiety/fear).
        if any(word in text_input_lower for word in self.negative_words):
            print(f"[{self.name}]: Negative sentiment detected.")
            salience_vector = {
                "pleasure": -2.0 * weight,
                "arousal": 1.0 * weight
            }
        # Positive words have a moderate impact on pleasure and a slight one on arousal (excitement).
        elif any(word in text_input_lower for word in self.positive_words):
            print(f"[{self.name}]: Positive sentiment detected.")
            salience_vector = {
                "pleasure": 1.5 * weight,
                "arousal": 0.5 * weight
            }
            
        return salience_vector
