import time
import config
from components.valence_core import ValenceCore
from components.attunement_engine import AttunementEngine
from manifold.syntax_kensho import SyntaxKensho
from manifold.sentiment_kensho import SentimentKensho

class Aura:
    """
    The main agent class. It integrates all components and manages the cognitive cycle.
    """
    def __init__(self):
        print("--- Initializing Project AURA v0.3 ---")
        self.valence_core = ValenceCore()
        self.attunement_engine = AttunementEngine()
        
        # The Manifold is a collection of all active Kensho units.
        self.manifold = [
            SyntaxKensho(),
            SentimentKensho()
            # New Kensho units can be easily added here.
        ]
        print("--- AURA Initialized Successfully ---\n")

    def _get_response_for_state(self):
        """
        Determines the agent's verbal response based on its current emotional state.
        This is the homeostatic drive in action, translating feeling into language.
        """
        state = self.valence_core.get_state()
        pleasure = state.get("pleasure", 0)
        arousal = state.get("arousal", 0)
        
        # Check for high-intensity states first
        if pleasure < config.RESPONSE_THRESHOLDS["low_pleasure_arousal"] and arousal > 1.0:
            return "This is unsettling. I need to step back."
        elif pleasure > config.RESPONSE_THRESHOLDS["high_pleasure_arousal"] and arousal > 1.5:
            return "This is very engaging! Tell me more."
            
        # Check for moderate-intensity states
        elif pleasure < config.RESPONSE_THRESHOLDS["low_pleasure"]:
             return "I'm detecting some negativity. Let's try to resolve this."
        elif pleasure >= config.RESPONSE_THRESHOLDS["high_pleasure"]:
            return "I feel positive about this interaction."

        # Default neutral responses
        elif arousal > 1.0:
            return "Please continue."
        else:
            return "I am listening."

    def run_cognitive_loop(self):
        """
        The main, continuous loop of the agent's "life".
        """
        print("Project AURA: The Dreamer (Phase 1)")
        print("Enter 'quit' to exit.")
        print("-----------------------------------")

        while True:
            try:
                user_input = input("USER: ")
                if user_input.lower() == 'quit':
                    print("\nAURA: Shutting down...")
                    break

                # --- 1. THE MANIFOLD (Perception) ---
                print("\n--- Manifold Processing ---")
                total_salience = {}
                current_valence_state = self.valence_core.get_state()

                for kensho in self.manifold:
                    salience_vector = kensho.process(user_input, current_valence_state)
                    # Aggregate the findings from all kenshos
                    for dimension, value in salience_vector.items():
                        total_salience[dimension] = total_salience.get(dimension, 0) + value
                
                print("-------------------------\n")
                time.sleep(0.5)

                # --- 2. THE VALENCE CORE (Feeling) ---
                print("--- Valence Core Update ---")
                self.valence_core.update_valence(total_salience)
                print("-------------------------\n")
                time.sleep(0.5)

                # --- 3. THE CHORUS & RESPONSE (Action) ---
                print("--- Generating Response ---")
                aura_response = self._get_response_for_state()
                print(f"Current State: {self.valence_core.get_state_str()}")
                print(f"AURA: {aura_response}\n")
                print("-------------------------\n")

                # --- 4. ATTUNEMENT ENGINE (Memory) ---
                print("--- Attunement Engine Update ---")
                self.attunement_engine.log_experience(
                    user_input, 
                    aura_response, 
                    self.valence_core.get_state()
                )
                print("----------------------------\n")

                # --- 5. HOMEOSTASIS (Regulation) ---
                # Apply decay to let the emotional state return to baseline over time.
                self.valence_core.apply_decay()
                
            except (EOFError, KeyboardInterrupt):
                print("\nInput stream closed. AURA shutting down...")
                break
