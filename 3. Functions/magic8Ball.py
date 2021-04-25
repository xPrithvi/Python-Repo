import random

def getAnswer(number):
    if number == 1:
        return "It is certain."
    elif number == 2:
        return "It is decidedly so."
    elif number == 3:
        return "Yes."
    elif number == 4:
        return "Reply hazy, ask again."
    elif number == 5:
        return "My reply is no."
    elif number == 6:
        return "Ask again later."
    elif number == 7:
        return "Concentrate and ask again."
    elif number == 8:
        return "Outlook not so good."
    elif number == 9:
        return "Very doubtful."

while True:
    input("Ask a question: ")
    print(getAnswer(random.randint(1,9)))
