from tkinter import *
from PIL import Image, ImageTk

root=Tk()

button_size=(100, 100)

# create image object
img1=Image.open("test_images/test_image1.png")
img2=Image.open("test_images/test_image2.png")
img3=Image.open("test_images/test_image3.png")
img4=Image.open("test_images/test_image4.png")
img5=Image.open("test_images/test_image5.png")
img6=Image.open("test_images/test_image6.png")
img7=Image.open("test_images/test_image7.png")
img8=Image.open("test_images/test_image8.png")
img9=Image.open("test_images/test_image9.png")
img10=Image.open("test_images/test_image10.png")
img11=Image.open("test_images/test_image11.png")
img12=Image.open("test_images/test_image12.png")
img13=Image.open("test_images/test_image13.png")
img14=Image.open("test_images/test_image14.png")
img15=Image.open("test_images/test_image15.png")
img16=Image.open("test_images/test_image16.png")

img_list=[img1, img2, img3, img4, img5, img6, img7, img8, 
            img9, img10, img11, img12, img13, img14, img15, img16]

# resize them to fit button size preserving aspect ratio
for i in img_list:
    i.thumbnail(button_size)

# make images Tkinter-compatible
for i in range(len(img_list)):
    img_list[i]=ImageTk.PhotoImage(img_list[i])

# create buttons with images in them
button_list=[]
for i in img_list:
    x=Button(image=i, height=100, width=100)
    button_list.append(x)

# put buttons on grid
for i in range(len(button_list)):
    button_list[i].grid(row=int(i/4), column=i%4)

root.mainloop()