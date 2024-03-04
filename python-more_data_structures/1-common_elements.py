def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate through each element in set_1
    for element in set_1:
        # Check if the element is present in set_2
        if element in set_2:
            # If yes, add it to the common_set
            common_set.add(element)

    return common_set

# Test the function
if __name__ == "__main__":
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
