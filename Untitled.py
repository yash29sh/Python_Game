#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    attempts += 1
    
    # Get the player's guess from the Entry widget
    guess = int(guess_entry.get())
    
    if guess == secret_number:
        result_label.config(text="Congratulations! You guessed it in {} attempts.".format(attempts))
        guess_entry.config(state="disabled", justify="center", bg="lightgray")
        check_button.config(state="disabled")
    elif guess < secret_number:
        result_label.config(text="Too low! Try again.")
    else:
        result_label.config(text="Too high! Try again.")

# Create the main window
window = tk.Tk()
window.title("Guess the Number")

# Create a Label widget for instructions
instructions_label = tk.Label(window, text="Guess a number between 1 and 100:")
instructions_label.pack()

# Create an Entry widget for the player's guess
guess_entry = tk.Entry(window, width=20)
guess_entry.pack()

# Create a Button widget to check the guess
check_button = tk.Button(window, text="Check", command=check_guess)
check_button.pack()

# Create a Label widget for displaying the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()


# In[ ]:




