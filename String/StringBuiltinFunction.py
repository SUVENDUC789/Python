# String function

w = "Hello my name is Suvendu Chowdhury"

print("String Length is : ", len(w))  # length of the string

# Each word first letter is capital
print(w.title())

# Only first letter is capital others are small
print(w.capitalize())

# all are in lower case
print(w.lower())

# all are in uppercase
print(w.upper())

w1 = "Hello is the Hello, Hello bro,Hello"
print(w1.count("Hello", 10, 20))
print(w1.count("Hello"))

print(w1.find('Hello',10,20))
print(w1.find('Hee'))

w2='        Hi how are you      '
print(w2.strip())

print(w2.replace('you','Rahul ?'))
