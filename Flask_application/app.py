from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
# from tensorflow import load_model
from PIL import Image
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
MODEL_PATH = 'C:\\Users\\vedant\\OneDrive\\Desktop\\Deepfake\\model\\my_model_1.h5'

# Load the pre-trained model
model = new_model = tf.keras.models.load_model(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return "Form submitted successfully!"

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(file_path)
        prediction = process_image(file_path)
        return render_template('index.html', image=file_path, prediction=prediction)
    return render_template('index.html')

def process_image(file_path):
    # Open and preprocess the image
    image = tf.io.read_file(file_path)
    # Example: Resize the image to fit model input size
    image = tf.image.decode_jpeg(image,channels = 3)
    image = tf.image.convert_image_dtype(image,tf.float32)#normalize
    image = tf.image.resize(image,size=[224,224])
    # Example: Convert image to numpy array
    img_array = np.array(image) 
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Example: Make predictions using the loaded model
    predictions = model.predict(img_array)

    # Example: Convert predictions to human-readable format
    # Replace this with your actual post-processing code
    threshold = 0.5

# Categorize the prediction
    if predictions >= threshold:
        prediction_class = 'Real_Image'
    else:
        prediction_class = 'Ai-generated Image'

    prediction_label = f'{prediction_class}'

    return prediction_label
#You require to use a less secured email for the cnnection and sending of email or it womnt happen , google stops the requets so keep thaat kn mind 


def send_email(name_contact, sender_email, phone_contact, message):

    # Set up the SMTP server
    message = "Name: {}\nEmail of Sender: {}\nPhone: {}\nQuery: {}".format(name_contact, sender_email, phone_contact, message)

    try:
        sender = "ai.39.vedant.ranade@gmail.com"
        recipient = "ai.39.vedant.ranade@gmail.com"
        email_message = MIMEText(message)
        email_message["Subject"] = "{} Trying to Contact".format(name_contact)
        email_message["From"] = sender
        email_message["To"] = recipient
        print("Email drafted...")

        # Use your Gmail account and App Password for secure connection
        gmail_user = "your@gmail.com"
        app_password = "your_app_password"

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender,"hosy zgdh uoti hvel")
            server.sendmail(sender, recipient, email_message.as_string())
            print("Email sent...")

    except smtplib.SMTPAuthenticationError:
        print("Email not sent. Authentication failed. Please check the sender's email and App Password.")
    except smtplib.SMTPException as e:
        print("Email not sent due to an SMTP error:", str(e))
    except Exception as e:
        print("Email not sent due to an unexpected error:", str(e))
        
if __name__ == '__main__':
    app.run(debug=True)
