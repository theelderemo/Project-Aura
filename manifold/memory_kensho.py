# manifold/memory_kensho.py

from .kensho import Kensho
import config

class MemoryKensho(Kensho):
    """
    Searches the agent's memory (Episodic Stream) for connections to concepts.
    It generates valence based on the emotional context of past experiences.
    """
    def __init__(self):
        super().__init__(name="Memory-Kensho")

    def process(self, text_input: str, current_valence: dict, episodic_memories: list = None, concepts: list = None) -> dict:
        """
        If concepts are provided, search memories for them. If a concept is found
        in a memory with a strong emotional charge, generate a corresponding
        salience vector.
        """
        if not concepts or not episodic_memories:
            return {}

        print(f"[{self.name}]: Searching memory for {len(concepts)} concepts...")
        total_pleasure_impact = 0
        total_arousal_impact = 0
        memories_found = 0

        # Limit search to the 50 most recent memories for efficiency
        searchable_memories = episodic_memories[-50:]

        for concept in concepts:
            for memory in searchable_memories:
                if concept in memory.get("user_input", "").lower():
                    valence_at_time = memory.get("valence_at_time", {})
                    pleasure = valence_at_time.get("pleasure", 0)

                    # A memory is salient if it had a strong emotional charge
                    if abs(pleasure) >= config.RESPONSE_THRESHOLDS["high_pleasure"]:
                        total_pleasure_impact += pleasure
                        total_arousal_impact += abs(pleasure) * 0.5 
                        memories_found += 1
                        # Once a concept triggers a memory, we don't need to check it again
                        break 

        if memories_found > 0:
            avg_pleasure = (total_pleasure_impact / memories_found) * config.KENSHO_IMPACT_WEIGHTS.get("memory", 0.5)
            avg_arousal = (total_arousal_impact / memories_found) * config.KENSHO_IMPACT_WEIGHTS.get("memory", 0.5)
            
            print(f"[{self.name}]: Found {memories_found} salient memories. Impact: Pleasure {avg_pleasure:.2f}, Arousal {avg_arousal:.2f}")
            return {"pleasure": avg_pleasure, "arousal": avg_arousal}

        return {}
