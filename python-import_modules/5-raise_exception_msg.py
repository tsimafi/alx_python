def raise_exception_msg(message=""):
    raise NameError(message)

# Test the function
if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)