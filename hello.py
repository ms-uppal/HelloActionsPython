import os

def get_greeting():
    # Retrieve environment variable WHO_TO_GREET (default to 'World' if missing)
    who_to_greet = os.environ.get("WHO_TO_GREET", "World")
    return f"Hello, {who_to_greet}!"

if __name__ == "__main__":
    print(get_greeting())
