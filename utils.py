# utils.py

def format_output(setup, punchline):
    """
    Formats the joke for a nice console output.
    
    Args:
        setup (str): The setup of the joke.
        punchline (str): The punchline of the joke.
        
    Returns:
        str: The formatted joke.
    """
    separator = "-" * 30
    return f"\n{separator}\n\n{setup}\n\n... {punchline}\n\n{separator}\n"