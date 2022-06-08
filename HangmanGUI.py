# -*- coding: utf-8 -*-

import tkinter as tk
import random as random

class HangmanGame():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("HangmanGame")
        self.lbl_title = tk.Label(self.window)
        self.lbl_word = tk.Label(self.window)
        self.lbl_remain = tk.Label(self.window)
        self.frame_main = tk.Frame(self.window)
        self.btn_newgame = tk.Button(self.window)
    
    def clear_window(self):
        self.lbl_title.pack_forget()
        self.lbl_word.pack_forget()
        self.lbl_remain.pack_forget()
        self.frame_main.pack_forget()

    def restart(self):
        self.clear_window()
        self.__fill_window()
        self.btn_newgame.pack_forget()

    def __guess_char(self, event):
        if not event.widget["state"] == tk.DISABLED:
            pressed = event.widget["text"]
            guessed = False
            hide_word = ""
            for al in self.word:
                if al == pressed:
                    guessed = True
                    self.dict_inputs += pressed
                if al in self.dict_inputs:
                    hide_word += al
                else:
                    hide_word += '_'
                hide_word += " "
            if not guessed:
                self.attempts -= 1
                self.lbl_remain["text"] = "Remaining attempts: " + str(self.attempts)
            self.lbl_word["text"] = hide_word
            event.widget["state"] = tk.DISABLED
            self.__update_game_status()

    def __update_game_status(self):
        if self.attempts == 0:
            self.lbl_remain["text"] = "You lose. Try again!\nGuessed word was " + self.word
            self.frame_main.pack_forget()
            self.btn_newgame = tk.Button(master=self.window, text="New Game", font=("Arial", 15), command=self.restart)
            self.btn_newgame.pack()
        if len(self.word) == len(self.dict_inputs):
            self.lbl_remain["text"] = "You win!!!"
            self.frame_main.pack_forget()
            self.btn_newgame = tk.Button(master=self.window, text="New Game", font=("Arial", 15), command=self.restart)
            self.btn_newgame.pack()

    def __fill_window(self):
        self.window.geometry('800x300')
        self.window.rowconfigure(0, weight=1, minsize=50)
        self.lbl_title = tk.Label(master=self.window, text="Hangman Game", font=("Arial", 25))
        self.lbl_title.pack(pady=10)
        self.window.rowconfigure(1, weight=1, minsize=50)
        self.window.rowconfigure(2, weight=1, minsize=50)
        self.word = random.choice(self.words_to_guess).upper()
        hide_word = '_ '*len(self.word)
        self.attempts = 10
        self.dict_inputs = []
        self.lbl_word = tk.Label(master=self.window, text=hide_word, font=("Arial", 25))
        self.lbl_word.pack(pady=10)
        self.lbl_remain = tk.Label(master=self.window, text="Remaining attempts: " + str(self.attempts), font=("Arial", 18))
        self.lbl_remain.pack(pady=8)
        self.frame_main = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.frame_main.pack()
        self.__create_keyboard()

    
    def __create_keyboard(self):
        k = 'A'
        for i in range(3, 5):
            self.window.rowconfigure(i, weight=1, minsize=50)
            frame = tk.Frame(master=self.frame_main, relief=tk.RAISED, borderwidth=1)
            frame.pack()
            for j in range(13):
                btn_temp = tk.Button(master=frame, text=k, font=("Arial", 15))
                btn_temp.bind("<Button-1>", self.__guess_char)
                btn_temp.grid(row=i, column=j, padx=5, pady=5)
                k = chr(ord(k) + 1)

    def __load_words(self):
        txt_file = open("words.txt", "r")
        file_content = txt_file.read()

        self.words_to_guess = file_content.split("\n")
        txt_file.close()

    
    def start_game(self):
        self.__load_words()
        self.__fill_window()
        self.window.mainloop()      


hangman = HangmanGame()
hangman.start_game()