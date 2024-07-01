from tkinter import *

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_ans.config(text=f"{km}")

# Setting up the window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Miles input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is equal to label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer answer label
kilometer_ans = Label(text="0")
kilometer_ans.grid(column=1, row=1)

# Kilometer label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate button
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

# Run the main event loop
window.mainloop()
