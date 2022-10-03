from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding = 20)
frm.grid()
ttk.Label(frm, text="Escolha seu candidato:  ").grid(column=0, row=0)
ttk.Button(frm, text="sair", command=root.destroy).grid(column=2, row=2)
ttk.Button(frm, text="confirmar", command=root.destroy).grid(column=1, row=2)
ttk.Entry(frm).grid(column=1, row=0)

root.mainloop()

'''
from Tkinter import *
def inc():
 n=int(rotulo.configure("text")[4])+1
 rotulo.configure(text=str(n))

b = Button(text="Incrementa",command=inc)
b.pack()
rotulo = Label(text="0")
rotulo.pack()
mainloop()
'''
