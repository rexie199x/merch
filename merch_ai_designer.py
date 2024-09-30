import openai
import streamlit as st
import os
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

st.title("Merch AI Designer: Revolutionizing Merchandise Creation")
st.sidebar.title("Describe your Merchandise")

image_description = st.sidebar.text_input("Describe the image you'd like to generate:")
merch_type = st.sidebar.selectbox("Choose your merchandise type:", ["T-Shirt", "Mug", "Poster", "Tote Bag", "Sticker"])
submit_button = st.sidebar.button("Generate Design")

# Function to generate merch design
def generate_merch_design(description_input):
    try:
        # Create a prompt for the design
        prompt = f"A clean and professional design featuring: {description_input}."
        
        # Generate the image using OpenAI's image generation API
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

# Function to overlay design onto merchandise template
def overlay_design_on_merch(design_url, merch_type):
    # Load the merchandise template based on the selected merch_type
    if merch_type == "T-Shirt":
        template_path = "templates/tshirt_template.png"  # Example path to T-shirt template
    elif merch_type == "Mug":
        template_path = "templates/mug_template.png"
    # Add other merchandise types as needed

    # Open the merchandise template
    merch_template = Image.open(template_path)
    
    # Download the generated design
    response = requests.get(design_url)
    design = Image.open(BytesIO(response.content))

    # Resize and paste the design onto the template
    design = design.resize((400, 400))  # Resize to fit the merchandise
    merch_template.paste(design, (50, 50), design)  # Adjust position as needed

    # Return the final image with the design
    return merch_template

# Generate the design when the button is pressed
if submit_button:
    if image_description:
        # Call the function to generate the design
        generated_image_url = generate_merch_design(image_description)

        if "An error occurred" in generated_image_url:
            st.error(generated_image_url)  # Display error if there is one
        else:
            # Overlay the design on the selected merchandise template
            final_image = overlay_design_on_merch(generated_image_url, merch_type)

            # Display the final image with the design on the selected merchandise
            st.image(final_image, caption=f'Your Custom {merch_type}')
    else:
        st.write("Please enter an image description.")
