def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

# Test cases
if __name__ == "__main__":
    print(no_c("School"))               # Correct output: Shool
    print(no_c("Chicago"))              # Correct output: hiago
    print(no_c("Holberton"))            # Correct output: Holberton
    print(no_c("Holberton School"))     # Correct output: Holberton Shool
    print(no_c(""))                     # Correct output: (empty string)
    print(no_c("HellcCcccooccoscccss")) # Correct output: Hellooosss
