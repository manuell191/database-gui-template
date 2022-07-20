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
    userText.place(x=225, y=130)

    userBox = Entry(window, width=50)
    userBox.place(x=225, y=150)

    passText = Label(window, text="Password:")
    passText.place(x=225, y=180)

    passBox = Entry(window, width=50, show="*")
    passBox.place(x=225, y=200)

    backButton = Button(window, text="Back", width=10, command=lambda: [userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=404)

    enterButton = Button(window, text="Enter", width=10, command=lambda: [printit(userBox.get(), passBox.get())])
    enterButton.place(x=225, y=225)

    exitButton = Button(text="Exit", width=10, command=window.destroy)
    exitButton.place(x=650, y=404)

def signupSetup():
    userText = Label(window, text="Set a username:")
    userText.place(x=225, y=130)

    userBox = Entry(window, width=50)
    userBox.place(x=225, y=150)

    passText = Label(window, text="Set a password:")
    passText.place(x=225, y=180)

    passBox = Entry(window, width=50, show="*")
    passBox.place(x=225, y=200)

    backButton = Button(window, text="Back", width=10, command=lambda: [userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=404)

    enterButton = Button(window, text="Enter", width=10, command=lambda: [printit(userBox.get(), passBox.get())])
    enterButton.place(x=225, y=225)

    exitButton = Button(text="Exit", width=10, command=window.destroy)
    exitButton.place(x=650, y=404)

def menu():
    loginButton = Button(window, text="Login", width=10, command=lambda: [loginButton.destroy(), signupButton.destroy(), exitButton.destroy(), loginSetup()])
    loginButton.place(x=240, y=175)

    signupButton = Button(window, text="Sign Up", width=10, command=lambda: [loginButton.destroy(), signupButton.destroy(), exitButton.destroy(), signupSetup()])
    signupButton.place(x=431, y=175)

    exitButton = Button(text="Exit", width=10, command=window.destroy)
    exitButton.place(x=335, y=404)


window = Tk()

window.geometry("750x450")

window.title("Application Project")

menu()

window.mainloop()