import tensorflow as tf

# Load the TensorFlow model
converter = tf.lite.TFLiteConverter.from_saved_model("yolo11_tf_model")

# Optimize for size (optional)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert and save as TFLite model
tflite_model = converter.convert()

# Save the TFLite model
with open("yolo11.tflite", "wb") as f:
    f.write(tflite_model)

print("Model successfully converted to TensorFlow Lite!")
