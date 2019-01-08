import random

pickDictionary = ""
key = 0
encrypting = ""
dictionary = ""
reference = ""

while encrypting != "e" and encrypting != "d":
    encrypting = input("Would you like to encrypt or decrypt? ( e / d ) ")

while True:
    try:
        key = int(input("Please enter a valid password. It should be a positive integer: "))  # tbh any integer will do.
        if 1 <= key:
            break
        else:
            print("Invalid response. Your number is not positive.")
    except ValueError:
        print("Invalid response. Value must be integer")

while pickDictionary != "letter" and pickDictionary != "advanced" and pickDictionary != "random" \
        and pickDictionary != "custom":
    pickDictionary = input("Which dictionary would you like to use? ( letter / advanced / random / custom ) ")

if pickDictionary == "letter":
    dictionary = "abcdefghijklmnopqrstuvwxyz"
elif pickDictionary == "advanced":
    dictionary = "`-=~_+ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]\\{}|;':\",./<>?abcdefghijklmnopqrstuvwxyz1234567890"
elif pickDictionary == "random":
    complexDictionary = []
    for letter in "`-=~_+ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]\\{}|;':\",./<>?abcdefghijklmnopqrstuvwxyz1234567890":
        complexDictionary.append(letter)
    random.shuffle(complexDictionary)
    for letter in complexDictionary:  # Note that double quote mark is used.
        dictionary += letter
        if letter == "\\":
            reference += "\\\\"
        elif letter == "\"":
            reference += "\\\""
        else:
            reference += letter

elif pickDictionary == "custom":
    dictionary = input("Paste your dictionary here: ")

message = input("Enter your message: ")
newMessage = ""
for character in message:
    position = dictionary.find(character)
    if position == -1:
        newMessage += character
    else:
        if encrypting == "e":
            newPosition = (position + key) % len(dictionary)
        elif encrypting == "d":
            newPosition = (position - key) % len(dictionary)
        newMessage += dictionary[newPosition]

print()
print(newMessage)
if pickDictionary == "random":
    print("The dictionary used is", dictionary)
    print("Please be advised that the dictionary is defined as a string with a double quote mark.")
