#Import tkinter module
import tkinter as tk

#import tkinter.ttk as ttk
import tkinter.ttk as ttk   

# Create the main window
window = tk.Tk()
window.title("Send Me A Poem!")
window.geometry("1920x1080")

frame = ttk.Frame(window, padding="10")
frame2 = ttk.Frame(window, padding="10")
framelabel = ttk.Label(frame, text="v0.5 - A simple GUI to collect poems")
framelabel.pack()

frame2label = ttk.Label(frame2, text="Made with <3 by mso-docs")
frame2label.pack()

frame.pack()
frame2.pack()

# Widget - Classic
greeting = tk.Label(text="Send Me A Poem!", fg="white", bg="black", width=15, height=1)
greeting.config(font=("Comic Sans MS", 64))
greeting.pack()

# Widget - Themed
subtitle = ttk.Label(text="I love poetry! \n")
subtitle.pack()

# Instructions
instructions = ttk.Label(text="Instructions: \n Please enter your first and last name in the fields below.\n Then, type a free verse poem for me. \n \n")
instructions.pack()

# Poem Name Label
PoemLabel = ttk.Label(text="Enter a title for your poem:")
PoemLabel.pack()

# Poem Title Entry
PoemEntry = ttk.Entry(width=50)
PoemEntry.pack()

# Poem Name Button
def print_poem_title():
    title = PoemEntry.get()
    print("Poem Title: " + title)

PoemButton = ttk.Button(text="Submit Poem Title", command=print_poem_title)
PoemButton.pack()

# Label - Classic
Label1 = tk.Label(text="Type your first name below and click the button!")
Label1.pack()

# Entry - Classic
entry1 = tk.Entry(width=30)
entry1.pack()

# Button - Classic
button1 = tk.Button(text="Enter First Name", command=lambda: print("Button Clicked!"))
button1.pack()

#Label - Themed
Label2 = ttk.Label(text="Type your last name below and click the button!")
Label2.pack()

# Entry - Last Name
entry2 = ttk.Entry(width=30)
entry2.pack()  

# Function to collect and print the names
def print_full_name():
    name = entry1.get() 
    last_name = entry2.get()
    print("Poem By: " + name + " " + last_name)

# Button - Themed
button2 = ttk.Button(text="Print Full Name", command=print_full_name)
button2.pack()

# Text widget - Classic (ttk doesn't have Text widget)
text_widget = tk.Text(width=50, height=10, bg="white", fg="black")
text_widget.pack()

#Print Poem
def print_poem():
    poem = text_widget.get("1.0", "end-1c")  # Get text from the Text widget
    if poem:
        print("Poem Submitted: \n" + poem)
    else:
        print("No poem submitted.")
        
# Poem Button - Classic
poem_button = tk.Button(text="Submit Poem", width=10, height=1, bg="lightblue", fg="black", command=print_poem)
poem_button.pack()


# Start the main event loop
window.mainloop()
