import pytesseract
from PIL import Image
import streamlit as st
import re

# Configure the path to the Tesseract executable (if necessary)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("OCR with Hindi and English Text Recognition")

# Image uploader
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Perform OCR
    extracted_text = pytesseract.image_to_string(image, lang='hin+eng')
    st.text_area("Extracted Text", extracted_text)
    
    # Keyword search functionality with highlighting
    keyword = st.text_input("Enter keyword to search")
    if keyword:
        # Use regex to find and highlight the keyword in the text (case-insensitive)
        highlighted_text = re.sub(f'({keyword})', r'**\1**', extracted_text, flags=re.IGNORECASE)
        
        # Display highlighted text with markdown
        st.markdown(f"### Extracted Text with Highlighted Keyword:")
        st.markdown(highlighted_text)
        
        # Check if the keyword was found
        if keyword.lower() in extracted_text.lower():
            st.write(f'Keyword "{keyword}" found and highlighted!')
        else:
            st.write(f'Keyword "{keyword}" not found.')
