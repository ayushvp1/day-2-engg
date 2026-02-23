from input_layer import get_user_input
from pipeline import run_pipeline
from evaluation_layer import evaluate_output

if __name__ == "__main__":

    question = get_user_input()

    print("\n--- AI Assistant Response ---\n")

    output = run_pipeline(question)
    print(output)

    score = evaluate_output()

    print("\n--- Evaluation Result ---")
    print(score)
