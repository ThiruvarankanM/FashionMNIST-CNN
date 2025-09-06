
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(
    page_title="Fashion MNIST Classifier",
    layout="centered",
    initial_sidebar_state="auto",
)

def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def predict_image(interpreter, image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    img = image.convert('L').resize((28, 28))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    return np.argmax(output), output[0]

class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]


st.title('Fashion MNIST Image Classifier')
st.write('Upload a fashion item image.')

uploaded_file = st.file_uploader('Choose an image...', type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image, caption='Uploaded Image', width=120)
    with col2:
        st.write('')
        if st.button('Classify Image', use_container_width=True):
            with st.spinner('Classifying...'):
                interpreter = load_tflite_model('fashion_mnist_model_quantized.tflite')
                pred_class, pred_probs = predict_image(interpreter, image)
                st.success(f'Prediction: **{class_names[pred_class]}**')
                st.write('Class Probabilities:')
                st.bar_chart(pred_probs)
        else:
            st.info('Click the button to classify the image.')
