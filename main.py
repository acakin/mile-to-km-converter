from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

km = Label(text=0)
km.grid(row=1, column=1)

miles_text = Label(text="Miles")
miles_text.grid(row=0, column=2)
km_text = Label(text="Km")
km_text.grid(row=1, column=2)
is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(row=1, column=0)

entry = Entry(width=20)
entry.grid(row=0, column=1)
entry.get()


def mile_to_km():
    km.config(text=float(entry.get())*1.609344)


button = Button(text="Calculate", command=mile_to_km, width=20)
button.grid(row=2, column=1)








window.mainloop()