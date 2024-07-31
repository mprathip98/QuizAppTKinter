from customtkinter import *
from QandA import *
from tkinter import messagebox

window = CTk()
window.title("Quiz App")
window.geometry("1100x600")
window.configure(background='lightBlue')
set_appearance_mode('dark')
window.resizable(False, False)


def checkAnswer(choice):
    question = quiz_data[currentQuestion]
    selectedChoice = choiceBtns[choice].cget("text")

    if selectedChoice == question["answer"]:
        global score
        score += 1
        resultLabel.configure(text=f"{score}/{len(quiz_data)}")
        feedbackLabel.configure(text="Correct")
    else:
        feedbackLabel.configure(text="INCORRECT")
    for button in choiceBtns:
        button.configure(state="disabled")
    submitButton.configure(state="normal")

def nextC(m):
    global currentQuestion
    currentQuestion += 1
    if currentQuestion < len(quiz_data):
        showQuestion()
    else:
        messagebox.showinfo(message = f"Quiz Completed \n Score = {score}/{len(quiz_data)}")

def showQuestion():
    question = quiz_data[currentQuestion]
    questionLabel.configure(text=question["question"])
    choices = question["choices"]
    for i in range(4):
        choiceBtns[i].configure(text=choices[i], state="normal") # Reset button state
    feedbackLabel.configure(text=" ")
    submitButton.configure(state='disabled')

questionLabel = CTkLabel(master=window,

                         font=("Impact", 35),
                         bg_color="darkBlue",
                         width = 700,
                         height=100,
                         corner_radius=95,
                         )
questionLabel.pack(padx=10, pady=20)


choiceBtns = []
for i in range(4):
    button = CTkButton(master=window, command=lambda i = i: checkAnswer(i), font = ("Impact", 15), width= 200, height=40)
    button.pack(padx=20, pady=10)
    choiceBtns.append(button)

feedbackLabel = CTkLabel(master=window)
feedbackLabel.pack(padx=10, pady=10)

score = 0
resultLabel = CTkLabel(master=window, text = f"0 / {len(quiz_data)}")
resultLabel.pack(padx=10, pady=20)

submitButton = CTkButton(master=window,
                         text="NEXT",
                         corner_radius=25,
                         fg_color='lightBlue',
                         font=("Impact", 25),
                         command=next,
                         text_color='black',
                         state="disabled")
submitButton.pack(pady=20)

currentQuestion = 0

showQuestion()
window.bind("<Return>",nextC)
window.mainloop()
