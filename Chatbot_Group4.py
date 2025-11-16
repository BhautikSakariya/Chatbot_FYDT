import time
import sys
import random


def get_time():
    return time.strftime("%H:%M:%S")


def chatbot_answer(user_input):
    user_input = user_input.lower()
    final_answer = ""

    if user_input != "bye":

        questions_answers = (["name", f"{get_time()} My name is ChatBot.", f"{get_time()} I am ChatBot.", f"{get_time()} You can call me ChatBot.", f"{get_time()} I am ChatBot created in Python."],
                             ["time",
                                 f"{get_time()} The current time is {get_time()}.",  f"{get_time()} The Time Right Now is {get_time()}.", f"{get_time()} It's {get_time()} now.", f"{get_time()} The Time is {get_time()}."],
                             ["date",
                                 f"{get_time()} Today's date is {time.strftime('%Y-%m-%d')}.", f"{get_time()} The Date Today is {time.strftime('%Y-%m-%d')}.", f"{get_time()} It's {time.strftime('%Y-%m-%d')} Today.", f"{get_time()} Today's Date is {time.strftime('%Y-%m-%d')}."],
                             ["your age",
                                 f"{get_time()} I don’t have an age, I’m just a program.", f"{get_time()} I am just Bot I do not age", f"{get_time()} I am just Computer Program I don't have any Age", f"{get_time()} I have no age because i am a Bot"],
                             ["who made you",
                                 f"{get_time()} I was created by a developer.", f"{get_time()} A Group of Developers programmed me", f"{get_time()} I am a Computer Program created in python", f"{get_time()} I Programmed by Python Devloper"],
                             ["created you",
                                 f"{get_time()} I was created by a developer.",  f"{get_time()} A Group of Developers programmed me", f"{get_time()} I am a Computer Program created in python", f"{get_time()} I Programmed by Python Devloper"],
                             ["weather",
                                 f"{get_time()} I can’t check the weather right now, but I hope it’s nice!", f"{get_time()} Right now i am unable to check Weather, but I hope it's Good Outside", f"{get_time()} Sorry!.. , I am not able to know how is the weather, But I hope it good", f"{get_time()} I hope it's nice, Because I can not check weather yet"],
                             ["where are you",
                              f"{get_time()} I live inside this Computer.", f"{get_time()} I am Running inside this Computer", f"{get_time()} I exist within the computer's architecture.", f"{get_time()} The Computer is my Home."],
                             ["how are you",
                              f"{get_time()} I’m good, thanks for asking!", f"{get_time()} I'm excellent; what can I help you with?", f"{get_time()} Feeling great, thank you for asking", f"{get_time()} I'm operating perfectly and ready to help you with your next question!"],
                             ["what can you do",
                              f"{get_time()} I can answer simple questions and show the time and date.", f"{get_time()} I am a ChatBot, I can give you Answer of your simple Questions .", f"{get_time()} I am able to Answer your Questions.", f"{get_time()} I provide information, answer your questions."],
                             ["help", f"{get_time()} You can ask me about the time, date, or something simple.", f"{get_time()} What kind of help you need. I can answer your Quetions .",
                              f"{get_time()} I'm here to help! What is it that you need assistance with right now?.", f"{get_time()} You can type what kind of help you need I try to help you"]
                             )

        for i in range(len(questions_answers)):

            if str(questions_answers[i][0]) in user_input:
                random_answer = int(random.randint(1, 4))
                final_answer = str(questions_answers[i][random_answer])
                break

        if final_answer != "":
            print(final_answer)
        else:
            print(f"{get_time()} How can I help you?")

    else:
        print(f"{get_time()} Goodbye!")
        sys.exit()


def chatbot():
    print(f"{get_time()} Hello!")
    print(f"{get_time()} How can I help you?")
    print(f"{get_time()} Type 'bye' to exit.")

    while True:
        user_input = input(f"{get_time()} You: ")
        print(f"{get_time()} You said: {user_input}")

        if user_input.lower() == "bye":
            print(f"{get_time()} Goodbye!")
            break
        else:
            chatbot_answer(user_input)


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--question":
        user_input = " ".join(sys.argv[2:])
        chatbot_answer(user_input)
    else:
        chatbot()


main()
