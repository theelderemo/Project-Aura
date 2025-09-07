INITIAL_VALENCE = {
    "pleasure": 0.0,  # The pleasure/displeasure dimension
    "arousal": 0.0,   # The arousal/calm dimension
    "dominance": 0.0, # A sense of control/helplessness (for future use)
}

VALENCE_DECAY_FACTOR = 0.9  # How quickly valence returns to neutral (0.8 = faster, 0.95 = slower)
VALENCE_CLAMP_MIN = -5.0    # The minimum value for any valence dimension
VALENCE_CLAMP_MAX = 5.0     # The maximum value for any valence dimension

# --- Response Thresholds ---
# These thresholds determine which response is chosen based on the Valence Core's state.
RESPONSE_THRESHOLDS = {
    "high_pleasure_arousal": 2.0, # Threshold for feeling "engaged" or "excited"
    "high_pleasure": 1.5,         # Threshold for feeling "positive" or "content"
    "low_pleasure_arousal": -2.0, # Threshold for feeling "unsettled" or "anxious"
    "low_pleasure": -1.5,         # Threshold for feeling "negative" or "concerned"
}

# --- Manifold Settings ---
# Weights for different Kensho units to influence their impact on valence.
# This allows you to define how much each "sense" contributes to the overall feeling.
KENSHO_IMPACT_WEIGHTS = {
    "syntax": 0.1,    # The base impact of sentence complexity
    "sentiment": 1.0, # The base impact of emotional words
}
