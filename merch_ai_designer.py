import openai
import streamlit as st
from getpass import getpass
from IPython.display import Image, display

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

st.title("Merch AI Designer: Revolutionizing Merchandise Creation")
st.sidebar.title("Describe your Merchandise")

image_description = st.sidebar.text_input("Describe the image you'd like to generate:")
merch_type = st.sidebar.selectbox("Choose your merchandise type:", ["T-Shirt", "Mug", "Poster", "Tote Bag", "Sticker"])

submit_button = st.sidebar.button("Generate Design")

# Generate the design when the button is pressed
if submit_button and image_description:
    try:
        # Create the image using OpenAI's image generation API
        response = openai.Image.create(
            prompt=image_description,
            n=1,  
            size="1024x1024"
        )
        image_url = response['data'][0]['url'] 

        # Display the image and the merchandise type
        st.image(image_url, caption=f'Your Custom {merch_type}')

    except Exception as e:
        # Display an error message if something goes wrong
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter an image description and press the 'Generate Design' button.")
