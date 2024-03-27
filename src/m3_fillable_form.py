import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Form")

label = tk.Label(
    window,
    text="Name",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="Address Line 1",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="Address Line 2",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="City",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="State",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="Zip Code",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="Phone Number",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
label = tk.Label(
    window,
    text="Email Address",
    width = 20,
    background = "MediumPurple1",
   )
label.pack()

entry=tk.Entry(
    window,
    width = 24,
    background = "thistle",
)
entry.pack()
button=tk.Button(
    window,
    text="Submit"
)
button.pack()


window.mainloop()