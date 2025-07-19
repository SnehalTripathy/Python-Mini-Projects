import face_recognition
import cv2
import csv
import numpy as np
from datetime import datetime

video_capture = cv2.VideoCapture(0)
snehal_image = face_recognition.load_image_file("Snehal.jpg")
snehal_encoding = face_recognition.face_encodings(snehal_image)[0]


known_face_encodings = [snehal_encoding]
known_faces_names = ["Snehal"]

#list of expected students
students = known_faces_names.copy()

face_locations = []
face_encodings = []

#getting the current time and date
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)


while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    #recognizing faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        
        best_match_index = np.argmin(face_distance)
        if(matches[best_match_index]):
             name = known_faces_names[best_match_index]
        
        if name in known_faces_names:
            font = cv2.FONT_HERSHEY_DUPLEX
            bottom_left = (10, 30)
            font_scale = 1.0
            font_color = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name+": Present", bottom_left, font, font_scale, font_color, thickness, lineType)
            
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H:%M:%S")
            lnwriter.writerow([name, current_time])
                
            
    cv2.imshow("Attendance Scanning", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()
# Saving attendance to CSV



        
             