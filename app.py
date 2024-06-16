import streamlit as st
import cv2
import numpy as np
from zipfile import ZipFile
import os

def save_frames_from_video(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps  # Duration in seconds
    
    count = 0
    success, frame = cap.read()
    
    while success:
        # Save frame if it's at a whole second mark
        if count % int(fps) == 0:
            second = int(count / fps)
            cv2.imwrite(f"{output_folder}/frame_{second:04d}.jpg", frame)
        success, frame = cap.read()
        count += 1

    cap.release()
    return duration

def zip_frames(output_folder):
    zip_filename = "frames.zip"
    with ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(output_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, output_folder))
    return zip_filename

st.title("Video Frames Extractor")
st.caption("(1 frame per second)")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    video_bytes = uploaded_file.read()
    with open("temp_video.mp4", "wb") as f:
        f.write(video_bytes)

    output_folder = "frames"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    st.text("Extracting frames from the video...")
    duration = save_frames_from_video("temp_video.mp4", output_folder)
    st.text(f"Extracted frames for {int(duration)} seconds of video.")

    zip_filename = zip_frames(output_folder)
    
    with open(zip_filename, "rb") as f:
        st.download_button(
            label="Download Frames as ZIP",
            data=f,
            file_name=zip_filename,
            mime="application/zip"
        )
    
    # Clean up
    os.remove("temp_video.mp4")
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)
    os.rmdir(output_folder)
    os.remove(zip_filename)
