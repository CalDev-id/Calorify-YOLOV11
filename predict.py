from ultralytics import YOLO
from PIL import Image
import glob
import cv2


model_path = "/home/agil/Documents/Kuliah/IISMA/Ulsan College/UC Kuliah/Practical Cases In The IT Field/Projek besar/Training Segmentation/runs/segment/train5/weights/best.pt"
image_path = glob.glob("image.*")


img = cv2.imread(image_path[0])
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

# Visualize the results
for i, r in enumerate(results):
    # Plot results image
    im_bgr = r.plot()  # BGR-order numpy array
    im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

    # Show results to screen (in supported environments)
    r.show()

    # Save results to disk
    r.save(filename=f"results{i}.jpg")
