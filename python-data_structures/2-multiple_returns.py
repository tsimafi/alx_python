def multiple_returns(sentence):
    if len(sentence) == 0:
        return 0, None
    else:
        return len(sentence), sentence[0]

# Test cases
sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

sentence = "Holberton"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

sentence = "Holberton is so cool"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

sentence = "H"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
