import subprocess
import threading
import sys
import time

# Loading Spinner
class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)

# Feedback System
feedback_log = []

def collect_feedback(ai_response):
    feedback = input("\nWas this response helpful? (yes/no): ").strip().lower()
    feedback_entry = {"response": ai_response, "feedback": feedback}
    feedback_log.append(feedback_entry)

    with open("feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(str(feedback_entry) + "\n")

    print("✅ Feedback recorded!\n")

# AI Runner 

def run_ollama(prompt):
    """Run ollama and return full response"""
    with Spinner():
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )
    return result.stdout.strip()


def chat_with_ai(query):
    print("\n🤖 AI Response:\n")
    response = run_ollama(query)
    print(response)
    return response


def summarize_text(text):
    print("\n📌 Summary:\n")
    response = run_ollama(f"Summarize this text:\n{text}")
    print(response)
    return response


def generate_creative_content(prompt):
    print("\n✨ Creative Content:\n")
    response = run_ollama(f"Generate creative content:\n{prompt}")
    print(response)
    return response

# CLI Main Menu
def main():
    while True:
        print("\n==============================")
        print(" Welcome to your AI Assistant ")
        print("==============================")
        print("1. Answer Questions")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            while True:
                query = input("\nEnter your question (or type 'back' to return): ")
                if query.lower() == "back":
                    break
                ai_response = chat_with_ai(query)
                collect_feedback(ai_response)

        elif choice == "2":
            while True:
                text = input("\nEnter text to summarize (or type 'back' to return): ")
                if text.lower() == "back":
                    break
                ai_response = summarize_text(text)
                collect_feedback(ai_response)

        elif choice == "3":
            while True:
                prompt = input("\nEnter a creative prompt (or type 'back' to return): ")
                if prompt.lower() == "back":
                    break
                ai_response = generate_creative_content(prompt)
                collect_feedback(ai_response)

        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
