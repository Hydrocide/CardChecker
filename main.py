"""
Luhns
16-11-2023

Andrew Kotyck

"""

from tkinter import Frame, Label, Text, Button, Tk, TOP, BOTTOM, LEFT, RIGHT, END, X, Y, RIDGE, GROOVE
from guicolours import *
from luhns import luhnsalgorithm




class OnlineHasten:

    ################## TOP BAR VARIABLES ##################
    #create window
    window = Tk(className="Card Checker")
    
    topbarcolour = green
    #Top bar Frame
    top_bar = Frame(
        master=window, 
        bg=topbarcolour
        )
    #Top bar Label
    title_lbl = Label(
        master=top_bar, 
        text='Card Checker', 
        font='Montserrat 16', 
        bg=topbarcolour, 
        fg='white', 
        padx=5
        )
    
    ################## MID BAR SECTION ##################
    mid_section = Frame(
        master=window, 
        bg=grey
        )
    # BODY FRAME
    body_frm = Frame(
        master=mid_section, 
        bg=lightgrey, 
        padx=5, 
        pady=5
        )
    
    ################## PANEL SECTION ##################
    toppanel_frm = Frame(
        master=body_frm, 
        bg=lightgrey,
        #bg='green', 
        padx=5, 
        pady=5,
        relief=GROOVE
        )
    
    ############ cardcheck ############
    cardcheck_frm = Frame(
        master=toppanel_frm, 
        bg=lightgrey,
        #bg='blue', 
        padx=12, 
        pady=5,
        relief=GROOVE
        )
    
    cardcheck_card_frm = Frame(
        master=cardcheck_frm, 
        bg=lightgrey,
        #bg='green', 
        padx=5, 
        pady=0,
        relief=GROOVE
        )
    cardcheck_card_lbl = Label(
        master=cardcheck_card_frm, 
        text='Check Card Number:', 
        bg=lightgrey, 
        width=18, 
        height=1, 
        border=1,
        borderwidth=1,
        relief=RIDGE,
        padx=5,
        pady=3
        )
    
    cardcheck_textbox_frm = Frame(
        master=cardcheck_frm, 
        bg=lightgrey,
        #bg='red', 
        padx=5, 
        pady=0,
        relief=GROOVE
        )
    cardcheck_textbox_tbx = Text(
        master=cardcheck_textbox_frm, 
        #text='', 
        bg=lightgrey, 
        width=24, 
        height=1, 
        border=1,
        borderwidth=1,
        relief=RIDGE,
        padx=5,
        pady=3
        )
    
    ############ PROCESS ############
    process_frm = Frame(
        master=toppanel_frm, 
        bg=lightgrey,
        #bg='blue', 
        padx=12, 
        pady=5,
        relief=GROOVE
        )
    
    processbutton_frm = Frame(
        master=process_frm, 
        bg=lightgrey,
        #bg='green', 
        padx=5, 
        pady=0,
        relief=GROOVE
        )
    
    showfrm_frm = Frame(
        master=process_frm, 
        bg=lightgrey,
        #bg='green', 
        padx=5, 
        pady=0,
        relief=GROOVE
        )
    showfrm_lbl = Label(
        master=showfrm_frm, 
        text='', 
        bg=lightgrey, 
        width=16, 
        height=1, 
        border=1,
        borderwidth=1,
        relief=RIDGE,
        padx=5,
        pady=3
        )
    
    ##################  COMMANDS  ##################
    def getfunc(func):
        def wrapper(*args):
            return lambda : func(*args)
        return wrapper
    
    @getfunc
    def process(textbox: Text, showlabel: Label):
        textraw: str = textbox.get("1.0",END)
        text = (textraw.replace(" ", "")).replace("\n", "")
        output = luhnsalgorithm(text)
        if output:
            showlabel["text"] = "Valid"
            showlabel["fg"] = "Green"
        else:
            showlabel["text"] = "Invalid"
            showlabel["fg"] = "Red"

    ############### BUTTONS ###############
    process_btn = Button(
        master=processbutton_frm, 
        command=process(cardcheck_textbox_tbx, showfrm_lbl),
        background=lightgrey, 
        fg='black', 
        text='Process',
        relief=RIDGE, 
        width= 30, 
        height= 1,
        border=1, 
        borderwidth=1,
        padx=5
        )


    ##################  PACKING  ##################
    def generatewindow(self) -> None:
        self.window.geometry("700x250")
        self.window.configure(bg="#FFFFFF")
        self.window.minsize(width=700, height=250)

    def packcontainer(self) -> None:
        self.title_lbl.pack(side=TOP)
        self.top_bar.pack(side=TOP, fill=X)
        self.body_frm.pack(side=TOP, padx=25, pady=25)
        self.mid_section.pack(side=LEFT, fill='both', expand=True)


    def packmainitems(self) -> None:
        self.toppanel_frm.pack(side=TOP)
        self.packcardcheck()
        self.packprocess()

    def packbuttons(self) -> None:
        self.process_btn.pack()
        
    
    def packcardcheck(self) -> None:
        self.cardcheck_frm.pack(side=TOP)
        self.cardcheck_card_frm.pack(side=LEFT)
        self.cardcheck_textbox_frm.pack(side=RIGHT)
        self.cardcheck_card_lbl.pack()
        self.cardcheck_textbox_tbx.pack()

    def packprocess(self) -> None:
        self.process_frm.pack(side=TOP)
        self.processbutton_frm.pack(side=LEFT)
        self.showfrm_frm.pack(side=RIGHT)
        self.showfrm_lbl.pack()
        
    
    def __init__(self) -> None:
        self.generatewindow()
        self.packcontainer()
        self.packmainitems()
        self.packbuttons()

        self.window.mainloop()

if __name__ == "__main__":
    # pyinstaller --onefile --noconsole main.py
    print("<<< Starting GUI >>>")
    gui = OnlineHasten()