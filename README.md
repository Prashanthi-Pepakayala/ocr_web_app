# ocr_web_app
OCR Web Application
This is a web-based application that performs Optical Character Recognition (OCR) on uploaded images containing both Hindi and English text. It allows users to upload an image, extract the text, and search for keywords within the extracted text.


Features
1.Upload images in .jpg or .png formats.
2.Extracts text from images in both Hindi and English.
3.Search functionality to find specific keywords within the extracted text.


Installation


Prerequisites
1.Python 3.x
2.pip package manager
3.Tesseract OCR installed 


Steps to Install:
1.Clone the Repository:
git clone https://github.com/Prashanthi-Pepakayala/ocr_web_app.git
2.Navigate to the Project Directory:
cd ocr_web_app
3.Install Required Packages:
pip install -r requirements.txt


How to Run the Application Locally
1.Run the app using Streamlit:
streamlit run ocr_app.py
2.Open the app in your browser at http://localhost:8501.


Deployment

Deploy on Streamlit Sharing:
1.Go to Streamlit Sharing.
2.Connect your GitHub repository and select the ocr_app.py as the entry file.
3.Deploy the app and get the live URL for public access.

Usage
1.Upload an Image: Upload a .jpg or .png image containing Hindi and English text.
2.Extract Text: Once uploaded, the extracted text will be displayed.
3.Keyword Search: Enter a keyword, and if it's found in the text, the location will be highlighted.


Deliverables
1.Code Submission:
Python scripts (ocr_app.py) for the OCR processing and search functionality.
2.README File:
This README file explaining the setup, usage, and deployment process.
3.Live Web Application:
The public URL of the deployed app.
4.Extracted Text and Search Output:
Sample output of the extracted text and the result of keyword searches.


Technologies Used
1.Streamlit: Web framework for interactive applications.
2.Tesseract: OCR engine for extracting text from images.
3.Pillow: Image processing library.
4.OpenCV: Preprocessing images for better OCR results.

