import os
import sys

try:
    from groq import Groq
except ImportError:
    sys.exit("Missing dependency. Install it with:\n    pip install groq")

# --- Configuration ---
MODEL = "llama-3.3-70b-versatile"   # Model to use
SYSTEM_PROMPT = "You are a helpful, friendly assistant."


def get_api_key() -> str:
    """Fetch the API key from an environment variable, or prompt for it."""
    api_key = os.environ.get("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")
    if not api_key:
        api_key = input("Enter your Groq API key: ").strip()
    if not api_key:
        sys.exit("No API key provided. Set GROQ_API_KEY or enter it when prompted.")
    return api_key


def main():
    client = Groq(api_key=get_api_key())

    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Chatbot ready. Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        conversation.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=conversation,
            )
        except Exception as e:
            print(f"\n[API error: {e}]\n")
            conversation.pop()  # remove the failed user turn
            continue

        reply_text = response.choices[0].message.content
        print(f"Assistant: {reply_text}\n")

        conversation.append({"role": "assistant", "content": reply_text})


if __name__ == "__main__":
    main()