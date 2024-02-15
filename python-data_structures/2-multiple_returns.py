Write a function that returns a tuple with the length of a string and its first character.

    Prototype: def multiple_returns(sentence):
    If the sentence is empty, the first character should be equal to None
    You are not allowed to import any module

guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
multiple_returns = __import__('2-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/$ ./2-main.py
Length: 32 - First character: A
guillaume@ubuntu:~/$ 
