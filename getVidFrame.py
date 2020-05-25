import cv2

# Create VideoCapture object; open video file
vid_input = cv2.VideoCapture("baby_vid.mp4")

# If you want to use your web-camera,
# cv2.VideoCapture(0)

count = 0
print("start")

# check video file open successfully
while (vid_input.isOpened()):
    # Get frame from video
    # get success : ret = True / fail : ret= False
    ret, frame = vid_input.read()

    # fail to get frame
    if not ret:
        break

    # succeed
    else:
        # save the frame
        cv2.imwrite("C:\\Users\\Haemin\\Documents\\GitHub\\balanchew\\video_frame\\frame%d.jpg" % count, frame)

    print('frame%d.jpg saved!' % count)
    count += 1

vid_input.release()