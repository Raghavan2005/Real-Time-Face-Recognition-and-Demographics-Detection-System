import cv2
import os

def load_models():
    age_net = cv2.dnn.readNetFromCaffe(
       "model/age_deploy.prototxt",
       "model/age_net.caffemodel"
    )
    gender_net = cv2.dnn.readNetFromCaffe(
       "model/gender_deploy.prototxt",
       "model/gender_net.caffemodel"
    )
    return age_net, gender_net

def predict_age_gender(face_img, age_net, gender_net):
    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
    gender_list = ['Male', 'Female']

    blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = gender_list[gender_preds[0].argmax()]

    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = age_list[age_preds[0].argmax()]

    return gender, age

def start_capture(name):
    detector = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
    age_net, gender_net = load_models()

    vid = cv2.VideoCapture(0)
    while True:
        ret, img = vid.read()
        if not ret:
            print("Failed to capture image")
            break

        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = detector.detectMultiScale(image=grayimg, scaleFactor=1.1, minNeighbors=5)
        for x, y, w, h in face:
            face_img = img[y:y+h, x:x+w].copy()
            gender, age = predict_age_gender(face_img, age_net, gender_net)
            
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
            cv2.putText(img, f"Gender: {gender}", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(img, f"Age: {age}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(img, "Face Detected", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
            cv2.putText(img, "Priya Dharshini Project", (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
            cv2.putText(img, "Press q or ESC to Exit", (x, y+h+60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
        
        cv2.imshow("Face Detection", img)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q") or key == 27:  # 'q' or 'ESC'
            break

    vid.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)  

if __name__ == "__main__":
    start_capture('none')
