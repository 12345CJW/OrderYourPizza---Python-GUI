## Name: Cheryl Wijaya
# Date: Jun 3, 2025
# Task: Pizza Order Application

from tkinter import *

window = Tk()
window.title("Pizza Order Application")
window.geometry("1200x1000")
window.configure(background = "lightYellow")

# Photo
photo1 = PhotoImage(file = "PizzaIntroduction.gif")
photo1 = photo1.subsample(2, 2)
image_label = Label(window, image = photo1)
image_label.pack(anchor="nw", padx = 50, pady= 30)

#Adding a Title label
title_label = Label(window, text = "Build Your Own Pizzaa!", bg = "green2", fg ="white", font = "arial 30 bold")  
title_label.pack(anchor="w", padx = 180, pady= 0)

# Label to ask customer to pick a size
size_label = Label(window, text = "1. Pick a size (one only): ", bg = "lightyellow", fg ="black", font = "arial 25 bold")
size_label.pack( anchor = "w", padx = 50, pady= 20)

# Photo Size selection
# Load the original image once

photo2 = PhotoImage(file="pizaSize.gif")

# Create resized versions and store them in variables to prevent garbage collection
small_pizza_img = photo2.subsample(9, 9)
medium_pizza_img = photo2.subsample(7, 7)
large_pizza_img = photo2.subsample(5, 5)

size_frame = Frame(window, bg="white")
size_frame.pack(anchor = "w", padx = 50, pady=0)

# Small Pizza
small_frame = Frame(size_frame, bg="white")
small_frame.pack(side=LEFT, padx=50)

image_label1 = Label(small_frame, image=small_pizza_img, bg="white")
image_label1.pack()

var = StringVar()
size_check_button1 = Radiobutton(small_frame, text="Small", variable=var, fg ="black",value = "Small", bg="white", font = "arial 12 bold")
size_check_button1.pack(pady=2)

# Medium Pizza
medium_frame = Frame(size_frame, bg="white")
medium_frame.pack(side=LEFT, padx=50)

image_label2 = Label(medium_frame, image=medium_pizza_img, bg="white")
image_label2.pack()

size_check_button2 = Radiobutton(medium_frame, text="Medium", variable=var, value = "Medium", fg ="black",bg="white", font = "arial 12 bold")
size_check_button2.pack(pady=2)

# Large Pizza
large_frame = Frame(size_frame, bg="white")
large_frame.pack(side=LEFT, padx=50)

image_label3 = Label(large_frame, image=large_pizza_img, bg="white")
image_label3.pack()

size_check_button3 = Radiobutton(large_frame, text="Large", variable=var, value = "Large", fg ="black", bg="white", font = "arial 12 bold")
size_check_button3.pack(pady=2)

crust_title = Label(window, text = "2. Select the crust: ", bg = "lightyellow", fg ="black", font = "arial 25 bold")
crust_title.pack(anchor = "w", padx = 50, pady = 0)

# Create a frame to hold crust options side by side
crust_frame = Frame(window, bg="white")
crust_frame.pack(anchor="w", padx=50, pady=10)

# Crust 1
crust = StringVar()
crust_type1 = Radiobutton(crust_frame, text="Thin crust", variable=crust, value = "Thin_crust", fg ="black",font="arial 13 bold", bg="white")
crust_type1.pack(side=LEFT, padx=50)

# Crust 2
crust_type2 = Radiobutton(crust_frame, text="Hand Tossed", variable=crust, value = "Hand Tossed", fg ="black",font="arial 13 bold", bg="white")
crust_type2.pack(side=LEFT, padx=50)

# Create a frame to hold crust options side by side
crust_frame = Frame(window, bg="white")
crust_frame.pack(anchor="w", padx=50, pady=10)

# Crust 3
crust_type3 = Radiobutton(crust_frame, text="Deep-Dish", variable=crust, value = "Deep-Dish", fg ="black",font="arial 13 bold", bg="white")
crust_type3.pack(side=LEFT, padx=50)

# Crust 4
crust_type4 = Radiobutton(crust_frame, text="Brooklyn Style", variable=crust, value = "Brooklyn Style", fg ="black",font="arial 13 bold", bg="white")
crust_type4.pack(side=LEFT, padx=50)

# Select Toppings

topping_title = Label(window, text = "3. Choose the toppings: ", bg = "lightyellow", fg = "black", font = "arial 25 bold")
topping_title.pack(anchor = "w", padx = 50, pady = 0)

topping_frame = Frame(window, bg = "white")
topping_frame.pack(anchor = "w", padx = 50, pady = 10)

# Topping 1
topping1 = IntVar()
first_topping = Checkbutton(topping_frame, text = "Pepperoni", variable = topping1, bg = "white", fg ="black",font = "ariel 13 bold")
first_topping.pack(side = LEFT, padx = 50)

# Topping 2
topping2 = IntVar()
second_topping = Checkbutton(topping_frame, text = "Mushroom", variable = topping2, bg = "white", fg ="black",font = "ariel 13 bold")
second_topping.pack(side = LEFT, padx = 50)

# Next line topping
topping_frame = Frame(window, bg = "white")
topping_frame.pack(anchor = "w", padx =  50, pady = 0)

# Topping 3
topping3 = IntVar()
third_topping = Checkbutton(topping_frame, text = "Sausage", variable = topping3, bg = "white", fg ="black",font = "ariel 13 bold")
third_topping.pack(side = LEFT, padx = 50)

# Topping 4
topping4 = IntVar()
fourth_topping = Checkbutton(topping_frame, text = "Onions", variable = topping4, bg = "white", fg ="black",font = "ariel 13 bold")
fourth_topping.pack(side = LEFT, padx = 60)

# Selection Confirmation

top_right_frame = Frame(window, bg="white")
top_right_frame.pack(fill="x", anchor="n")  


# Confirmation Title
confirmation_title = Label(window, text="4. Confirm your selection:", bg = "lightyellow", fg ="black",font="arial 25 bold")
confirmation_title.place(x=900, y=30)

# Ask for information Title
information_title = Label(window, text="Enter your information:", bg="white", fg="black", font="arial 15 bold")
information_title.place(x=900, y=80)

# Frame to hold name label 
name_frame = Frame(window, bg="white")
name_frame.place(x=900, y=120)

name_label = Label(name_frame, text="Enter your name:", bg="white", fg="black", font="arial 12 bold")
name_label.pack(side=LEFT)

name_entry = Entry(name_frame, width=20, bg="white", fg ="black")
name_entry.pack(side=LEFT)

# Frame to hold telephone label 
telephone_frame = Frame(window, bg="white")
telephone_frame.place(x=900, y=170)

telephone_label = Label(telephone_frame, text="Enter your number:", bg="white", fg="black", font="arial 12 bold")
telephone_label.pack(side=LEFT)

telephone_entry = Entry(telephone_frame, width=20, bg="white", fg ="black")
telephone_entry.pack(side=LEFT)

# Receipt Title
receipt_title = Label(window, text="Your Receipt", bg = "lightyellow", fg = "black", font="arial 25 bold")
receipt_title.place(x=1050, y=240)

# Adding Text Area/ Receipt
output = Text(window, width = 40, height = 25, bg = "lightgreen", fg = "black", font = "arial 15")
output.place(x=950, y=280)


#function that calculates the total cost, total tax, appends toppings to a list, and finally output the inputs into a text box. 
#no parameter 
#no return
def click():
    #initialize total
    total= 0.0
    
    #create a toppings list to track toppings
    toppings = []
    if topping1.get()  ==1:
        toppings.append("Pepperoni")
    if topping2.get()  ==1:
        toppings.append("Mushroom")
    if topping3.get() ==1:
        toppings.append("Sausage")
    if topping4.get() ==1:
        toppings.append("Onions")
        
    #for every additional topping, add $1.25
    #initialize our final topping_string with cheese because every pizza has cheese
    
    topping_string = "Cheese "
    for i in range(len(toppings)):
        total = total + 1.25
        topping_string = topping_string + toppings[i] + " "
     
    #get the crust type from radio button
    crust_type = crust.get()
    
    #get the size from radio button
    size_type = var.get()
    
    #calculate total depending on size
    if size_type == "Small":
        total = total + 10.99
    elif size_type == "Medium":
        total = total + 12.99
    elif size_type == "Large":
        total = total +14.99
        
    #calculate with 8.75 percent tax
    tax = total * 0.0875
    total = tax + total
    
    #get our values from our inputs
    name = name_entry.get()
    phone = telephone_entry.get()
    
    #display the outputs
    output.insert(END, "Your name: " + name +"\n")
    output.insert(END, "Your phone number: "+phone+"\n")
    output.insert(END, "Your order: "+ size_type +" Pizza\n")
    output.insert(END, "Crust Type: "+ crust_type +"\n")
    output.insert(END, "Toppings: "+ topping_string +"\n")
    output.insert(END, f"Tax: ${tax :.2f}\n")
    output.insert(END, f"Your Final Cost is: ${total :.2f}")

#function that resets the total, the toppings list, the topping_string, the name input, the phone input, and deletes the output
#no parameter 
#no return
def reset():
    total = 0.0
    toppings = []
    topping_string = ""
    name = ""
    phone = ""
    output.delete("1.0", END)


# Submit and Reset Buttons
button_frame = Frame(window, bg="lightyellow")
button_frame.place(x=1000, y=800)
    
submit_button = Button(button_frame, text="Submit", font="arial 12 bold", bg="green", fg="black", padx=20, command=click)
submit_button.pack(side=LEFT, padx=10)
    
reset_button = Button(button_frame, text="Reset", font="arial 12 bold", bg="red", fg="black", padx=20, command = reset)
reset_button.pack(side=LEFT, padx=10)

window.mainloop()
