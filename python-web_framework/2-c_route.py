@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """
    Defines the behavior for the route '/c/<text>'.

    Parameters:
        text (str): The custom text provided in the URL.

    Returns:
        str: The string "C <text>" with underscores replaced by spaces.
    """
    # Replace underscores with spaces
    text_with_spaces = text.replace("_", " ")
    # Capitalize the first letter of each word
    text_formatted = ' '.join(word.capitalize() for word in text_with_spaces.split())
    return "C {}".format(text_formatted)
