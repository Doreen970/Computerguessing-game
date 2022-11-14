print("Welcome to my computer game")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay let's play")
score = 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What is the capital city of Kenya? ")
if answer.lower() == "nairobi":
    print("right")
    score += 1
else:
    print("wrong answer")

answer = input("Where is Kenya found? ")
if answer.lower() == "africa":
    print("correct")
    score += 1
else:
    print("wrong")

print(score)
print("You got" + str(score) + "marks")


