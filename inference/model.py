import cv2
import sys
sys.path.append("")
import darknet

input_path = 
config_file =
data_file =
weights =

network, class_names, class_colors = darknet.load_network(
        config_file,
        data_file,
        weights,
        batch_size=1
    )
width = darknet.network_width(network)
height = darknet.network_height(network)

def darknet_access(path,width,height):
    width = 416
    height = 416
    cap = cv2.VideoCapture(input_path)
    while cap.isOpened():            
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height),
                                interpolation=cv2.INTER_LINEAR)

        img_for_detect = darknet.make_image(width, height, 3)
        darknet.copy_image_from_bytes(img_for_detect, frame_resized.tobytes())
        detections = darknet.detect_image(network, class_names, img_for_detect, thresh=args.thresh)
        darknet.free_image(img_for_detect)
        image = darknet.draw_boxes(detections, frame_resized, class_colors)
        cv2.imshow('video',image)
    
darknet_access(input_path,width,height)