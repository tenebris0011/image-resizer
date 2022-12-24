import tkinter
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("350x150")
extensions = []

def checkbox_event():
    extensions.append(check_var.get())


def resize_images():
    input_dir = input_entry.get()
    output_dir = output_entry.get()
    size = len(os.listdir(input_dir))
    allowed_extension = ['jpg','tiff','jpeg','png']
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image in os.listdir(input_dir):
        if image.split('.')[1] not in allowed_extension:
            continue
        #Create an Image Object from an Image
        im = Image.open(input_dir + "/" + image)
        for percentage in range(25, 100, 25):
            size = percentage/100

            #Get the filename and extension
            file_name = image.split('.')[0]
            file_ext = image.split('.')[1]
            width = round(im.size[0]*size)
            height = round(im.size[1]*size)

            # Create our new file name
            new_file_name = file_name + "_" + str(width) + "x" + str(height) + "." + file_ext
            #Make the new image half the width and half the height of the original image
            resized_im = im.resize((round(im.size[0]*size), round(im.size[1]*size)))
            resized_im.save(output_dir + "/" + new_file_name, format=file_ext)
            resized_im.save(output_dir + "/" + new_file_name + ".webp", format="webp")
    label.configure(text="Image resizing completed.")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, 
                               text="Resize", 
                               command=resize_images, 
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
input_entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Input Folder",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
input_label = customtkinter.CTkLabel(master=app,
                               text="Input Folder",
                               width=120,
                               height=25)
input_label.grid(row=0, column=0)
input_entry.grid(row=1, column=0)

output_entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Output Folder",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
output_label = customtkinter.CTkLabel(master=app,
                               text="Output Folder",
                               width=120,
                               height=25)

output_label.grid(row=3, column=0)
output_entry.grid(row=4, column=0)
button.grid(row=4, column=1)

label = customtkinter.CTkLabel(master=app,
                               text='',
                               width=120,
                               height=25,
                               corner_radius=8)
label.grid(row=1, column=1)

app.mainloop()