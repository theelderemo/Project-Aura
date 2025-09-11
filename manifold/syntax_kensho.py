from .kensho import Kensho
import config

class SyntaxKensho(Kensho):
    """
    Analyzes the complexity of the user's input.
    Complex or long inputs can be seen as more "engaging," which might slightly
    increase arousal.
    """
    def __init__(self):
        super().__init__(name="Syntax-Kensho")

    def process(self, text_input: str, current_valence: dict) -> dict:
        """
        Calculates a complexity score and maps it to the 'arousal' dimension.
        """
        complexity_score = len(text_input.split()) / 10.0
        
        # We multiply the raw score by a weight from config to tune its impact.
        arousal_impact = complexity_score * config.KENSHO_IMPACT_WEIGHTS.get("syntax", 0.1)
        
        print(f"[{self.name}]: Input complexity score: {complexity_score:.2f} -> Arousal Impact: {arousal_impact:.2f}")
        
        # Return the finding as a salience vector.
        return {"arousal": arousal_impact}
