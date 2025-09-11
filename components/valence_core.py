import config

class ValenceCore:
    """
    Manages the multi-dimensional emotional state of the AURA instance.
    This moves beyond a single variable to a richer, more nuanced emotional model.
    """
    def __init__(self):
        # Initialize the valence state from the configuration file.
        self.state = config.INITIAL_VALENCE.copy()
        print("[ValenceCore]: Initialized.")

    def update_valence(self, salience_vector):
        """
        Updates the valence state based on a salience vector from the Manifold.
        A salience vector is a dictionary mapping valence dimensions to a score.
        Example: {'pleasure': 1.5, 'arousal': 0.5}
        """
        for dimension, value in salience_vector.items():
            if dimension in self.state:
                self.state[dimension] += value

        # Clamp the values to stay within a reasonable emotional range.
        self._clamp_state()
        print(f"[ValenceCore]: State updated to {self.get_state_str()}")

    def apply_decay(self):
        """
        Applies a decay factor to the valence, causing emotions to naturally
        return to a neutral state over time. This simulates emotional regulation.
        """
        for dimension in self.state:
            self.state[dimension] *= config.VALENCE_DECAY_FACTOR
        print(f"[ValenceCore]: Decay applied. State is now {self.get_state_str()}")

    def _clamp_state(self):
        """A private method to ensure valence dimensions don't go out of bounds."""
        for dimension, value in self.state.items():
            self.state[dimension] = max(config.VALENCE_CLAMP_MIN, min(config.VALENCE_CLAMP_MAX, value))

    def get_state(self):
        """Returns the current emotional state as a dictionary."""
        return self.state

    def get_state_str(self):
        """Returns a formatted string of the current emotional state for logging."""
        return ", ".join([f"{dim}: {val:.2f}" for dim, val in self.state.items()])

