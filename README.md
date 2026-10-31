# Dance Pose Detection Using YOLO

## About the Project
Dance Pose Detection is a Python-based computer vision project that uses YOLO Pose Estimation and OpenCV to detect human body keypoints in dance videos. It processes the input video and generates an output video with a black background and white dots representing detected body joints.

## Features
- Human pose detection using YOLO.
- Processes dance videos frame by frame.
- Displays detected body keypoints as white dots.
- Generates an output video with a black background.
- Uses OpenCV for video processing.

## Technologies Used
- Python
- YOLO Pose Estimation (Ultralytics)
- OpenCV
- NumPy

## Project Structure
```text
dance_pose_detection/
├── pose_detection.py
├── dance (2).mp4
├── dance_output.mp4
└── README.md
```

## Installation

### 1. Clone the Repository
```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Navigate to the Project Folder
```bash
cd dance_pose_detection
```

### 3. Install Dependencies
```bash
pip install ultralytics opencv-python numpy
```

## How to Run

1. Place your input video in the project folder.
2. Update the video filename in `pose_detection.py` if necessary.
3. Run the following command:

```bash
python pose_detection.py
```

4. After processing, the output video will be saved as `dance_output.mp4`.

## Output
The project generates a video with a black background and white dots representing the detected human body joints.

**Note:** The current implementation displays keypoints as dots and does not draw connecting lines between joints.

## Future Improvements
- Connect body keypoints to create a complete skeleton.
- Improve pose detection accuracy.
- Support multiple people in a video.
- Add real-time pose detection.

## Author
Adiba Anjum

## License
This project is available for educational and learning purposes.
