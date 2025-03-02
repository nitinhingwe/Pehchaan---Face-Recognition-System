# Pehchaan---Face-Recognition-System
Pehchaan - is our Face Recognition System project for efficient facial attendance.

# Pehchaan - Face Recognition System

![Pehchaan](image.png)

## 📌 About
**Pehchaan** is an AI-powered Face Recognition System designed for efficient facial attendance and authentication. This project integrates **OpenCV**, **Face Recognition**, and **Tkinter** to provide a seamless real-time facial recognition experience with an intuitive user interface.

## 🚀 Features
- 🔍 **Real-time Face Detection & Recognition**
- 🎭 **Automated Attendance Logging**
- 🔑 **Admin Authentication for Secure Access**
- 🖥 **Graphical User Interface (GUI) using Tkinter**
- 📂 **Face Data Storage for Future Recognition**

## 🛠 Tech Stack
- **Python**
- **OpenCV**
- **Face Recognition Library**
- **Tkinter (GUI)**
- **NumPy**
- **Pandas (for Logging)**

## 📁 Project Structure
```
Pehchaan---Face-Recognition-System/
│── face_database/             # Stored known face encodings
│── detect.py                  # Core face detection logic
│── facereco_with_UI.py        # GUI + Face Recognition Integration
│── requirements.txt           # Dependencies list
│── README.md                  # Project documentation
│── image.png                  # Repository cover image
```

## 🎬 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/nitinhingwe/Pehchaan---Face-Recognition-System.git
cd Pehchaan---Face-Recognition-System
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python facereco_with_UI.py
```

## 🖥 GUI Overview
The **Pehchaan** interface provides:
- **Webcam Window** - Displays real-time facial recognition.
- **Admin Button** - Secure access to attendance logs.
- **New Entry Button** - Register new faces in the system.

## 🔧 Customization
### 1️⃣ Adjust Webcam Window Size
Modify the `resize()` function inside `facereco_with_UI.py`:
```python
img = img.resize((600, 400))  # Change width & height as needed
```
### 2️⃣ Customize Button Styles
Modify button properties in `facereco_with_UI.py`:
```python
admin_button = Button(frame, text="Admin", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=12, height=2)
```

## 🛡 Security & Future Enhancements
- Implement **database integration** for robust face data storage.
- Use **deep learning models** for improved accuracy.
- Add **multi-user role authentication**.

## 👨‍💻 Contributing
Want to contribute? Feel free to fork and open pull requests!

## 📝 License
This project is open-source.

---
🚀 **Pehchaan - Smarter & Secure Face Recognition System**


