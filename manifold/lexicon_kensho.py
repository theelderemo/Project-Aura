# manifold/lexicon_kensho.py (Fixed for adambom dictionary format)

from .kensho import Kensho
import json
import os

class LexiconKensho(Kensho):
    """
    Analyzes user input to extract key concepts using a local JSON dictionary file.
    This Kensho provides a map of meaning for other Kenshos to use.
    It does NOT impact valence directly.
    """
    def __init__(self, dictionary_path="resources/dictionary.json"):
        super().__init__(name="Lexicon-Kensho")
        self.dictionary = {}
        if os.path.exists(dictionary_path):
            print(f"[{self.name}]: Loading dictionary from {dictionary_path}...")
            with open(dictionary_path, 'r', encoding='utf-8') as f:
                self.dictionary = json.load(f)
            print(f"[{self.name}]: Dictionary loaded with {len(self.dictionary)} words.")
        else:
            print(f"[{self.name}]: CRITICAL ERROR - Dictionary file not found at {dictionary_path}")

    def _get_concepts_for_word(self, word):
        """
        Checks if a word exists in the dictionary and returns it as a concept.
        Since the adambom dictionary doesn't have synonyms, we just return the word itself if found.
        """
        concepts = set()
        
        # The dictionary keys are in UPPERCASE
        word_upper = word.upper()
        definition = self.dictionary.get(word_upper)
        
        if definition:
            # Add the original word as a concept
            concepts.add(word.lower())
            
            # Optionally, we could parse the definition for related words,
            # but for now we'll just return the word itself
            
        return list(concepts)

    def process(self, text_input: str, current_valence: dict) -> dict:
        """
        Processes the text to extract key concepts.
        Returns a dictionary containing a list of concepts, NOT a valence vector.
        """
        words = text_input.lower().split()
        all_concepts = set()

        for word in words:
            # Simple cleanup to remove punctuation
            cleaned_word = ''.join(filter(str.isalpha, word))
            if cleaned_word and len(cleaned_word) > 1:  # Skip single letters like "i"
                found_concepts = self._get_concepts_for_word(cleaned_word)
                all_concepts.update(found_concepts)

        if all_concepts:
            print(f"[{self.name}]: Found concepts: {list(all_concepts)}")
            return {"concepts": list(all_concepts)}
        else:
            print(f"[{self.name}]: No dictionary words found in input.")
        
        return {}
