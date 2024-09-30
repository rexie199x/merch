import openai
import streamlit as st
import os

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

st.title("Merch AI Designer: Revolutionizing Merchandise Creation")
st.sidebar.title("Describe your Merchandise")

image_description = st.sidebar.text_input("Describe the image you'd like to generate:")
merch_type = st.sidebar.selectbox("Choose your merchandise type:", ["T-Shirt", "Mug", "Poster", "Tote Bag", "Sticker"])
submit_button = st.sidebar.button("Generate Design")

# Function to generate merch design
def generate_merch_design(description_input, merch_type):
    try:
        # Create a clear prompt for generating the design
        prompt = f"For this specific merch item: {merch_type}, please create a design based on the following description: {description_input}."
        
        # Create the image using OpenAI's image generation API
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        # Return the error message if something goes wrong
        return f"An error occurred: {e}"

# Generate the design when the button is pressed
if submit_button:
    if image_description:
        # Call the function to generate the design
        generated_image = generate_merch_design(image_description, merch_type)

        if "An error occurred" in generated_image:
            st.error(generated_image)  # Display error if there is one
        else:
            # Display the image and the merchandise type
            st.image(generated_image, caption=f'Your Custom {merch_type}')
    else:
        st.write("Please enter an image description.")
