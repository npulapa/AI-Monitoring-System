def evaluate_answer(answer):
    correct_answer = "Paris is the capital of France"

    if answer.strip().lower() == correct_answer.lower():
        return {
            "score": "correct",
            "feedback": "Good job!"
        }
    else:
        return {
            "score": "wrong",
            "feedback": "Try again."
        }


# Run program
if __name__ == "__main__":
    user_answer = input("Enter your answer: ")
    result = evaluate_answer(user_answer)
    print(result)
