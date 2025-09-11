# aura_agent.py (Definitively Corrected)

import time
import config
from components.valence_core import ValenceCore
from components.attunement_engine import AttunementEngine
from manifold.syntax_kensho import SyntaxKensho
from manifold.sentiment_kensho import SentimentKensho
from manifold.lexicon_kensho import LexiconKensho
from manifold.memory_kensho import MemoryKensho

class Aura:
    """
    The main agent class. It integrates all components and manages the cognitive cycle.
    """
    def __init__(self):
        print("--- Initializing Project AURA v0.4 ---")
        self.valence_core = ValenceCore()
        self.attunement_engine = AttunementEngine()
        
        # The Manifold is a collection of all active Kensho units.
        # Order matters: Lexicon must run before Memory.
        self.manifold = [
            LexiconKensho(),
            MemoryKensho(),
            SyntaxKensho(),
            SentimentKensho()
        ]
        print("--- AURA Initialized Successfully ---\n")

    def _get_response_for_state(self):
        """
        Determines the agent's verbal response based on its current emotional state.
        """
        state = self.valence_core.get_state()
        pleasure = state.get("pleasure", 0)
        arousal = state.get("arousal", 0)
        
        if pleasure < config.RESPONSE_THRESHOLDS["low_pleasure_arousal"] and arousal > 1.0:
            return "This is unsettling. I need to step back."
        elif pleasure > config.RESPONSE_THRESHOLDS["high_pleasure_arousal"] and arousal > 1.5:
            return "This is very engaging! Tell me more."
        elif pleasure < config.RESPONSE_THRESHOLDS["low_pleasure"]:
             return "I'm detecting some negativity. Let's try to resolve this."
        elif pleasure >= config.RESPONSE_THRESHOLDS["high_pleasure"]:
            return "I feel positive about this interaction."
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
                processed_concepts = []

                for kensho in self.manifold:
                    if isinstance(kensho, LexiconKensho):
                        salience_packet = kensho.process(user_input, current_valence_state)
                        if "concepts" in salience_packet:
                            processed_concepts = salience_packet["concepts"]
                        # LexiconKensho doesn't contribute to valence directly, so salience_vector is empty
                        salience_vector = {}
                    elif isinstance(kensho, MemoryKensho):
                        salience_vector = kensho.process(
                            user_input, 
                            current_valence_state,
                            episodic_memories=self.attunement_engine.retrieve_all_memories(),
                            concepts=processed_concepts
                        )
                    else:
                        salience_vector = kensho.process(user_input, current_valence_state)
                    
                    # Add this kensho's contribution to the total salience
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
                self.valence_core.apply_decay()
                
            except (EOFError, KeyboardInterrupt):
                print("\nInput stream closed. AURA shutting down...")
                break
