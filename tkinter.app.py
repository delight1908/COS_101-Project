from tkinter import Button, Entry, Label, StringVar, Tk


window = Tk()
#
window.geometry("600x250")
window.title("Igbo Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_Label = Label(window, textvariable=result)
result_Label.pack()

igbo_dict = {
    'Bia': 'come',
    'Mmirri': 'water',
    'Gawa': 'go',
    'Mmanu': 'oil',
    'otutu': 'morning',
    'walli': 'take',
    'ntutu': 'hair',
    'akwa': 'cloth',
    'Awu': 'goat',
    'Nnkita': 'Dog',
    'Nwa': 'child',
    'Anwu': 'sun',
    'Nwoke': 'brother',
    'Bata': 'enter',
    'Biko': 'please',
    'Echi': 'tomorrow',
    'Ashhia': 'market',
    'Okporoko': 'stockfish',
    'Oge': 'time',
    'Eze': 'king',
}


def search(word):
    if word in igbo_dict:
        result.set(igbo_dict[word])
        print(igbo_dict[word])
    else:
        result.set("Not Found")
        print("Not Found")


search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()

# run the application
window.mainloop()
