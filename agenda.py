from tkinter import *
from tkcalendar import Calendar
def agenda():
    print('abrindo agenda...')

    #create the gui object
    tk = Tk()

    #geometry of the GUI Interface
    tk.geometry("400x400")

    #add the Calendar module
    cal = Calendar(tk, selectmode='day',
                   year=2022, month=1,
                   day=11)

    cal.pack(pady=20, fill="both", expand=True)


    #function to grab the selected date
    def grad_date():
        date.config(text="Selected Date is: " + cal.get_date())


    #adding button and label
    Button(tk, text="Get Date",
           command=grad_date).pack(pady=20)

    date = Label(tk, text="")
    date.pack(pady=20)

    #Execute Tkinter
    tk.mainloop()
