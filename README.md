# DeepFake_Detector

## Building a deep fake image detection model that is capable of classifying images into two categories Ai-Generated or Real images using TensorFlow

# Problem Definition
* The model is used for the detection of deep fake or AI-generated images that 
  are now widely used for spreading hate speech and fake news.
  
# Project Report
[View My Report](https://github.com/vrmaverick/DeepFake_Detector/blob/main/DeepFake_Report.pdf). This was our third-year Year Project.

# Data
*We are using Kaggle data  uploaded on the drive can be downloaded from the following URL
https://www.kaggle.com/datasets/ericji150/nsf-reu-2023-sd-21
[E. Ji, B. Dong, B. Samanthula, N. Zhou. "2D-FACT: Dual-Domain Fake Image Detection Against Textto-Image Generative Models". MIT Undergraduate Research Technology Conference (URTC 2023).]

* For the Training dataset our project includes 10,000 Fake and 10,000 Real images which can create a bias so our project acknowledges these issues by reducing the number of fake images without affecting the accuracy largely


# Evaluation

* Prediction Probabilities should be more than *90%* which is this project's goal to achieve
* Our model achieved *96%* accuracy on the testing dataset

  # *Resources Referred for transfer learning*
* *Kaggle models* = https://www.kaggle.com/models?tfhub-redirect=true
* *Pytorch hub* = https://pytorch.org/hub/
* *Object detection* = https://www.kaggle.com/models/google/mobilenet-v2/frameworks/tensorFlow2/variations/130-224-classification/versions/1?tfhub-redirect=true
* *Papers with code* = https://paperswithcode.com/
* *Tesla model uses RESNET-50 model* = https://www.youtube.com/watch?v=oBklltKXtDE&t=173s
* *Tensorflow hub* = https://www.tensorflow.org/resources/models-datasets
* *Model-Zoo* = https://www.modelzoo.co/
* *Better model for Transfer Learning* https://www.kaggle.com/models/keras/efficientnetv2
  

# Flask DeepFake Detector Web App 🧠🖼️

In the Flask_Apllication directory of the project, there is a Flask-based web application that uses a deep learning model (`my_model_1.h5`) to classify uploaded images as either **Real** or **AI-generated**. It also applies a watermark based on the prediction.

---

## 🚀 Features

- Upload images for classification.
- Detects if the image is real or AI-generated.
- Adds a watermark label based on prediction.
- Download the watermarked image.
- Fully functional UI with routes like Home, About, Services, Contact, etc.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2.Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Locate appropriate directory (cd Flask_Application)

```bash
flask run
```
<ln>
## 🗂️ Folder Structure
  
```bash
Flask_application/
│
├── static/
│   └── uploads/           # Stores uploaded and watermarked images
│   └── images/            # Optional for static images
│
├── templates/
│   ├── index.html         # Main page
│   ├── uploaded_file.html # After prediction
│   └── ...                # Other HTML files
│
├── app.py                 # Main Flask application
├── my_model_1.h5          # Trained TensorFlow model
└── requirements.txt       # All required packages
New folder/ # Data sample from training dataset
│
├── fake/ # Ai generated or morphed images
|
├── sach/ # Real images
Training/ # Codes and notebook used for training the model
Testing/ # Codes and notebook used for testing the model
Model/ # trained models .h5 and .keras format
Updated.ipynb # A notebook used in training and testing
Deepfake_Detector.ipynb # Initial model trained using this notebook it is the old copy
```

## Contact
* [LinkdIn](https://www.linkedin.com/in/vedant-ranade-683867271/)
* Email : vedantranade2612@gmail.com
* [Portfolio](https://vedant-ranade.netlify.app/)



