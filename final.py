from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pytesseract
from pytesseract import image_to_string
from PIL import Image , ImageTk
pytesseract.pytesseract.tesseract_cmd =(r'C:\Program Files (x86)\Tesseract-OCR\tesseract')

root = Tk(  )

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/chandan/Documents/Python",
                           filetypes =(("Image File", "*.jpg"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    solution(name)
    display(name)
    
    
    
    
    
def solution(name):
    im = Image.open(name)
    exp=image_to_string(im)
    sol=(eval(exp))
    print(sol)
    ques= ttk.Label(root, text ="Your Question : "+exp,foreground="black",font=("Helvetica", 16))
    output = ttk.Label(root, text =
    sol,foreground="green",font=("Helvetica", 16))
    ques.pack()
    output.pack()


def display(name):
    canvas = Canvas(root,width=999,height=999)
    canvas.pack()
    pilImage = Image.open(name)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(400,400,image=image)
    root.mainloop()
    
    
    

    

Title = root.title( "Mental maths")
label = ttk.Label(root, text ="Welcome To Mental Maths!!! Select The Image With Your Question",foreground="red",font=("Helvetica", 16))
label.pack()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())
menu.add_cascade(label = 'File', menu = file)
root.mainloop()