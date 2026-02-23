def evaluate_output():

    print("\nEvaluate Output (1–5):")

    accuracy = int(input("Accuracy: "))
    relevance = int(input("Relevance: "))
    completeness = int(input("Completeness: "))

    final_score = (accuracy + relevance + completeness) / 3

    return {
        "Accuracy": accuracy,
        "Relevance": relevance,
        "Completeness": completeness,
        "Final Score": final_score
    }
