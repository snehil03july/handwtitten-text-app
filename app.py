import streamlit as st
import requests
from PIL import Image
from io import BytesIO

def app():
    st.title("Image to Text Extractor")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the selected image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # Extract text button
        if st.button("Extract Text"):
            # Perform OCR on the uploaded image
            text = extract_text(uploaded_file)

            # Display the extracted text
            st.subheader("Extracted Text:")
            st.text(text)

def extract_text(image_file):
    # API endpoint for handwriting OCR
    api_url = "https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/"

    # API headers
    headers = {
        "content-type": "multipart/form-data",
        "x-rapidapi-host": "pen-to-print-handwriting-ocr.p.rapidapi.com",
        "x-rapidapi-key": "913cc6411fmsh545157806af22e3p15b2a6jsn6a3e0c354dd5",  # Replace with your RapidAPI key
    }

    # Prepare image data
    img_bytes = image_file.read()
    img_data = BytesIO(img_bytes)
    img = Image.open(img_data)

    # Send image to OCR API
    files = {"srcImg": (image_file.name, img_bytes)}
    params = {"Session": "string"}

    response = requests.post(api_url, headers=headers, files=files, data=params)

    # Parse response
    if response.status_code == 200:
        return response.json().get("value", "")
    else:
        return "Error: OCR failed."

# Run the Streamlit app
if __name__ == "__main__":
    app()
