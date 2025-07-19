from tkinter import *
import calendar

def Calendar_see():
    window = Tk()
    window.config(bg="light blue")
    window.title("Calendar")
    window.geometry("600x600")
    get_year = int(year_entry.get())
    window_content = calendar.calendar(get_year)
    year_cal = Label(window, text=window_content, bg="light green", font=("Arial", 15, "bold"))
    year_cal.grid(row=5, column=1, padx=20)
    window.mainloop()

if __name__ == "__main__":
    
    root = Tk()
    root.title("Calendar")
    root.config(bg="light blue")
    root.geometry("300x300")

    name = Label(root, text="Calendar", bg="light green", font=("Arial", 20, "bold"))
    name.grid(row=1, column = 1)
    
    year = Label(root, text="Enter Year", bg="light green", font=("Arial", 15, "bold"))
    year.grid(row=2, column=1)
    
    year_entry = Entry(root, font=("Arial", 15, "bold"))
    year_entry.grid(row=3, column=1)
    
    show_button = Button(root, text="Show Calendar",fg ="red", bg="pink", font=("Arial", 15, "bold"), command=Calendar_see)
    show_button.grid(row=4, column=1)
    
    
    root.mainloop()