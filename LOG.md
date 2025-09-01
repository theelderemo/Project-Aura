# Project AURA: Experiment Log

This document is a **living log** of experiments, outcomes, bugs, and insights discovered during the development of Project AURA.

---

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
