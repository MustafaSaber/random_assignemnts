import cv2
import face_recognition
import os


def read_and_detect(img_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return gray, faces


def save_detected_faces(gray, faces, text):
    i = 0
    for (x, y, w, h) in faces:
        temp_face = gray[y:y + h, x:x + w]
        cv2.imwrite(text + str(i) + '.jpg', temp_face)
        i = i + 1
    return i


def check(counter1, counter2, texts):
    ans = (-1, -1, -1)
    for i in range(counter1):
        current_ori_image = face_recognition.load_image_file(texts[0] + str(i) + '.jpg')
        try:
            current_ori_image_encoding = face_recognition.face_encodings(current_ori_image)[0]
            for j in range(counter2):
                current_id_image = face_recognition.load_image_file(texts[1] + str(j) + '.jpg')
                try:
                    current_id_image_encoding = face_recognition.face_encodings(current_id_image)[0]
                    match = face_recognition.compare_faces([current_ori_image_encoding], current_id_image_encoding,
                                                           tolerance=0.6)
                    prob = face_recognition.face_distance([current_ori_image_encoding], current_id_image_encoding)

                    if match[0]:
                        ans = (i, j, prob)
                except IndexError:
                    pass
        except IndexError:
            pass
    return ans


def clear(counter1, counter2, texts):
    for i in range(counter1):
        try:
            os.remove(texts[0] + str(i) + '.jpg')
        except: pass

    for i in range(counter2):
        try:
            os.remove(texts[1] + str(i) + '.jpg')
        except: pass


def main(original_photo_path, id_photo_path, original_name):
    texts = ["original", "ID"]
    gray_original, faces_original = read_and_detect(original_photo_path)
    gray_id, faces_id = read_and_detect(id_photo_path)
    counter1 = save_detected_faces(gray_original, faces_original, texts[0])
    counter2 = save_detected_faces(gray_id, faces_id, texts[1])
    (i, j, prob) = check(counter1, counter2, texts)
    if i == -1:
        print("No similarity")
    else:
        print("A similarity for {} photo is found between photo {} and photo {} with probability = {}".format(
            original_name, i, j, prob))
    temp = input("Press 'c' if you want to clear stored images.")
    if temp == "c":
        clear(counter1, counter2, texts)


if __name__ == "__main__":
    main('../BBi/sample13.jpg', '../BBi/sample13.jpg', 'Ahmed')
