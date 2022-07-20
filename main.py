from tkinter import *

'''
IMPORTANT ABOUT TKINTER:
Each line is 25 pixels in height
Each letter is 8 pixels in length
'''

database_dict = {
    
}

def printit(input1, input2):
    print(input1)
    print(input2)

def loginSetup():
    userText = Label(window, text="Username:")
    userText.place(x=160, y=80)

    userBox = Entry(window, width=30)
    userBox.place(x=160, y=100)

    passText = Label(window, text="Password:")
    passText.place(x=160, y=130)

    passBox = Entry(window, width=30, show="*")
    passBox.place(x=160, y=150)

    backButton = Button(window, text="Back", width=10, command=lambda: [userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=254)

    enterButton = Button(window, text="Enter", width=10, command=lambda: [printit(userBox.get(), passBox.get())])
    enterButton.place(x=160, y=175)

    exitButton = Button(text="Exit", width=10, command=window.destroy)
    exitButton.place(x=400, y=254)

def signupSetup():
    userText = Label(window, text="Set a username:")
    userText.place(x=160, y=80)

    userBox = Entry(window, width=30)
    userBox.place(x=160, y=100)

    passText = Label(window, text="Set a password:")
    passText.place(x=160, y=130)

    passBox = Entry(window, width=30, show="*")
    passBox.place(x=160, y=150)

    backButton = Button(window, text="Back", width=10, command=lambda: [userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=254)

    enterButton = Button(window, text="Enter", width=10, command=lambda: [printit(userBox.get(), passBox.get())])
    enterButton.place(x=160, y=175)

    exitButton = Button(text="Exit", width=10, command=window.destroy)
    exitButton.place(x=400, y=254)

def menu():
    loginButton = Button(window, text="Login", width=10, command=lambda: [loginButton.destroy(), signupButton.destroy(), exitButton.destroy(), loginSetup()])
    loginButton.place(x=145, y=100)

    signupButton = Button(window, text="Sign Up", width=10, command=lambda: [loginButton.destroy(), signupButton.destroy(), exitButton.destroy(), signupSetup()])
    signupButton.place(x=276, y=100)

    exitButton = Button(text="Exit", width=10, command=window.destroy)
    exitButton.place(x=210, y=254)


window = Tk()

window.geometry("500x300")

window.title("Application Project")

menu()

window.mainloop()