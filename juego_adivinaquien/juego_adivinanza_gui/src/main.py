import tkinter as tk
from tkinter import messagebox
from gui import ArtistGuessingGame

def main():
    root = tk.Tk()
    root.title("Artist Guessing Game")
    app = ArtistGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()