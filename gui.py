import tkinter
from tkinter import*
window = tkinter.Tk()
window.geometry("1280x720")
window.title("My App")

lbl=Label(window,text="Enter First Name:", fg='yellow' ,bg='black',font= "times 14 bold")
lbl.place(x=10,y=18)

entry=Entry(window, fg='red',bg='yellow',font=("times 14 bold"))
entry.place(x=180,y=18)

lbl1=Label(window,text="Enter Last Name:", fg='yellow' ,bg='black',font= "times 14 bold")
lbl1.place(x=10,y=48)

entry1=Entry(window,font= "times 14 bold", fg='red',bg='yellow')
entry1.place(x=180,y=48)

lbl2=Label(window,text="User name:", fg='yellow' ,bg='black',font= "times 14 bold")
lbl2.place(x=10,y=78)

entry2=Entry(window,font= "times 14 bold", fg='red',bg='yellow')
entry2.place(x=180,y=78)

lbl3=Label(window,text="Password:", fg='yellow' ,bg='black',font= "times 14 bold")
lbl3.place(x=10,y=108)

entry3=Entry(window,font= "times 14 bold", fg='red',bg='yellow')
entry3.place(x=180,y=108)

lbl4=Label(window,text="Gender:", fg='yellow' ,bg='black',font= "times 14 bold")
lbl4.place(x=10,y=138)

v = StringVar(window, "1") 
  
btn3=Radiobutton(window, 
              text="Male",
              padx = 10,
              variable=v, 
              value=1)
btn3.place(x=110,y=138)              
btn2=Radiobutton(window, 
              text="Female",
              padx = 10, 
              variable=v, 
              value=2)
btn2.place(x=170,y=138) 
            



# btn=Radiobutton(window,text="Male:")
# btn.place(x=110,y=130)
# btn=Radiobutton(window,text="Female:")
# btn.place(x=110,y=160)



# v = StringVar(window, "1") 
  
# # Dictionary to create multiple buttons 
# values = {"Male" : "1", 
#           "Female" : "2"} 
  
# # Loop is used to create multiple Radiobuttons 
# # rather than creating each button separately 
# for (text, value) in values.items(): 
#     Radiobutton(window, text = text, variable = v, 
#         value = value).pl
  

  
window.mainloop()