# Video Processing App

This project is a video processing application that provides video analytics for stores and marketing stalls. It is inspired by Amazon Rekognition and built using Streamlit, YOLOv5, and DeepSort for object detection and tracking.
**Hugginface Space**- https://huggingface.co/spaces/alphamike/StallVision

## Features

- Upload and analyze video files in various formats (e.g., MP4, AVI, MOV)
- Perform object detection and tracking using YOLOv5 and DeepSort
- Display analysis results including object count and tracking duration
- Visualize results with interactive maps and graphs

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/videoprocessingapp.git
    ```

2. Change to the project directory:
    ```bash
    cd videoprocessingapp
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`

3. Upload a video file and click the "Analyze Video" button to see the results.






## Technologies Used

- Python
- Streamlit
- OpenCV
- YOLOv5
- DeepSort

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [YOLOv5](https://github.com/ultralytics/yolov5)
- [DeepSort](https://github.com/nwojke/deep_sort)
- [Streamlit](https://www.streamlit.io/)
- Inspiration from [Amazon Rekognition](https://aws.amazon.com/rekognition/)

