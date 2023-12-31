import streamlit as st
import numpy as np
import cv2
import tensorflow
from tensorflow import keras
from keras.models import load_model
from streamlit_drawable_canvas import st_canvas

# Load the trained CNN model
model = load_model('TASK2/Model.h5')

# Function to preprocess the input image
def preprocess_image(image):
    greyscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    input_image_resized = cv2.resize(greyscale, (28, 28))
    input_reshape = np.reshape(input_image_resized, (1, 28, 28, 1))
    return input_reshape

# Streamlit app title
st.title("Digit Recognition App")

# Create a canvas for drawing
canvas = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=280,
    height=280,
    drawing_mode="freedraw"
)

predict_button = st.button("Predict")

if predict_button:
    # Preprocess the canvas drawing and make a prediction
    preprocessed_image = preprocess_image(canvas.image_data)
    prediction = model.predict(preprocessed_image)
    predicted_class = np.argmax(prediction)

    # Display the prediction result
    st.write(f"Predicted Digit: {predicted_class}")
