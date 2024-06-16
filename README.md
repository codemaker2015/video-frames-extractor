# Video Frames Extractor

This Streamlit application allows users to upload a video file and extract frames from the video at a rate of 1 frame per second. The extracted frames are saved as JPEG images and can be downloaded as a ZIP file.

![demo](demos/demo.gif)

## Features

- Upload video files in `mp4`, `avi`, `mov`, or `mkv` formats.
- Extract frames from the video at a rate of 1 frame per second.
- Download the extracted frames as a ZIP file.
- Clean up temporary files after processing.

## Installation

To run this application, you need to have Python installed. You also need to install the required libraries. You can install them using `pip`:

```sh
pip install streamlit opencv-python-headless numpy
```

## Usage
- Clone the repository or download the script.
- Open a terminal in the directory containing the script.
- Run the Streamlit application:
   
```sh
   streamlit run app.py
```
- Open the provided URL in your web browser.
- Upload a video file using the file uploader.
- Wait for the frames to be extracted.
- Download the extracted frames as a ZIP file using the provided download button.

## Code Overview
- `save_frames_from_video(video_path, output_folder)` - This function takes a video file path and an output folder path as input. It reads the video file, extracts frames at a rate of 1 frame per second, and saves them as JPEG images in the output folder.
- `zip_frames(output_folder)` - This function takes an output folder path as input. It creates a ZIP file containing all the JPEG images in the output folder and returns the path to the ZIP file.