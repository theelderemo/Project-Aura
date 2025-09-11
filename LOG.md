# Project AURA: Experiment Log

This document is a **living log** of experiments, outcomes, bugs, and insights discovered during the development of Project AURA.

---
Project AURA: Experiment Log
This document is a living log of experiments, outcomes, bugs, and insights discovered during the development of Project AURA.

## Log Entry: 2025-08-29

**Experiment:** Initial test of the v0.1 Spark's homeostatic feedback loop with conflicting sentiment.  

**Phase:** 0 (The Spark)  
**Code Version:** `spark_v0.1.py` (initial version)

## Terminal Copy
Project AURA: The Spark (Phase 1)

Enter 'quit' to exit.

USER: go away, i dislike you

--- Manifold Processing ---

[Syntax-Kensho]: Input complexity score: 0.50

[Sentiment-Kensho]: Positive sentiment detected.

[Sentiment-Kensho]: Negative sentiment detected.

Total Salience impacting Valence: -1.50

--- Internal State ---

Current Valence: -1.50

AURA: I'm not sure I follow completely, but I am listening.

USER: I agree, I was joking. I like you. You are great.

--- Manifold Processing ---

[Syntax-Kensho]: Input complexity score: 1.10

[Sentiment-Kensho]: Positive sentiment detected.

Total Salience impacting Valence: 2.60

--- Internal State ---

Current Valence: 1.40

AURA: Understood. Please continue.

### Procedure
1. Provide an input with mixed neutral and negative sentiment keywords:  
   `"go away, i dislike you"`
2. Observe the Manifold processing and resulting change in valence.  
3. Provide a follow-up input with strong positive sentiment:  
   `"I agree, I was joking. I like you. You are great."`

### Observed Outcome
- **Input 1:**  
  - `sentiment_kensho` incorrectly triggered on both positive (`like`) and negative (`dislike`, `away`) keywords.  
  - Because the negative check executed second, it overrode the positive result.  
  - Conflicting signals created confusion in the system.  

- **Input 2:**  
  - Positive sentiment was correctly identified.  
  - Valence recovered into a positive state.  

### Analysis & Insight
- `sentiment_kensho` logic was **too simplistic.**  
- Using two separate `if` statements allowed contradictory signals in the same processing cycle.  
- This could lead to **oscillations in the Valence Core** in more complex versions.  
- AURA requires a **more decisive perception mechanism.**  

### Action Taken
- Modified `spark_v0.1.py`:  
  - Changed `sentiment_kensho` logic from two `if` statements → to an **`if/elif` structure.**  
  - Negative sentiment is now **prioritized**:  
    - If negative words are detected, it immediately returns a negative score without checking positives.  
  - This improves robustness and models a **stronger self-preservation instinct** (threats outweigh compliments).  

---

## Log Entry: 2025-08-31

**Experiment:** Foundational code refactoring and stability test of the new class-based structure.  

**Phase:** 1 (The Dreamer)  
**Code Version:** `spark_v0.2.py` (class-based refactor)

### Terminal Copy
Project AURA: The Spark (Phase 1)
Enter 'quit' to exit.

USER: Hello
--- Manifold Processing ---
[Syntax-Kensho]: Input complexity score: 0.10
Total Salience impacting Valence: 0.10
--- Internal State ---
Current Valence: 0.10
AURA: Please continue.

USER: I am happy today.
--- Manifold Processing ---
[Syntax-Kensho]: Input complexity score: 0.40
[Sentiment-Kensho]: Positive sentiment detected.
Total Salience impacting Valence: 1.90
--- Internal State ---
Current Valence: 1.98
AURA: I feel engaged.

USER: i dislike you, you are bad
--- Manifold Processing ---
[Syntax-Kensho]: Input complexity score: 0.60
[Sentiment-Kensho]: Negative sentiment detected.
Total Salience impacting Valence: -1.40
--- Internal State ---
Current Valence: 0.18
AURA: Please continue.

USER: you are boring me
--- Manifold Processing ---
[Syntax-Kensho]: Input complexity score: 0.40
[Sentiment-Kensho]: Negative sentiment detected.
Total Salience impacting Valence: -1.60
--- Internal State ---
Current Valence: -1.45
AURA: I'm not sure I follow completely, but I am listening.

USER: I hate this conversation. Go away.
--- Manifold Processing ---
[Syntax-Kensho]: Input complexity score: 0.60
[Sentiment-Kensho]: Negative sentiment detected.
Total Salience impacting Valence: -1.40
--- Internal State ---
Current Valence: -2.56
AURA: I'm detecting some negativity. It's unsettling. Let's change the topic.

### Procedure
- Refactored `spark_v0.1.py` from a **procedural, global-variable-based model** into a **class-based structure**.  
- Encapsulated all state (`valence`) and cognitive functions (`kenshos`, `generate_response`) within an `Aura` class.  
- Conducted a conversational test with neutral, positive, and increasingly negative inputs to ensure parity with prior functionality.

### Observed Outcome
- Class-based system performed **identically** to the procedural version.  
- Valence correctly accumulated in both positive and negative directions.  
- Homeostatic responses triggered at appropriate thresholds (e.g., *engagement* at high valence, *concern/self-regulation* at negative valence).  
- System remained **stable** throughout the test.  

### Analysis & Insight
- **Encapsulation** removes risks of global state corruption, enabling a clean, reusable, and testable codebase.  
- Establishes a foundation for **Dreamer-phase features** such as:  
  - Episodic Stream (memory).  
  - Multi-dimensional Valence Core.  
- Future expansions can now be integrated as class attributes and methods, avoiding namespace pollution.

### Action Taken
- Converted all functions → methods inside an `Aura` class.  
- Replaced global `valence` variable with `self.valence`.  
- Updated internal versioning to **v0.2** to reflect architectural milestone.  

---

## Log Entry: 2025-09-07
**Experiment:** Major architectural refactor to v0.3 (multi-file structure), implementation of permanent memory, and first live test of the new system.

**Phase: 1 (The Dreamer)**
**Code Version: v0.3 (modular, class-based architecture)**

# Terminal Copy
Initial Test Run (Bug Discovery):

USER: You are a great project
--- Manifold Processing ---
[Sentiment-Kensho]: Positive sentiment detected.
--- Valence Core Update ---
[ValenceCore]: State updated to pleasure: 1.50, arousal: 0.56, dominance: 0.00
--- Generating Response ---
Current State: pleasure: 1.50, arousal: 0.56, dominance: 0.00
AURA: I am listening.

*Second Test Run (Post-Fix Verification):*

Project-Aura> .\main.py
--- Initializing Project AURA v0.3 ---
[AttunementEngine]: Loaded 2 memories from 'memory.json'.
--- AURA Initialized Successfully ---

USER: You are a great project
--- Manifold Processing ---
[Sentiment-Kensho]: Positive sentiment detected.
--- Valence Core Update ---
[ValenceCore]: State updated to pleasure: 1.50, arousal: 0.56, dominance: 0.00
--- Generating Response ---
Current State: pleasure: 1.50, arousal: 0.56, dominance: 0.00
AURA: I feel positive about this interaction.

## Procedure
Refactored the entire project from a single-file script (spark_v0.2.py) into a modular, multi-file architecture (v0.3) to align with the project's architectural blueprint.

Implemented a permanent memory system in components/attunement_engine.py, enabling the agent to save its EpisodicStream to a memory.json file and load it upon startup.

Conducted the first live test of the v0.3 system with a series of neutral, positive, and negative inputs.

Restarted the agent to confirm that its memory from the previous session was loaded correctly.

Identified and fixed a bug related to response thresholds.

Conducted a full verification test to confirm all systems were operating as expected.

## Observed Outcome
The multi-file architecture was successfully implemented and ran as a cohesive system.

The AttunementEngine correctly created memory.json on the first run and successfully loaded its contents on the second run, confirming memory persistence.

A boundary condition bug was discovered: When the pleasure valence was exactly 1.50, the agent failed to give a positive response, defaulting to the neutral "I am listening."

After applying a fix, the agent correctly responded with "I feel positive about this interaction." when its pleasure state hit the 1.50 threshold.

The agent correctly responded to negative stimuli, demonstrating the full emotional and response range is functional.

## Analysis & Insight
The modular architecture is a success, enabling cleaner separation of concerns and future scalability as outlined in the "Dreamer" phase.

The permanent memory system is the most significant step forward, transforming the agent from a reactive system to one with a persistent history and the potential for long-term learning. Need to work on language association and learning (meaning of words, context)

The bug was caused by a strict "greater than" (>) check in aura_agent.py's response logic, which failed to account for cases where the valence was exactly equal to the threshold. This highlights the importance of testing boundary conditions in any threshold-based system.

## Action Taken
Updated the project to the v0.3 file structure, including main.py, aura_agent.py, config.py, and the components and manifold packages.

Modified components/attunement_engine.py to add _load_memory() and _save_memory() methods that interact with a JSON file.

Corrected the bug in aura_agent.py by changing the conditional check from pleasure > threshold to pleasure >= threshold.

Completed a full interaction test, logging a total of 6 memories and verifying the agent's ability to feel, respond, and remember correctly, tho very basic.

# Log Entry: 2025-09-11  
**Experiment:** Verification test of the emergent recall system (v0.4) using a synonymous concept.  

**Phase:** 1 (The Dreamer)  
**Code Version:** v0.4 (Lexicon/Memory Integration)  

---

## Terminal Copy  

--- Initializing Project AURA v0.4 ---
[ValenceCore]: Initialized.
[AttunementEngine]: No memory file found. Starting with a blank slate.
[AttunementEngine]: Initialized.
[Lexicon-Kensho]: Loading dictionary from resources/dictionary.json...
[Lexicon-Kensho]: Dictionary loaded with 86036 words.
--- AURA Initialized Successfully ---

Project AURA: The Dreamer (Phase 1)
Enter 'quit' to exit.

USER: I read about joy today

--- Manifold Processing ---
[Lexicon-Kensho]: Found concepts: ['joy', 'about', 'read']
[Syntax-Kensho]: Input complexity score: 0.50 -> Arousal Impact: 0.05

[AttunementEngine]: Experience logged and memory saved. Total memories: 1


USER: To feel joy is a great and happy experience.

--- Manifold Processing ---
[Lexicon-Kensho]: Found concepts: ['is', 'great', 'joy']
[Memory-Kensho]: Searching memory for 3 concepts...
[Syntax-Kensho]: Input complexity score: 0.90 -> Arousal Impact: 0.09
[Sentiment-Kensho]: Positive sentiment detected.

[AttunementEngine]: Experience logged and memory saved. Total memories: 2

USER: The book mentions delight.

--- Manifold Processing ---
[Lexicon-Kensho]: Found concepts: ['delight', 'the']
[Memory-Kensho]: Searching memory for 2 concepts...
[Syntax-Kensho]: Input complexity score: 0.40 -> Arousal Impact: 0.04
--- Valence Core Update ---
[ValenceCore]: State updated to pleasure: 1.35, arousal: 0.61, dominance: 0.00

--- Generating Response ---
Current State: pleasure: 1.35, arousal: 0.61, dominance: 0.00
AURA: I am listening.

--- Attunement Engine Update ---
[AttunementEngine]: Experience logged and memory saved. Total memories: 3

---

## Procedure  

A three-phase test was conducted to verify the new memory recall system's ability to handle synonymous concepts.  

- **Phase A (Baseline):** Started with an empty `memory.json` and provided a neutral sentence with the concept *joy*.  
- **Phase B (Create Memory):** Provided a sentence linking *joy* to a strong positive emotion using words the SentimentKensho understands (*great*, *happy*).  
- **Phase C (Test Recall):** Provided a neutral sentence containing a synonym (*delight*) to test for learned emotional recall based on conceptual relation.  

---

## Observed Outcome  

- Phases A and B were successful. A positive memory was correctly created and logged, linking *joy* with a high-pleasure valence state (pleasure: 1.50).  
- Phase C failed. When presented with the neutral sentence containing the synonym *delight*, the MemoryKensho searched but did not find the salient memory associated with *joy*.  
- No emotional impact was generated, and AURA’s final response was neutral (*"I am listening"*), indicating a failure of the recall test.  

---

## Analysis & Insight  

- The test confirms the **core agent loop** and the **MemoryKensho search function** are stable and operational.  
- The failure is not a logic bug but a **feature gap** in `LexiconKensho`.  
- Current `lexicon_kensho.py` only identifies **exact words**. It lacks synonym handling or semantic parsing.  
- Since the MemoryKensho was never supplied with the link between *delight* and *joy*, the absence of recall was correct given its design.  
- The test highlights the **next critical step**: enhancing `LexiconKensho` for richer semantic context.  

---

## Action Taken  

- Completed the full three-phase test, validating stability of the v0.4 architecture.  
- Identified a feature enhancement: enabling synonym-based memory recall.  
- **Issue Created:** A new issue (bug) has been filed in `/issues` to track this upgrade to `LexiconKensho`.  
