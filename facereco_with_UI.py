import cv2
import face_recognition
import numpy as np
import os
import tkinter as tk
from tkinter import Label, Button, Frame, Entry, Toplevel, messagebox, ttk
from PIL import Image, ImageTk
from datetime import datetime
import csv

# Load known faces
known_face_encodings = []
known_face_names = []

for file in os.listdir("face_database"):
    if file.endswith(".npy"):
        name = file.split(".")[0]
        encoding = np.load(f"face_database/{file}")
        known_face_encodings.append(encoding)
        known_face_names.append(name)

# Initialize webcam
cap = cv2.VideoCapture(0)

current_face = None
entry_time = None
log_status = "Attendance"

# Ensure CSV file exists with headers
def initialize_csv():
    if not os.path.exists("face_recognition_log.csv"):
        with open("face_recognition_log.csv", "w", newline="") as log_file:
            writer = csv.writer(log_file)
            writer.writerow(["Action", "Name", "Time"])

initialize_csv()

def log_entry(action, name):
    with open("face_recognition_log.csv", "a", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow([action, name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

def recognize_faces():
    global current_face, entry_time
    ret, frame = cap.read()
    if not ret:
        return
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    detected_face = "Unknown"
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        
        if True in matches:
            first_match_index = matches.index(True)
            detected_face = known_face_names[first_match_index]
            
        color = (0, 255, 0) if detected_face != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, detected_face, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    if detected_face != current_face:
        if current_face is not None:
            log_entry("Face Changed", current_face)
        current_face = detected_face
        entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return frame

def update_frame():
    frame = recognize_faces()
    if frame is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = img.resize((600, 400))
        imgtk = ImageTk.PhotoImage(image=img)
        webcam_label.imgtk = imgtk
        webcam_label.configure(image=imgtk)
        webcam_label.after(10, update_frame)

def log_in():
    global log_status
    log_status = "You are Logged In"
    status_label.config(text=log_status)
    if current_face:
        log_entry("Log In", current_face)

def log_out():
    global log_status
    log_status = "You are Logged Out"
    status_label.config(text=log_status)
    if current_face:
        log_entry("Log Out", current_face)

def admin_action():
    def verify_admin():
        if admin_id.get() == "admin" and admin_password.get() == "admin":
            admin_window.destroy()
            show_log_data()
        else:
            messagebox.showerror("Error", "Invalid ID or Password")
    
    admin_window = Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.geometry("300x200")
    
    Label(admin_window, text="Admin ID:").pack(pady=5)
    admin_id = Entry(admin_window)
    admin_id.pack(pady=5)
    
    Label(admin_window, text="Password:").pack(pady=5)
    admin_password = Entry(admin_window, show="*")
    admin_password.pack(pady=5)
    
    Button(admin_window, text="Login", command=verify_admin).pack(pady=10)

def show_log_data():
    log_window = Toplevel(root)
    log_window.title("Face Recognition Log")
    log_window.geometry("500x300")
    
    tree = ttk.Treeview(log_window, columns=("Action", "Name", "Time"), show="headings")
    tree.heading("Action", text="Action")
    tree.heading("Name", text="Name")
    tree.heading("Time", text="Time")
    tree.pack(fill="both", expand=True)
    
    with open("face_recognition_log.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tree.insert("", "end", values=row)

# Creating main window
root = tk.Tk()
root.title("Pehchaan - Face Recognition System")
root.geometry("700x550")
root.configure(bg="white")

# Title Label
title_label = Label(root, text="PEHCHAAN", font=("Arial", 18, "bold"), bg="white")
title_label.pack(pady=5)

sub_label = Label(root, text="Face Recognition System", font=("Arial", 12), bg="white")
sub_label.pack()

# Frame for UI elements
frame = Frame(root, bg="white")
frame.pack(pady=10)

# Status Label
status_label = Label(frame, text=log_status, font=("Arial", 12, "bold"), bg="yellow", width=40)
status_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

# Webcam Window
webcam_label = Label(frame, text="Webcam Window", font=("Arial", 10), bg="gray", width=600, height=400)
webcam_label.grid(row=1, column=0, padx=10, pady=10)

# Buttons
admin_button = Button(frame, text="Admin", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=10, height=2, relief="raised", borderwidth=3, command=admin_action)
admin_button.grid(row=1, column=1, padx=30, pady=10, sticky="w")

log_in_button = Button(frame, text="Log In", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=10, height=2, relief="raised", borderwidth=3, command=log_in)
log_in_button.grid(row=3, column=0, padx=10, pady=5)

log_out_button = Button(frame, text="Log Out", font=("Arial", 14, "bold"), bg="#FF5733", fg="white", width=10, height=2, relief="raised", borderwidth=3, command=log_out)
log_out_button.grid(row=3, column=1, padx=10, pady=5)

# Start updating frames
update_frame()

# Run the application
root.mainloop()

# Release camera on exit
cap.release()
cv2.destroyAllWindows()
