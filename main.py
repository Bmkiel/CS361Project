# Imports
import tkinter.messagebox
from tkinter import *
from tkinter import font as tkfont
from PIL import ImageTk, Image
import json
import requests


# ========== Functions ==========
def selected_from(event):
    """
    Grabs the user's selection from the drop down menu from CURRENT
    """
    from_ = pick_currency_from.get()
    # Checks currency selected and outputs accordingly through wikiscraper
    # selected = wiki search term
    # sentences = amount of sentences to return
    if from_ == "USD":
        selected = "UnitedStatesDollar"
        sentences = "1"
    elif from_ == "EUR":
        selected = "European_Currency"
        sentences = "2"
    elif from_ == "JPY":
        selected = "Japan_Currency"
        sentences = "2"
    elif from_ == "GBP":
        selected = "Great_Britain_Pound"
        sentences = "1"
    elif from_ == "AUD":
        selected = "Austrailian_dollar"
        sentences = "2"
    elif from_ == "CAD":
        selected = "Canadian_Dollar"
        sentences = "2"
    elif from_ == "CHF":
        selected = "Swissfranc"
        sentences = "3"
    elif from_ == "HKD":
        selected = "HKD"
        sentences = "2"
    elif from_ == "NZD":
        selected = "NZD"
        sentences = "1"
    # Variables have been set accordingly and now wikiscraper does its job
    entry_field_output.delete(0, END)
    response = requests.get(
        f'https://wiki-scrape-361.herokuapp.com/firstpara/{selected}/{sentences}')
    data = response.json()
    text_info = data['output']
    if from_ == "CHF":
        canvas1.itemconfig(current_info, text=text_info, font=font3)
    else:
        canvas1.itemconfig(current_info, text=text_info, font=bold_font2)


def selected_to(event):
    """
    Grabs the user's selection from the drop down menu from DESIRED
    """
    to_ = pick_currency_to.get()
    # Checks currency and outputs accordingly
    # selected = wiki search term
    # sentences = amount of sentences to return
    if to_ == "USD":
        selected = "UnitedStatesDollar"
        sentences = "1"
    elif to_ == "EUR":
        selected = "European_Currency"
        sentences = "2"
    elif to_ == "JPY":
        selected = "Japan_Currency"
        sentences = "2"
    elif to_ == "GBP":
        selected = "Great_Britain_Pound"
        sentences = "1"
    elif to_ == "AUD":
        selected = "Austrailian_dollar"
        sentences = "2"
    elif to_ == "CAD":
        selected = "Canadian_Dollar"
        sentences = "2"
    elif to_ == "CHF":
        selected = "Swissfranc"
        sentences = "3"
    elif to_ == "HKD":
        selected = "HKD"
        sentences = "2"
    elif to_ == "NZD":
        selected = "NZD"
        sentences = "1"
    # Variables have been set accordingly and now wikiscraper does its job
    entry_field_output.delete(0, END)
    response = requests.get(
        f'https://wiki-scrape-361.herokuapp.com/firstpara/{selected}/{sentences}')
    data = response.json()
    text_info = data['output']
    if to_ == "CHF":
        canvas1.itemconfig(desire_info, text=text_info, font=font3)
    else:
        canvas1.itemconfig(desire_info, text=text_info, font=bold_font2)


def clear_values():
    """
    Used to clear current/desired input fields and current selection of currencies
    No returns
    """
    message = tkinter.messagebox.askquestion("Warning", "Are you sure you want to clear fields?")
    if message == 'yes':
        entry_field.delete(0, END)
        entry_field_output.delete(0, END)
        pick_currency_from.set("Choose Current: ")
        pick_currency_to.set("Choose Desired: ")
        canvas1.itemconfig(current_info, text="Currently Selected Info: ", font=bold_font2)
        canvas1.itemconfig(desire_info, text="Currently Selected Info: ", font=bold_font2)
    else:
        return


def currency_conversion():
    """
    Uses API to convert current to desired
    """
    # User input (Numerical) -- Current currency -- Desired Currency
    user_input = entry_field.get()
    current_currency = pick_currency_from.get()
    desired_currency = pick_currency_to.get()
    # Checks to make sure user supplied 3 inputs
    if user_input == "":
        tkinter.messagebox.showerror("Error", "Please input a value to be converted.")
    elif current_currency == "Choose Current: ":
        tkinter.messagebox.showerror("Error", "Please select current currency type.")
    elif desired_currency == "Choose Desired: ":
        tkinter.messagebox.showerror("Error", "Please select desired currency type.")
    else:
        # Sets base currency to current, desired currency and amount to be converted.
        # Clear field before outputting so user does not have to CLEAR
        entry_field_output.delete(0, END)
        response = requests.get(
            f'http://v6.exchangerate-api.com/v6/e3d569feabb94a65b8c21c60/pair/{current_currency}/{desired_currency}/{user_input}')
        data = response.json()
        conversion_result = data['conversion_result']
        conversion_result = float(conversion_result)
        # Output into text field
        entry_field_output.insert(0, conversion_result)


if __name__ == '__main__':
    # Create window, title window frame, and set size of the window
    window = Tk()
    window.title("Currency Converter 1.1")
    window.geometry('700x500')

    # Create greeting/title-screen font (bolded)
    bold_font = tkfont.Font(family="Helvetica", size=26, weight="bold")
    bold_font2 = tkfont.Font(family="Helvetica", size=10, weight="bold")
    font3 = tkfont.Font(family="Helvetica", size=8, weight="bold", )

    # Don't allow for resize, Permanent 700x500
    window.resizable(False, False)

    # Add background image
    bg = PhotoImage(file="CurrencyBG1.png")

    # Create Canvas for displaying
    canvas1 = Canvas(window, width=700, height=500)

    # Display image entire window span
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.pack(fill="both", expand=True)

    # Create option menu for drop down containing items in the list
    drop_down_options = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'HKD', 'NZD']

    # Sets fields to strings
    pick_currency_from = StringVar(window)
    pick_currency_to = StringVar(window)

    # Add options to dropdown and set initial menu text
    drop = OptionMenu(window, pick_currency_from, *drop_down_options, command=selected_from)
    drop2 = OptionMenu(window, pick_currency_to, *drop_down_options, command=selected_to)
    pick_currency_from.set("Choose Current: ")
    pick_currency_to.set("Choose Desired: ")

    # Input title/greeting on screen
    greet_text = canvas1.create_text(350, 50, text=" Welcome to the Currency Converter! ", fill="black", font=bold_font)
    # Create rectangle around title/greeting
    greet_white_box = canvas1.create_rectangle(canvas1.bbox(greet_text), fill="white")

    # Create area for wikiscraper to output "Current" selected info out
    current_info = StringVar(window)
    current_info = canvas1.create_text(165, 375, width=250, text=" Currently selected info: ", fill="black",
                                       font=bold_font2)

    # Create area for wikiscraper to output "Desired" selected info out
    desire_info = StringVar(window)
    desire_info = canvas1.create_text(510, 375, width=250, text=" Desired info: ", fill="black", font=bold_font2)

    # Send the background color to the back and bring the text to the front for greeting
    canvas1.tag_lower(greet_white_box, greet_text)

    program_instructions = canvas1.create_text(530, 145, text=" Instructions:  \n"
                                                              " 1. Input current currency amount  \n"
                                                              " 2. Choose current currency via dropdown  \n"
                                                              " 3. Choose desired currency via dropdown  \n"
                                                              " 4. Press convert button ",
                                               font=bold_font2)

    # Create rectangle in white around the text for the instructions
    text_white_box = canvas1.create_rectangle(canvas1.bbox(program_instructions), fill="white")

    # Send the background color to the back and bring the text to the front for instructions text
    canvas1.tag_lower(text_white_box, program_instructions)

    convert_button = Button(window, text="Convert", command=currency_conversion)
    clear_button = Button(window, text="Clear", command=clear_values)

    # Entry fields
    entry_field = Entry(window, width=20, bd=5, justify=RIGHT)
    entry_field_output = Entry(window, width=20, bd=5, justify=RIGHT)

    display_convert_button = canvas1.create_window(315, 225, anchor="nw", window=convert_button)

    display_clear_button = canvas1.create_window(322, 255, anchor="nw", window=clear_button)

    # Add entry fields (Current and Desired)
    canvas1.create_window(100, 225, anchor="nw", window=entry_field)
    canvas1.create_window(450, 225, anchor="nw", window=entry_field_output)

    # Add drop down menus (Holds various currencies to convert to and from)
    canvas1.create_window(100, 255, anchor="nw", window=drop, width=134)
    canvas1.create_window(450, 255, anchor="nw", window=drop2, width=134)

    # mainloop
    window.mainloop()
