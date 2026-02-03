# GenAI-drift_audit
An adversarial testing tool designed to quantify semantic drift and behavioral instability (AI Psychosis) in Generative AI outputs.
Project: GenAI-Drift-Audit
Mission
To detect and quantify "AI Hallucination" through semantic variance. This tool measures how much an LLM's logic drifts when presented with the same adversarial or complex prompt multiple times.

The Theory
High-stability models should maintain high semantic similarity. When a model begins to output "out-of-distribution" (OOD) logic (AI Psychosis), the consistency score drops.

How it Works
Inputs multiple responses from a single prompt.

Uses difflib to calculate the Ratio of Similarity.

Flags responses that fall below a specific safety threshold (default 0.7).
