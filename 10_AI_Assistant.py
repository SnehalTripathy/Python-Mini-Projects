from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()
root.title("ROBO 2.O - AI Assistant")
root.geometry("1100x1100")
root.config(bg="#18BADE")


#ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, f"User: {user_val}\n")
    if bot_val != None:
        text.insert(END, f"ROBO 2.O: {bot_val}\n")
    if bot_val == 'ok sir':
        root.destroy()
        
#send function
def send(): 
    send = entry.get()
    bot = action.action(send)
    text.insert(END, f"User: {send}\n")
    if bot != None:
        text.insert(END, f"ROBO 2.O: {bot}\n")
    if bot == 'ok sir':
        root.destroy()
    
#delete function
def del_text():
    text.delete(1.0, END)

#FRAME

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief = "raised")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label = Label(frame, text="ROBO 2.O", font=("Cambria", 20, "bold"), bg="#DE4A18")
text_label.grid(row=0, column=0, padx=20, pady=10)

image = ImageTk.PhotoImage(Image.open("BOT.webp"))
image_label = Label(frame, image=image, bg="#18DE50")
image_label.grid(row=1, column=0, pady=20)

#text widget
text = Text(root, font=(("Cambria", 15)), bg="#18DE50", fg="black")
text.grid(row=2, column=0)
text.place(x=100,y=375, width=375, height=100)

#entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

#buttons
Button1 = Button(root, text="ASK", font=("Cambria", 15, "bold"),pady=16, padx=40, bg="#DE4A18", fg="black", relief=SOLID, borderwidth=3, command=ask)
Button1.place(x=100, y=575)

Button2 = Button(root, text="SEND", font=("Cambria", 15, "bold"),pady=16, padx=40, bg="#DE4A18", fg="black", relief=SOLID, borderwidth=3, command=send)
Button2.place(x=300, y=575)

Button3 = Button(root, text="DELETE", font=("Cambria", 15, "bold"),pady=16, padx=40, bg="#DE4A18", fg="black", relief=SOLID, borderwidth=3, command=del_text)
Button3.place(x=500, y=575)

root.mainloop()
print("ROBO 2.O is closed")
