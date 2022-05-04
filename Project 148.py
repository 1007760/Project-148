from tkinter import *
import random
root = Tk()
root.geometry("400x400")
root.title("Picnic List")
item_list = Label(root)
random_number_display = Label(root)
gift_list = ["Bottle", "Tiffin", "ID Card", "Choclates", "Chips", "Tickets", "Hanky"]
item_list["text"] = "Gift list is : " + str(gift_list)

def randomNumber() :
    random_number = random.sample(range(0, 7), 1)
    random_number_display["text"] = "Put item number " + str(random_number) + " in the bag."

btn = Button(root, text = "Gift Number", command = randomNumber)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)
item_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)
random_number_display.place(relx = 0.5, rely = 0.6, anchor = CENTER)
root.mainloop()