from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
import pyperclip

# Main window
root = Tk()
root.title("AI Language Translator")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Title
title = Label(
    root,
    text="AI Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0",
    fg="blue"
)
title.pack(pady=10)

# Input text
Label(root, text="Enter Text:", font=("Arial", 12)).pack()

input_text = Text(root, height=8, width=60)
input_text.pack(pady=10)

# Languages
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "Hindi": "hi",
    "German": "de",
    "Spanish": "es"
}

# Source Language
Label(root, text="Source Language").pack()

source_lang = ttk.Combobox(
    root,
    values=list(languages.keys())
)
source_lang.pack()
source_lang.set("English")

# Target Language
Label(root, text="Target Language").pack()

target_lang = ttk.Combobox(
    root,
    values=list(languages.keys())
)
target_lang.pack()
target_lang.set("Urdu")

# Output text
Label(root, text="Translated Text:", font=("Arial", 12)).pack()

output_text = Text(root, height=8, width=60)
output_text.pack(pady=10)

# Translate function
def translate():

    text = input_text.get(1.0, END)

    source = languages[source_lang.get()]
    target = languages[target_lang.get()]

    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    output_text.delete(1.0, END)
    output_text.insert(END, translated)

# Copy function
def copy_text():

    text = output_text.get(1.0, END)
    pyperclip.copy(text)

# Buttons
translate_btn = Button(
    root,
    text="Translate",
    command=translate,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
)
translate_btn.pack(pady=5)

copy_btn = Button(
    root,
    text="Copy Text",
    command=copy_text,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold")
)
copy_btn.pack(pady=5)

# Run app
root.mainloop()