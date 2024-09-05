import random
import tkinter as tk
from tkinter import filedialog

print ("Select a file to randomize:")
def select_file():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    return file_path

def randomize_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()

    random.shuffle(questions)

    for i, question in enumerate(questions, 1):
        print(f"{i}) {question.strip()}")

 
if __name__ == "__main__":
    file_path = select_file()
    if file_path:
        randomize_questions(file_path)
    else:
        print("No file selected.")
