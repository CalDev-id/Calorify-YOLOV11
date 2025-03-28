import cv2
import glob
import matplotlib
import matplotlib.pyplot as plt
from ultralytics import YOLO

matplotlib.use("qtagg")


# Load the pre-trained YOLO model
model = YOLO(
    "/home/agil/Documents/Kuliah/IISMA/Ulsan College/UC Kuliah/Practical Cases In The IT Field/Projek besar/Training Segmentation/runs/segment/train5/weights/best.pt"
)

# Evaluate the model on the validation set
# results = model.val(data="config.yaml", imgsz=640)

# List of test images
test_images_dir = "data/test"
test_images = glob.glob(test_images_dir + "*")

# Loop through the test images and make predictions
for image_path in test_images:
    # Run inference
    results = model.predict(image_path, imgsz=640)

    # Visualize the results
    for result in results:
        # Load the original image
        img = cv2.imread(image_path)

        # Draw the predictions on the image
        annotated_img = result.plot()  # This draws the detections on the image

        # Display the image with detections
        plt.imshow(annotated_img)
        plt.axis("off")  # Hide axis
        plt.title(f"Detections for {image_path}")
        plt.show()
