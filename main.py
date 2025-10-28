# main.py

from jokes import get_random_joke
from utils import format_output

def main():
    """
    Main function to get and display a random programming joke.
    """
    joke = get_random_joke()
    if joke:
        formatted_joke = format_output(joke['setup'], joke['punchline'])
        print(formatted_joke)
    else:
        print("Could not retrieve a joke at this moment. Please try again later.")

if __name__ == "__main__":
    main()