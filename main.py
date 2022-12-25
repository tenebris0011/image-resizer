import streamlit as st
from PIL import Image
import os
import shutil
import random
import string

def resize_images(uploaded):
    if not os.path.exists('./resized'):
        os.makedirs('./resized')
    file_list = []
    for uploaded_file in uploaded_files:
        file_list.append(uploaded_file.name)
    for image in file_list:
        #Create an Image Object from an Image
        im = Image.open("./images/" + image)
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
            resized_im.save("./resized/" + new_file_name)
            resized_im.save("./resized/" + new_file_name + ".webp", format="webp")
    if not os.path.exists('./output'):
        os.makedirs('./output')
    shutil.make_archive(f"./output/{st.session_state['session_key']}", 'zip', "./resized")
    st.session_state['session_zip_file'] = st.session_state['session_key'] + ".zip"


def save_uploadedfile(uploadedfile):
    if not os.path.exists('./images'):
        os.makedirs('./images')
    with open(os.path.join("./images",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
        if os.path.exists(os.path.join("./images",uploadedfile.name)):
           return str(os.path.join("./images",uploadedfile.name))
    return False

st.title("Image Resizer")
st.caption("Resize and generate webp images for all of your image files.")

if 'session_key' not in st.session_state:
    st.session_state['session_key'] = ''.join(random.choices(string.ascii_lowercase, k=5))
    st.session_state['session_zip_file'] = st.session_state['session_key'] + ".zip"

uploaded_files = st.file_uploader("Choose a image file", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    file_path = save_uploadedfile(uploaded_file)

st.button('Resize', key=None, help=None, on_click=resize_images, args=(uploaded_files,), disabled=False)

if os.path.exists(f"./output/{st.session_state['session_zip_file']}"):
    with open(f"./output/{st.session_state['session_zip_file']}", "rb") as fp:
        btn = st.download_button(
            label="Download Resized Images ZIP",
            data=fp,
            file_name=st.session_state['session_zip_file'],
            mime="application/zip"
        )