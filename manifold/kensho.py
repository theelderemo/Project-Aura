from abc import ABC, abstractmethod

class Kensho(ABC):
    """
    An abstract base class for a Kensho unit.
    Each Kensho is a specialized, non-conscious process that observes input
    and generates a salience vector (a dictionary of its findings).
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def process(self, text_input: str, current_valence: dict) -> dict:
        """
        The core method of any Kensho. It takes the user input and the agent's
        current emotional state, and returns a salience vector.
        
        A salience vector is a dictionary that maps a valence dimension to a score.
        Example: {'pleasure': 1.0, 'arousal': 0.2}
        
        An empty dictionary should be returned if the Kensho finds nothing of note.
        """
        pass

