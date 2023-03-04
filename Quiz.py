import random

statements = [
    "The sky is pink.",
    "Birds can fly.",
    "The Earth is flat.",
    "Tomato is a vegetable.",
    "Sea water is salty.",
    "2+2+5",
    "Computing saves lives!!"
]

random.shuffle(statements)

score = 0

for statement in statements:
    print(statement)
    answer = input("True or false? ").lower()
    if answer == "true":
        if statement == "Birds can fly." or statement == "Sea water is salty." or statement == "Computing saves lives!!":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    elif answer == "false":
        if statement == "Birds can fly." or statement == "Sea water is salty." or statement == "Computing saves lives!!":
            print("Incorrect!")
        else:
            print("Correct!")
            score += 1
    else:
        print("Invalid answer.")

print("Your score is:", score)
