import random

RESPONSES = ["It is certian.", "It is decidedly so.", "Yes definitely."
             , "Reply hazy, try again later.", "Ask again later.", "Concentrate and ask again.",
             "My reply is no.", "Outlook no so good.", "Very doubtful."]

while True:
    print("What is your question?")
    user_question = input(">> ")
    
    if user_question is not "":
        print(RESPONSES[random.randint(0, (len(RESPONSES)-1))])
        print("")
    else:
        break
input("Press any key to exit...")
