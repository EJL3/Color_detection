from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter
from tkinter import *
from tkinter import messagebox


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def get_colours (image,number_of_colors,show_chart):
    mod_img = cv2.resize(image, (600, 400))
    mod_img = mod_img.reshape(mod_img.shape[0] * mod_img.shape[1], 3)
    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(mod_img)
    cnts = Counter(labels)
    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in cnts.keys()]
    hexC = [RGB2HEX(ordered_colors[i]) for i in cnts.keys()]

    if (show_chart):
        plt.figure(figsize=(8, 6))
        plt.pie(cnts.values(), labels=hexC, colors=hexC)
        plt.show()


def sub(i,n):
    try:
        image = cv2.imread(i)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
        img = get_image(i)
        get_colours(img, n, True)

    except:
        messagebox.showerror("Error", "Not enough colours to show "+str(n)+" slices")
def gui():
    root = Tk()
    root.geometry("600x200+700+400")
    root.resizable(False, False)
    root.title("Colours From Image")

    l = Label(root, text="Enter the path to the image you want to analyse ")
    l.place(x=20, y=20)
    l.config(font=26)

    t = Entry(width=70)
    t.place(x=20, y=50)

    l = Label(root, text="Enter the number of colours to be displayed : ")
    l.place(x=20, y=90)
    l.config(font=26)

    u = Entry(width=10)
    u.place(x=400, y=90)

    b = Button(text="Submit", fg='purple',command=lambda: sub(t.get(), int(u.get())))
    b.place(x=270, y=140)

    v = Label(root, text='𝓑𝔂 𝓡𝓲𝔃𝔀𝓪𝓷 𝓐𝓡')
    v.place(x=400,y=176)
    v.config(font=24)

    root.mainloop()


gui()
