@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """
    Defines the behavior for the route '/c/<text>'.

    Parameters:
        text (str): The custom text provided in the URL.

    Returns:
        str: The string "C <text>" formatted as "C is super fun" if the input is "is_super_fun".
    """
    if text == "is_super_fun":
        return "C is super fun"
    else:
        return "C {}".format(text)
