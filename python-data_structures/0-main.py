def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

# Test cases
if __name__ == "__main__":
    print(no_c("School"))   # Output: Holberton Shool
    print(no_c("Chicago"))            # Output: hiago
    print(no_c("holberton school"))          # Output:  is fun!
    print(no_c(""))
    print(no_c("HellcCcccooccoscccss"))
