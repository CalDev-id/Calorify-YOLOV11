from ultralytics import YOLO

model = YOLO("yolo11s.pt")
model.train(data="config.yaml", epochs=1, batch=4, imgsz=640)



# Save the best model
trained_model_path = "runs/detect/train/weights/best.pt"


# Load trained YOLO model
model = YOLO(trained_model_path)

# Export to ONNX format
model.export(format="tflite")  # This creates best.onnx