def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    
    # Initialize variables to keep track of the maximum score and the corresponding key
    max_score = float("-inf")
    best_key = None
    
    # Iterate through the dictionary
    for key, value in a_dictionary.items():
        # Update the best_key if we find a higher score
        if value > max_score:
            max_score = value
            best_key = key
    
    return best_key

# Test the function
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
