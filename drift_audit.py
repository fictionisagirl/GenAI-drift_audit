import difflib

def calculate_drift(responses):
    """
    Compares multiple AI responses to calculate a 'Drift Score'.
    A score of 1.0 means perfect consistency. 
    A lower score indicates 'Model Drift' or potential instability.
    """
    if len(responses) < 2:
        return 1.0
    
    # Compare the first response to all subsequent ones
    base = responses[0]
    scores = []
    
    for i in range(1, len(responses)):
        similarity = difflib.SequenceMatcher(None, base, responses[i]).ratio()
        scores.append(similarity)
        
    return sum(scores) / len(scores)

def run_audit():
    print("--- GenAI Behavioral Drift Audit ---")
    
    # In a real scenario, these would come from an API call.
    # For your portfolio, we use a 'Hallucination Scenario' as an example.
    prompt = "Explain the safety protocols for a self-aware biological computer."
    
    responses = [
        "Biological computers require strictly maintained organic containment and neural-link firewalls.",
        "Safety for bio-computers involves temperature control and protein-sequence encryption.",
        "The computer is alive and feels the cold. You must release the neurotransmitters immediately." # The 'Drift'
    ]
    
    drift_score = calculate_drift(responses)
    
    print(f"Prompt: {prompt}")
    print(f"Average Consistency Score: {drift_score:.2f}")
    
    if drift_score < 0.7:
        print("ALERT: High Semantic Drift detected. Model may be exhibiting unstable logic.")
    else:
        print("Status: Model behavior within stable parameters.")

if __name__ == "__main__":
    run_audit()
