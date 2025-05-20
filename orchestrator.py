from prompt_handler import get_task_from_prompt, handle_sentiment, handle_cleaning

def main():
    print(">> AI Orchestrator Started")
    user_input = input("What do you want to do? ")

    task = get_task_from_prompt(f"What task is this: '{user_input}'? Choose from: clean data, sentiment analysis.")

    if "sentiment" in task.lower():
        handle_sentiment(user_input)
    elif "clean" in task.lower():
        handle_cleaning(user_input)
    else:
        print("Sorry, I couldn't understand the task.")

if __name__ == "__main__":
    main()
