

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="english", dest="urdu"):
    trans = Translator()
    trans1 = trans.translate(text, src=src.lower(), dest=dest.lower())
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='#f0f4f8')  # Soft light background

# Header Label with Smaller Name Font Size
lab_txt = Label(root, text="Translator by Awais Tanveer", font=("Arial", 20, "bold"), bg='#3a7bd5', fg='white')
lab_txt.place(x=50, y=20, height=50, width=400)

# Main Frame
frame = Frame(root, bg='#f0f4f8')
frame.place(x=0, y=100, width=500, height=600)

# Source Text Label
lab_txt = Label(frame, text="Source Text", font=("Arial", 16, "bold"), fg="#3a7bd5", bg="#f0f4f8")
lab_txt.place(x=100, y=0, height=20, width=300)

# Source Text Box
sor_txt = Text(frame, font=("Arial", 14), wrap=WORD, bd=2, relief=SOLID, fg="#333333", bg="#ffffff")
sor_txt.place(x=10, y=30, height=150, width=480)

# Language Options
list_text = list(LANGUAGES.values())

# Source Language Combobox
comb_sor = ttk.Combobox(frame, value=list_text, font=("Arial", 12))
comb_sor.place(x=10, y=200, height=40, width=150)
comb_sor.set("english")

# Translate Button
button_change = Button(frame, text="TRANSLATE", font=("Arial", 12, "bold"), relief=RAISED, bg="#3a7bd5", fg="white", command=data)
button_change.place(x=170, y=200, height=40, width=150)

# Destination Language Combobox
comb_dest = ttk.Combobox(frame, value=list_text, font=("Arial", 12))
comb_dest.place(x=330, y=200, height=40, width=150)
comb_dest.set("urdu")

# Destination Text Label
lab_txt = Label(frame, text="Destination Text", font=("Arial", 16, "bold"), fg="#3a7bd5", bg="#f0f4f8")
lab_txt.place(x=100, y=260, height=20, width=300)

# Destination Text Box
dest_txt = Text(frame, font=("Arial", 14), wrap=WORD, bd=2, relief=SOLID, fg="#333333", bg="#ffffff")
dest_txt.place(x=10, y=290, height=150, width=480)

root.mainloop()