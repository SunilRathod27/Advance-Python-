import tkinter
from tkinter import*
window=tkinter.Tk()
window.geometry("1280x720")
window.title("My App")


lbl=Label(window,text=" Enter URL:", fg='black' ,bg='Wheat',font= "Cursive 14 bold")
lbl.place(x=380,y=180)

entry=Entry(window, fg='red' ,bg='Silver',font= "Cursive 14 bold")
entry.place(x=520,y=180)

btn=Button(window,text="Clear" ,fg='black' ,bg='Wheat',font= "Cursive 14 bold")
btn.place(x=760,y=180)

lbl1=Label(window,text="choose path :", fg='black' ,bg='Wheat',font= "Cursive 14 bold")
lbl1.place(x=380,y=280)

entry1=Entry(window, fg='red' ,bg='Silver',font= "Cursive 14 bold")
entry1.place(x=520,y=280)

btn1=Button(window,text="Browse" ,fg='black' ,bg='Wheat',font= "Cursive 14 bold")
btn1.place(x=760,y=280)


btn2=Button(window,text="Download" ,fg='black' ,bg='Wheat',font= "Fantasy 14 bold")
btn2.place(x=570,y=380)

window.mainloop()