import openai
import streamlit as st
import os

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Set the OpenAI API key
openai.api_key = api_key

st.title("Merch AI Designer: Revolutionizing Merchandise Creation")
st.sidebar.title("Describe your Merchandise")

image_description = st.sidebar.text_input("Describe the image you'd like to generate:")
merch_type = st.sidebar.selectbox("Choose your merchandise type:", ["T-Shirt", "Mug", "Poster", "Tote Bag", "Sticker"])
submit_button = st.sidebar.button("Generate Design")

# Function to generate merch design
def generate_merch_design(description_input, merch_type):
    try:
        # Create a prompt for generating the merchandise with the design
        prompt = f"For this specific merch item: {merch_type.lower()}, please create a design based on the following description: {description_input}."
        
        # Create the image using OpenAI's image generation API, specifying the model
        esponse = client.images.generate(
            model="dall-e",  # Replace "dall-e" with the latest model name if needed
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
        generated_image_url = generate_merch_design(image_description, merch_type)

        if "An error occurred" in generated_image_url:
            st.error(generated_image_url)  # Display error if there is one
        else:
            # Display the generated image
            st.image(generated_image_url, caption=f'Your Custom {merch_type}')
    else:
        st.write("Please enter an image description.")
