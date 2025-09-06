# Fashion MNIST Image Classifier

A simple web app for classifying fashion item images using a quantized neural network trained on the Fashion MNIST dataset. Built with Streamlit and TensorFlow Lite.

## Features
- Upload any image of a fashion item
- Automatic grayscale conversion and resizing
- Predicts one of 10 Fashion MNIST classes
- Displays prediction and class probabilities

## Demo
![Demo Screenshot](demo_screenshot.png)

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fashion-mnist-classifier.git
cd fashion-mnist-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add the model file
Place your `fashion_mnist_model_quantized.tflite` file in the project directory.

### 4. Run the app
```bash
streamlit run app.py
```

## Deployment
For Streamlit Community Cloud:
- Push `app.py`, `requirements.txt`, and your model file to a public GitHub repository.
- Connect the repo to Streamlit Cloud and deploy—no Dockerfile needed!

## File Structure
```
├── app.py
├── requirements.txt
├── fashion_mnist_model_quantized.tflite
└── README.md
```

## Model
The app uses a quantized TensorFlow Lite model trained on the Fashion MNIST dataset. You can retrain or quantize your own model if needed.

## License
This project is licensed under the MIT License.

---

