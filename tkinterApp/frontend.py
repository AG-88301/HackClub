import backend
from tkinter import *

def add_command():
    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                       year_text.get(), isbn_text.get()))

def main_screen():
    global l1,l2,l3,l4,e1,e2,e3,e4,year_text,isbn_text,list1,title_text,author_text
    window = Tk()
    window.wm_title("App 4")

    l1 = Label(window, text="Title")
    l1.grid(row=0, column=0)

    l2 = Label(window, text="Author")
    l2.grid(row=0, column=2)

    l3 = Label(window, text="Year")
    l3.grid(row=1, column=0)

    l4 = Label(window, text="ISBN")
    l4.grid(row=1, column=2)

    title_text = StringVar()
    e1 = Entry(window, textvariable=title_text)
    e1.grid(row=0, column=1)

    author_text = StringVar()
    e2 = Entry(window, textvariable=author_text)
    e2.grid(row=0, column=3)

    year_text = StringVar()
    e3 = Entry(window, textvariable=year_text)
    e3.grid(row=1, column=1)

    isbn_text = StringVar()
    e4 = Entry(window, textvariable=isbn_text)
    e4.grid(row=1, column=3)

    list1 = Listbox(window, height=6, width=35)
    list1.grid(row=2, column=0, rowspan=6, columnspan=2)

    sb1 = Scrollbar(window)
    sb1.grid(row=2, column=2, rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
  
    b1 = Button(window, text="View all", width=12)
    b1.grid(row=2, column=3)

    b2 = Button(window, text="Search Entry", width=12)
    b2.grid(row=3, column=3)

    b3 = Button(window, text="Add Entry", width=12, command=add_command)
    b3.grid(row=4, column=3)

    b4 = Button(window, text="Update Selected", width=12)
    b4.grid(row=5, column=3)

    b5 = Button(window, text="Delete Selected", width=12)
    b5.grid(row=6, column=3)

    b6 = Button(window, text="Close", width=12, command=window.destroy)
    b6.grid(row=7, column=3)

    window.mainloop()

if __name__ == "__main__":
    main_screen()
