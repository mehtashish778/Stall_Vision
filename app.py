import streamlit as st
import tempfile
import os
import shutil
import re

# Import the function to process the video
from model.models import gen_frames

# Page configuration
st.set_page_config(
    page_title="Stall Vision",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #000000; /* Set the background color to black */
        color: white; /* Set the text color to white for better contrast */
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


# Title and Description
st.title("🎥 Stall Vision")
st.subheader("Analyze and Gain Insights from Your Store and Marketing Stall Videos")

st.markdown("""
This application helps you process and analyze videos from your store or marketing stalls, 
providing valuable insights similar to Amazon Rekognition. 
Upload a video to get started and discover the analytics!
""")

# File uploader widget
uploaded_file = st.file_uploader("📂 Upload a video file", type=["mp4", "avi", "mov"])

# Analyze button
analyze_button = st.button("🔍 Analyze Video")

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_.]', '_', filename)

if uploaded_file is not None and analyze_button:
    tmpdir = tempfile.mkdtemp()
    try:
        # Sanitize the file name
        sanitized_filename = sanitize_filename(uploaded_file.name)
        
        # Define the path to save the uploaded video file
        video_path = os.path.join(tmpdir, sanitized_filename)

        # Save the uploaded file to the defined path
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(uploaded_file, buffer)

        # Process the video and get analysis results
        st.info("Processing video... This might take a few moments.")
        count_list, track_durations = gen_frames(video_path)

        # Display the analysis results
        st.success("Video processing complete!")
        st.write("### Analysis Results:")
        st.write("**Count List:**", count_list)
        st.write("**Track Durations:**", track_durations)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
    finally:
        # Clean up temporary directory
        shutil.rmtree(tmpdir)

# Add a sidebar with additional information
st.sidebar.title("About This App")
st.sidebar.info("""
This Video Processing App is designed to provide video analytics for stores and marketing stalls. 
Upload a video, and the app will analyze it to give you insights such as people count and track durations.
""")

st.sidebar.title("How to Use")
st.sidebar.markdown("""
1. **Upload a Video:** Click on 'Browse files' to upload your video.
2. **Analyze the Video:** Click on 'Analyze Video' to start the processing.
3. **View Results:** Check the results displayed on the main page.
""")



