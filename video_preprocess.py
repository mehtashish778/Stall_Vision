import cv2

def preprocessing(video_path, fps, res):
    # Open the input video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Error opening video file")

    # Get input video properties
    input_fps = int(cap.get(cv2.CAP_PROP_FPS))
    input_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    input_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Determine output resolution
    output_width = min(input_width, res[0])
    output_height = min(input_height, res[1])

    # Ensure desired fps is not greater than input fps to avoid division by zero
    if fps > input_fps:
        fps = input_fps

    # Set up the video writer
    output_path = 'processed_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, min(input_fps, fps), (output_width, output_height))

    # Process the video frame by frame
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Only write every nth frame to reduce fps, where n = input_fps / desired_fps
        if frame_count % max(1, input_fps // fps) == 0:
            # Resize the frame if necessary
            if input_width > res[0] or input_height > res[1]:
                frame = cv2.resize(frame, (output_width, output_height))
            out.write(frame)
        
        frame_count += 1

    # Release the video capture and writer objects
    cap.release()
    out.release()

    return output_path
