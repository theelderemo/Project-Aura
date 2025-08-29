# Project AURA: Experiment Log

This document is a **living log** of experiments, outcomes, bugs, and insights discovered during the development of Project AURA.

---

## Log Entry: 2025-08-29

**Experiment:** Initial test of the v0.1 Spark's homeostatic feedback loop with conflicting sentiment.  

**Phase:** 1 (The Spark)  
**Code Version:** `spark_v0.1.py` (initial version)

---

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

---

### Procedure
1. Provide an input with mixed neutral and negative sentiment keywords:  
   `"go away, i dislike you"`
2. Observe the Manifold processing and resulting change in valence.  
3. Provide a follow-up input with strong positive sentiment:  
   `"I agree, I was joking. I like you. You are great."`

---

### Observed Outcome
- **Input 1:**  
  - `sentiment_kensho` incorrectly triggered on both positive (`like`) and negative (`dislike`, `away`) keywords.  
  - Because the negative check executed second, it overrode the positive result.  
  - Conflicting signals created confusion in the system.  

- **Input 2:**  
  - Positive sentiment was correctly identified.  
  - Valence recovered into a positive state.  

---

### Analysis & Insight
- `sentiment_kensho` logic was **too simplistic.**  
- Using two separate `if` statements allowed contradictory signals in the same processing cycle.  
- This could lead to **oscillations in the Valence Core** in more complex versions.  
- AURA requires a **more decisive perception mechanism.**  

---

### Action Taken
- Modified `spark_v0.1.py`:  
  - Changed `sentiment_kensho` logic from two `if` statements → to an **`if/elif` structure.**  
  - Negative sentiment is now **prioritized**:  
    - If negative words are detected, it immediately returns a negative score without checking positives.  
  - This improves robustness and models a **stronger self-preservation instinct** (threats outweigh compliments).  

---
