# Imports
import tkinter.messagebox
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
import json
import requests


# ========== Functions ==========

def selectedFrom(event):
    """
    Grabs the user's selection from the drop down menu from CURRENT
    """
    return pickCurrencyFrom.get()



def selectedTo(event):
    """
    Grabs the user's selection from the drop down menu from DESIRED
    """
    return pickCurrencyTo.get()



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
    r = 'http://api.currencylayer.com/live?access_key=d4c293de8c4d087826ede4613c44aecc&format=1'

    if userInput == "":
        tkinter.messagebox.showerror("Error", "Please input a value to be converted.")
    elif currentCurrency == "Choose Current: ":
        tkinter.messagebox.showerror("Error", "Please select current currency type.")
    elif desiredCurrency == "Choose Desired: ":
        tkinter.messagebox.showerror("Error", "Please select desired currency type.")
    else:
        data = requests.get(r).json()
        current = currentCurrency.strip() + desiredCurrency.strip()
        userInput = float(userInput)
        cc = data['quotes'][current]
        conversion = cc*userInput
        entryFieldOutput.insert(0, conversion)


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

    # Create option menu for drop down
    dropDownOptions = [
        'USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD',
        'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP',
        'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK',
        'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
        'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD',
        'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR',
        'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
        'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL',
        'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS',
        'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']

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
    # Current
    rectangleCurrent = canvas1.create_rectangle(25,300,325,475, fill='white')
    # Desired
    rectangleDesire = canvas1.create_rectangle(350,300,650,475, fill='white')
    
    # Send the background color to the back and bring the greeting to the front
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
    # entryFieldOutput.config(state="disable")

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
