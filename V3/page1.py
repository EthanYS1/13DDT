from tkinter import *
from PIL import Image, ImageTk
import func as func



def open_page1():
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize("500","800")
    root.maxsize("500","800")
    
    BG= Label(root, bg="#61143a")
    BG.place(x=0,y=0,width=500,height=800)
    
    func.listing(root, 50, "Images\Rat.png", "Wicked Pack", "Ingredients:Chicken, Bread, Potatoes", "Golden crispy chicken fired in olive oil. ", "$20.00", "item1")

    func.listing(root,325, "Images\Turty.png", "Wicked Wings 8pc", "Ingredients: Chicken, Bread, herbs", "8 Pack signiture Spicy Wings", "$18.00", "item2")
