import openai
import streamlit as st
from getpass import getpass

api_key = getpass("Enter your OpenAI API Key: ")
client = openai.OpenAI(api_key=api_key)

st.title("Merch AI Designer: Revolutionizing Merchandise Creation")
st.sidebar.title("Describe your Merchandise")

image_description = st.sidebar.text_input("Describe the image you'd like to generate:")
merch_type = st.sidebar.selectbox("Choose your merchandise type:", ["T-Shirt", "Mug", "Poster", "Tote Bag", "Sticker"])

submit_button = st.sidebar.button("Generate Design")

if submit_button and image_description:

    try:
        response = openai.Image.create(
            prompt=image_description,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        st.image(image_url, caption=f'Your Custom {merch_type}')

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter an image description and press the 'Generate Design' button.")
