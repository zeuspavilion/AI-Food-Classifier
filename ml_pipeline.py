import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os

print("⏳ Loading MobileNetV2 Model into memory...")
# Load the model once when this module is imported
model = MobileNetV2(weights='imagenet')
print("✅ Model loaded successfully!")

def warmup_model():
    """
    Passes a dummy image through the model to initialize the TensorFlow graph.
    This makes the VERY FIRST user prediction fast instead of freezing the app.
    """
    print("🔥 Warming up the model...")
    dummy_image = np.zeros((1, 224, 224, 3))
    dummy_image = preprocess_input(dummy_image)
    model.predict(dummy_image)
    print("🚀 Model is warmed up and ready for inference!")

# Run the warmup immediately
warmup_model()

def predict_image(img_path):
    """
    Takes an image path, preprocesses it, and returns the top prediction label.
    """
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        preds = model.predict(x)
        results = decode_predictions(preds, top=1)[0]
        
        # results[0] looks like: ('n07259812', 'pizza', 0.9854)
        predicted_label = results[0][1].replace("_", " ").title()
        confidence = float(results[0][2]) # We will use this later for the DB!
        
        return predicted_label
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Unknown Error"