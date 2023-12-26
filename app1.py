import streamlit as st
import easyocr
import io
from PIL import Image
import tempfile

def app():
    #st.title("Image to Text Extractor")



    st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

    page_bg_img = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
            body {
                background-color: #add8e6; /* Set your desired background color code */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

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
    # Convert the uploaded file to bytes
    image_bytes = image_file.read()

    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))

    # Save the PIL Image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        image.save(temp_image.name, format="PNG")

    reader = easyocr.Reader(['hi', 'en'])  # This needs to run only once to load the model into memory
    result = reader.readtext(temp_image.name)
    text = ''
    for i in result:
        text += i[1] + ' '

    # Remove the temporary file
    temp_image.close()
    return text

# Run the Streamlit app
if __name__ == "__main__":
    app()