from tkinter import *
from customtkinter import *

'''
IMPORTANT ABOUT TKINTER:
Each line is 25 pixels in height
Each letter is 8 pixels in length
'''

set_appearance_mode("dark")

set_default_color_theme("dark-blue")

def changePass1():
    passTxt = CTkLabel(window, text="Enter your password to verify it's you")
    passTxt.place(x=270, y=100)

    checkPass = CTkEntry(window, width=300)
    checkPass.place(x=225, y=150)

    backButton = CTkButton(window, text="Back", width=80, command=lambda: [passTxt.destroy(), checkPass.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), account()])
    backButton.place(x=25, y=404)

    enterButton = CTkButton(window, text="Enter", width=80)
    enterButton.place(x=225, y=200)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=650, y=404)

def invalid():
    invalidText = CTkLabel(window, text="Username or password invalid")
    invalidText.place(x=280, y=100)

    tryAgain = CTkButton(window, text="Try Again", width=80, command=lambda: [invalidText.destroy(), tryAgain.destroy(), backButton.destroy(), exitButton.destroy(), loginSetup()])
    tryAgain.place(x=335, y=175)

    backButton = CTkButton(window, text="Back", width=80, command=lambda: [invalidText.destroy(), tryAgain.destroy(), backButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=404)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=650, y=404)

def account():
    welcomeText = CTkLabel(window, text="Welcome back!")
    welcomeText.pack(side=TOP, pady=75)

    changePassword = CTkButton(window, text="Change Password", width=120, command=lambda: [welcomeText.destroy(), changePassword.destroy(), logoutButton.destroy(), exitButton.destroy(), changePass1()])
    changePassword.place(x=315, y=175)

    logoutButton = CTkButton(window, text="Log Out", width=80, command=lambda: [changePassword.destroy(), logoutButton.destroy(), exitButton.destroy(), menu()])
    logoutButton.place(x=25, y=404)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=650, y=404)

def login(username, password):
    database_dict = {

    }

    f = open("database.txt", "r")
    database_reference = f.readlines()

    for i in database_reference:
        split_data = i.split(";")
        database_dict[split_data[0]] = split_data[1]
    
    if username in database_dict:
        if database_dict[username] == password:
            print("You logged in!\n")
            account()
        else:
            print("Username or password invalid.")
            invalid()
    else:
        print("Username or password invalid.")
        invalid()

def signUp(username, password):
    new_user_list = [username, ";", password, ";", "\n"]
    f = open("database.txt", "a")
    f.write("".join(new_user_list))

    successText = CTkLabel(window, text="You have now created a new account!")
    successText.place(x=280, y=100)

    continueButton = CTkButton(window, text="Continue", width=80, command=lambda: [successText.destroy(), continueButton.destroy(), exitButton.destroy(), menu()])
    continueButton.place(x=335, y=175)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=650, y=404)

def loginSetup():
    userText = CTkLabel(window, text="Username:")
    userText.place(x=190, y=100)

    userBox = CTkEntry(window, width=300)
    userBox.place(x=225, y=125)

    passText = CTkLabel(window, text="Password:")
    passText.place(x=190, y=175)

    passBox = CTkEntry(window, width=300, show="*")
    passBox.place(x=225, y=200)

    backButton = CTkButton(window, text="Back", width=80, command=lambda: [userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=404)

    enterButton = CTkButton(window, text="Enter", width=80, command=lambda: [login(userBox.get(), passBox.get()), userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy()])
    enterButton.place(x=225, y=250)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=650, y=404)

def signupSetup():
    userText = CTkLabel(window, text="Set a username:")
    userText.place(x=205, y=100)

    userBox = CTkEntry(window, width=300)
    userBox.place(x=225, y=125)

    passText = CTkLabel(window, text="Set a password:")
    passText.place(x=205, y=175)

    passBox = CTkEntry(window, width=300, show="*")
    passBox.place(x=225, y=200)

    backButton = CTkButton(window, text="Back", width=80, command=lambda: [userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy(), menu()])
    backButton.place(x=25, y=404)

    enterButton = CTkButton(window, text="Enter", width=80, command=lambda: [signUp(userBox.get(), passBox.get()), userText.destroy(), userBox.destroy(), passText.destroy(), passBox.destroy(), backButton.destroy(), enterButton.destroy(), exitButton.destroy()])
    enterButton.place(x=225, y=250)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=650, y=404)

def menu():
    loginButton = CTkButton(window, text="Login", width=80, command=lambda: [loginButton.destroy(), signupButton.destroy(), exitButton.destroy(), loginSetup()])
    loginButton.place(x=240, y=175)

    signupButton = CTkButton(window, text="Sign Up", width=80, command=lambda: [loginButton.destroy(), signupButton.destroy(), exitButton.destroy(), signupSetup()])
    signupButton.place(x=431, y=175)

    exitButton = CTkButton(text="Exit", width=80, command=window.destroy)
    exitButton.place(x=335, y=404)


window = CTk()

window.geometry("750x450")

window.title("Application Project")

menu()

window.mainloop()