import datetime
import json
import os

class AttunementEngine:
    """
    Manages the Episodic Stream (memory) and, in later phases, the Core Identity Matrix.
    It has the authority to log, retrieve, and eventually modify its own memories by
    reading from and writing to a permanent file.
    """
    def __init__(self, memory_filepath="memory.json"):
        self.memory_filepath = memory_filepath
        self._episodic_stream = []
        self._load_memory() # MODIFIED: Load memory on initialization.
        print("[AttunementEngine]: Initialized.")

    # --- NEW METHOD: Load memory from the file ---
    def _load_memory(self):
        """
        Loads the episodic stream from the JSON file.
        If the file doesn't exist, it starts with an empty memory.
        """
        if os.path.exists(self.memory_filepath):
            try:
                with open(self.memory_filepath, 'r') as f:
                    # The JSON stores datetime as strings, so we just load it as is for now.
                    self._episodic_stream = json.load(f)
                print(f"[AttunementEngine]: Loaded {len(self._episodic_stream)} memories from '{self.memory_filepath}'.")
            except (json.JSONDecodeError, IOError) as e:
                print(f"[AttunementEngine]: Error loading memory file: {e}. Starting fresh.")
                self._episodic_stream = []
        else:
            print(f"[AttunementEngine]: No memory file found. Starting with a blank slate.")

    # --- NEW METHOD: Save memory to the file ---
    def _save_memory(self):
        """
        Saves the entire episodic stream to the JSON file, overwriting it.
        This makes the current state of memory permanent.
        """
        try:
            with open(self.memory_filepath, 'w') as f:
                # We need a custom way to handle datetime objects for JSON serialization.
                json.dump(self._episodic_stream, f, indent=4, default=str)
        except IOError as e:
            print(f"[AttunementEngine]: CRITICAL ERROR - Could not save memory: {e}")

    def log_experience(self, user_input, aura_response, valence_snapshot):
        """
        Creates a new memory entry, adds it to the episodic stream, and immediately
        saves the updated stream to the permanent file.
        """
        memory_entry = {
            # Convert datetime to a standard string format for JSON
            "timestamp": datetime.datetime.now().isoformat(),
            "user_input": user_input,
            "aura_response": aura_response,
            "valence_at_time": valence_snapshot
        }
        self._episodic_stream.append(memory_entry)
        self._save_memory() # MODIFIED: Save after every new experience.
        print(f"[AttunementEngine]: Experience logged and memory saved. Total memories: {len(self._episodic_stream)}")

    def retrieve_recent_memories(self, count=5):
        return self._episodic_stream[-count:]

    def reflect_and_consolidate(self):
        print("[AttunementEngine]: Entering reflection state... (consolidation logic to be implemented)")
        # In the future, this method would:
        # 1. Run complex logic on the self._episodic_stream list.
        # 2. After modifying the list in memory, it would call self._save_memory()
        #    to make those modifications permanent.
        pass
