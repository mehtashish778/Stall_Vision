import cv2
import torch

from ultralytics import YOLO
from video_preprocess import preprocessing
from deep_sort_realtime.deepsort_tracker import DeepSort


# Load YOLOv5 model and move it to GPU if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('yolov5su.pt').to(device)
tracker = DeepSort(max_age=30, nn_budget=70)

# Function to count people in a frame
def count_people(frame):
    results = model(frame)
    detections = results[0].boxes
    people_count = 0

    # Convert detections to the required format for DeepSort
    deepsort_detections = []
    for det in detections:
        if int(det.cls) == 0:  # Class 0 is 'person' in COCO dataset
            
            
            # Convert [x_min, y_min, x_max, y_max] to [left, top, width, height]
            x_min, y_min, x_max, y_max = det.xyxy[0]
            bbox = [x_min.item(), y_min.item(), (x_max - x_min).item(), (y_max - y_min).item()]
            
            confidence = det.conf
            detection_class = int(det.cls)
            deepsort_detections.append((bbox, confidence, detection_class))
            
            people_count += 1
            
    # Update tracker
    tracks = tracker.update_tracks(deepsort_detections, frame=frame)

    return people_count, frame, tracks


def gen_frames(video_path):
    
    #preprocessing the video
    video_path = preprocessing(video_path,15,(640, 480))
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    count_list = []
    track_durations = {}


    # Loop through video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Count people in the frame
        people_count, frame, tracks = count_people(frame)
        count_list.append(people_count)

        # Track the duration of each object in the frame
        for track in tracks:
            if track.is_confirmed() and track.time_since_update <= 1:
                track_id = track.track_id
                if track_id not in track_durations:
                    track_durations[track_id] = 0
                track_durations[track_id] += 1

    cap.release()
    cv2.destroyAllWindows()
    
    # Print the duration each object stayed in the frame
    
    for track_id, duration in track_durations.items():
        print(f'Track ID: {track_id}, Duration: {duration} frames')
    
    return(count_list, track_durations)