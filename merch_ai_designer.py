import openai
import streamlit as st
import os

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


st.title("Merch AI Designer: Revolutionizing Merchandise Creation")
st.sidebar.title("Describe your Merchandise")

image_description = st.sidebar.text_input("Describe the image you'd like to generate:")
merch_type = st.sidebar.selectbox("Choose your merchandise type:", ["T-Shirt", "Mug", "Poster", "Tote Bag", "Sticker"])
submit_button = st.sidebar.button("Generate Design")

# Function to generate merch design
        # Create the image using OpenAI's image generation API, specifying the model
response = client.images.generate(
               model="dall-e-3",
               prompt = "For this specific merch item: {merch_type.lower()}, please create a design based on the following description: {description_input}.",
               size="1024x1024",
               quality="standard",
               n=1,
           )
image_url = response.data[0].url
image_url
from IPython.display import Image, display
# Create an Image instance with the URL
image = Image(url=image_url)
# Display the image
display(image)

# Generate the design when the button is pressed
if submit_button:
    if image_description:
        # Call the function to generate the design
        generated_image_url = generate_merch_design(image_description, merch_type)

        if "An error occurred" in generated_image_url:
            st.error(generated_image_url)  # Display error if there is one
        else:
            # Display the generated image
            st.image(generated_image_url, caption=f'Your Custom {merch_type}')
    else:
        st.write("Please enter an image description.")
