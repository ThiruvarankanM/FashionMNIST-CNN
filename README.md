
# Fashion MNIST Image Classifier

A simple web app for classifying fashion item images using a Convolutional Neural Network (CNN) trained on the Fashion MNIST dataset. Built with Streamlit and TensorFlow.

## Features
- Upload any image of a fashion item
- Automatic grayscale conversion and resizing
- Predicts one of 10 Fashion MNIST classes
- Displays prediction and class probabilities

## Demo
Watch the demo video on YouTube: [Fashion MNIST CNN Web App Demo](https://youtu.be/92-V68D-ilw)

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
Place your `fashion_mnist_model.h5` file in the project directory.

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
├── fashion_mnist_model.h5
├── Fashion_MNIST_Image_Classification_with_CNNs.ipynb
└── README.md
```

## Model
The app uses a standard Keras `.h5` model trained on the Fashion MNIST dataset. You can retrain or update your own model if needed.

## License
This project is licensed under the MIT License.

---

