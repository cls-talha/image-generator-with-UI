import streamlit as st
from PIL import Image
from stable_diffusion import get_image
st.markdown(
    """
    ---
    ##### Made by Talha with ♥
    """
)
# Title of the app
st.title('ImageGenius Battle: Duel of the Visual Masters')

# Text input

col1, col2 = st.columns(2)
with col1:
    # Display the prompt for user1 and image user1 side by side
    user_input1 = st.text_input('User#1 Prompt :', '')
    col1.write(f"Prompt 1: {user_input1}")
    image1 = Image.open('images/purple_cat.jpg')
    # image1 = get_image(user_input1)
    col1.image(image1, caption='Image 1')

with col2:
    user_input2 = st.text_input('User#2 Prompt :', '')
    # Display the prompt for user2 and image user2 side by side
    col2.write(f"Prompt 2: {user_input2}")
    # image2 = get_image(str(user_input2))
    image2 = Image.open('images/purple_cat.jpg')
    col2.image(image2, caption='Image 2')
