#Creates canvas for program
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser



#Creates a window and sizes it
window=Tk()
window.geometry("500x500"
)
window.title('Photo to ASCII Generator')


#Upload function
def upload():
    showinfo(
        title='Disclaimer!',
        message='Upload has been clicked!'
    )


#Creates boundary for the insides of program
frm = ttk.Frame(window)
frm['padding']=(150,150,0,0)
frm.grid(rowspan=2, columnspan=3, sticky=E+W+N+S, pady=5)

#Bottom Frame
btmfrm = ttk.Frame(window)
btmfrm.grid_columnconfigure(0, weight=1)
btmfrm.grid_rowconfigure(0, weight=1)
btmfrm.grid(rowspan=11, columnspan=3, sticky=E+W+N+S, padx=15)

#Inside text of program
ttk.Label(frm, text="Photo to ASCII Generator").grid(column=0, row=0)
ttk.Label(frm, text="by ste, https://github.com/lnterger").grid(column=0, row=1)

ttk.Button(btmfrm, text="Upload Photo", command=upload).grid(column=1, row=3, pady=5)
ttk.Button(btmfrm, text="Quit", command=window.destroy).grid(column=3, row=3, pady=5)

#Program doesn't shut down until window is destroyed by button
window.mainloop()

