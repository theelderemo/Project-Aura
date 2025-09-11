# components/attunement_engine.py

import datetime
import json
import os

class AttunementEngine:
    def __init__(self, memory_filepath="memory.json"):
        self.memory_filepath = memory_filepath
        self._episodic_stream = []
        self._load_memory()
        print("[AttunementEngine]: Initialized.")

    def _load_memory(self):
        if os.path.exists(self.memory_filepath):
            try:
                with open(self.memory_filepath, 'r', encoding='utf-8') as f:
                    self._episodic_stream = json.load(f)
                print(f"[AttunementEngine]: Loaded {len(self._episodic_stream)} memories from '{self.memory_filepath}'.")
            except (json.JSONDecodeError, IOError) as e:
                print(f"[AttunementEngine]: Error loading memory file: {e}. Starting fresh.")
                self._episodic_stream = []
        else:
            print(f"[AttunementEngine]: No memory file found. Starting with a blank slate.")

    def _save_memory(self):
        try:
            with open(self.memory_filepath, 'w', encoding='utf-8') as f:
                json.dump(self._episodic_stream, f, indent=4, default=str)
        except IOError as e:
            print(f"[AttunementEngine]: CRITICAL ERROR - Could not save memory: {e}")

    def log_experience(self, user_input, aura_response, valence_snapshot):
        memory_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_input": user_input,
            "aura_response": aura_response,
            "valence_at_time": valence_snapshot
        }
        self._episodic_stream.append(memory_entry)
        self._save_memory()
        print(f"[AttunementEngine]: Experience logged and memory saved. Total memories: {len(self._episodic_stream)}")

    def retrieve_all_memories(self):
        """Returns the entire episodic stream."""
        return self._episodic_stream

    def retrieve_recent_memories(self, count=5):
        return self._episodic_stream[-count:]

    def reflect_and_consolidate(self):
        print("[AttunementEngine]: Entering reflection state... (consolidation logic to be implemented)")
        pass
