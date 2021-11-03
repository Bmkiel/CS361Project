# Imports
import tkinter.messagebox
from tkinter import *
from tkinter import font as tkfont
from PIL import ImageTk, Image
import json
import requests


# ========== Functions ==========
def selectedFrom(event):
    """
    Grabs the user's selection from the drop down menu from CURRENT
    """
    # Grab user's current currency selection
    from_ = pickCurrencyFrom.get()
    # Checks currency and outputs accordingly
    if from_ == "USD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/UnitedStatesDollar/1')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "EUR":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/European_Currency/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "JPY":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Japan_Currency/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "GBP":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Great_Britain_Pound/1')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "AUD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Austrailian_dollar/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "CAD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Canadian_dollar/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "CHF":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Swissfranc/3')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo, font=font3)
    elif from_ == "HKD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/HKD/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)
    elif from_ == "NZD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/NZD/1')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(currentInfo, text=textinfo)

def selectedTo(event):
    """
    Grabs the user's selection from the drop down menu from DESIRED
    """
    # Grab user's desired currency selection
    to_ = pickCurrencyTo.get()
    # Checks currency and outputs accordingly
    if to_ == "USD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/UnitedStatesDollar/1')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "EUR":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/European_Currency/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "JPY":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Japan_Currency/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "GBP":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Great_Britain_Pound/1')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "AUD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Austrailian_dollar/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "CAD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Canadian_dollar/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "CHF":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/Swissfranc/3')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo, font=font3)
    elif to_ == "HKD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/HKD/2')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)
    elif to_ == "NZD":
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'https://wiki-scrape-361.herokuapp.com/firstpara/NZD/1')
        data = response.json()
        textinfo = data['output']
        canvas1.itemconfig(desireInfo, text=textinfo)

def clearValues():
    """
    Used to clear current/desired input fields and current selection of currencies
    No returns
    """
    message = tkinter.messagebox.askquestion("Warning", "Are you sure you want to clear fields?")
    if message == 'yes':
        entryField.delete(0, END)
        entryFieldOutput.delete(0, END)
        pickCurrencyFrom.set("Choose Current: ")
        pickCurrencyTo.set("Choose Desired: ")
        canvas1.itemconfig(currentInfo, text="Currently Selected Info: ")
        canvas1.itemconfig(desireInfo, text="Currently Selected Info: ")
    else:
        return


def currencyConversion():
    """
    Uses API to convert current to desired
    """
    # User input (Numerical) -- Current currency -- Desired Currency
    userInput = entryField.get()
    currentCurrency = pickCurrencyFrom.get()
    desiredCurrency = pickCurrencyTo.get()
    # Checks to make sure user supplied 3 inputs
    if userInput == "":
        tkinter.messagebox.showerror("Error", "Please input a value to be converted.")
    elif currentCurrency == "Choose Current: ":
        tkinter.messagebox.showerror("Error", "Please select current currency type.")
    elif desiredCurrency == "Choose Desired: ":
        tkinter.messagebox.showerror("Error", "Please select desired currency type.")
    else:
        # Sets base currency to current, desired currency and amount to be converted.
        # Clear field before outputting so user does not have to CLEAR
        entryFieldOutput.delete(0, END)
        response = requests.get(
            f'http://v6.exchangerate-api.com/v6/e3d569feabb94a65b8c21c60/pair/{currentCurrency}/{desiredCurrency}/{userInput}')
        data = response.json()
        conversionResult = data['conversion_result']
        conversionResult = float(conversionResult)
        # Output into text field
        entryFieldOutput.insert(0, conversionResult)


if __name__ == '__main__':
    # Create window, title window frame, and set size of the window
    window = Tk()
    window.title("Currency Converter 1.0")
    window.geometry('700x500')
    # Don't allow for resize, Permanent 700x500
    window.resizable(False, False)

    # Add background image
    bg = PhotoImage(file="CurrencyBG1.png")

    # Create Canvas for displaying
    canvas1 = Canvas(window, width=700, height=500)

    # Display image entire window span
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.pack(fill="both", expand=True)

    # ========== Fonts ==========
    # Create greeting/title-screen font (bolded)
    bold_font = tkfont.Font(family="Helvetica", size=26, weight="bold")
    bold_font2 = tkfont.Font(family="Helvetica", size=10, weight="bold")
    font3 = tkfont.Font(family="Helvetica", size=8, weight="bold",)

    # Create option menu for drop down
    dropDownOptions = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'HKD', 'NZD']

    pickCurrencyFrom = StringVar(window)
    pickCurrencyTo = StringVar(window)
    # Set initial menu text and add options to dropdown
    drop = OptionMenu(window, pickCurrencyFrom, *dropDownOptions, command=selectedFrom)
    drop2 = OptionMenu(window, pickCurrencyTo, *dropDownOptions, command=selectedTo)
    pickCurrencyFrom.set("Choose Current: ")
    pickCurrencyTo.set("Choose Desired: ")

    # Input title/greeting on screen
    greetText = canvas1.create_text(350, 50, text=" Welcome to the Currency Converter! ", fill="black", font=bold_font)
    # Create rectangle around title/greeting
    greetWhiteBox = canvas1.create_rectangle(canvas1.bbox(greetText), fill="white")

    # Create rectangle for inputs from WIKISCRAPER
    # Size; x = 300 y = 175
    # Current
    currentInfo = StringVar(window)
    currentInfo = canvas1.create_text(165, 375, width=250, text=" Currently selected info: ", fill="black",
                                      font=bold_font2)

    # Desired
    desireInfo = StringVar(window)
    desireInfo = canvas1.create_text(510, 375, width=250, text=" Desired info: ", fill="black", font=bold_font2)

    # Send the background color to the back and bring the text to the front
    canvas1.tag_lower(greetWhiteBox, greetText)

    # Input Instructions
    bgText = canvas1.create_text(530, 145, text=" Instructions:  \n"
                                                " 1. Input current currency amount  \n"
                                                " 2. Choose current currency via dropdown  \n"
                                                " 3. Choose desired currency via dropdown  \n"
                                                " 4. Press convert button ",
                                 font=bold_font2)

    # Create rectangle in white around the text for the instructions
    textWhiteBox = canvas1.create_rectangle(canvas1.bbox(bgText), fill="white")
    # Send the background color to the back and bring the text to the front
    canvas1.tag_lower(textWhiteBox, bgText)

    # Create Buttons/Inputs/dropdowns
    # Convert button
    convertButton = Button(window, text="Convert", command=currencyConversion)
    clearButton = Button(window, text="Clear", command=clearValues)

    # Entry fields
    entryField = Entry(window, width=20, bd=5, justify=RIGHT)
    entryFieldOutput = Entry(window, width=20, bd=5, justify=RIGHT)
    # Grey out (Disable) output field

    # ========== Display Buttons ==========
    # Add convert button
    convertButton_canvas = canvas1.create_window(315, 225, anchor="nw", window=convertButton)
    # Add clear button
    clearButton_canvas = canvas1.create_window(322, 255, anchor="nw", window=clearButton)
    # Add entry fields
    canvas1.create_window(100, 225, anchor="nw", window=entryField)
    canvas1.create_window(450, 225, anchor="nw", window=entryFieldOutput)
    # Add drop down menus
    canvas1.create_window(100, 255, anchor="nw", window=drop, width=134)
    canvas1.create_window(450, 255, anchor="nw", window=drop2, width=134)

    # mainloop
    window.mainloop()
