import dlib
import cv2
import json

# create list for landmarks
ALL = list(range(0, 68))
RIGHT_EYEBROW = list(range(17, 22))
LEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INNER = list(range(61, 68))
JAWLINE = list(range(0, 17))


# create face detector, predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


# create VideoCapture object (input the video)
# 0 for web camera
vid_in = cv2.VideoCapture(0)
#vid_in = cv2.VideoCapture("baby_vid.mp4")

# capture the image in an infinite loop -> make it looks like a video
with open("test.json", "w") as json_file:
    while True:
        # Get frame from video > success : ret = True / fail : ret= False
        ret, image_o = vid_in.read()

       # resize the video
        image = cv2.resize(image_o, dsize=(640, 480), interpolation=cv2.INTER_AREA)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get faces (up-sampling=1)
        face_detector = detector(img_gray, 1)
        # the number of face detected
        print("The number of faces detected : {}".format(len(face_detector)))

        # one loop belong to one face
        for face in face_detector:
            # face wrapped with rectangle
            cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()),
                          (0, 0, 255), 3)
            #create list to contain landmarks
            landmark_list = []

            # detect 68 facial landmarks
            landmarks = predictor(image, face)

            # append (x, y) in landmark_list
            for p in landmarks.parts():
                landmark_list.append([p.x, p.y])
                cv2.circle(image, (p.x, p.y), 2, (0, 255, 0), -1)

            # transform landmark_list to dict and save in json
            key_val = [ALL, landmark_list]
            landmark_dict = dict(zip(*key_val))
            print(landmark_dict)
            json_file.write(json.dumps(landmark_dict))
            json_file.write('\n')

        cv2.imshow('result', image)

        # wait for keyboard input
        key = cv2.waitKey(1)

        # if esc,
        if key == 27:
            break

vid_in.release()