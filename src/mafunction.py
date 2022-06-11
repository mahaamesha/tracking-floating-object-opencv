from time import sleep
import cv2 as cv
import sys


# read image
def read_img(file_path="media/img1.jpg"):
    img = cv.imread(file_path)

    if img is None:
        sys.exit("Error: Could not read the image")
    
    cv.imshow(winname=file_path, mat=img)
    cv.waitKey(0)
    cv.imwrite(filename=file_path, img=img)


# set size video
def set_size_video(cap, size=(640, 480)):
    cap.set(cv.CAP_PROP_FRAME_WIDTH, size[0])
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, size[1])


def resize_frame(frame, size=(640, 480)):
    frame = cv.resize(frame, (size[0], size[1]))
    return frame


# to reverse frame, so every frame will be contiuous
def reverse_playback(cap, frame_counter):
    frame_counter += 1

    if frame_counter == cap.get(cv.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)
    
    return cap, frame_counter


def get_fps(cap):
    fps = cap.get(cv.CAP_PROP_FPS)
    return fps


# use background substractor to detect object
def background_substractor(mode="MOG2/KNN"):
    if (mode == "MOG2"):
        backSub = cv.createBackgroundSubtractorMOG2()
    elif (mode == "KNN"):
        backSub = cv.createBackgroundSubtractorKNN()
    else:
        sys.exit("Error: choose mode 'MOG2' or 'KNN'")
    
    return backSub


def processing_frame(frame):
    # convert original img to gray img
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # bluring to removes noise
    imgaus = cv.GaussianBlur(gray, (5,5), 0)


    # finding contours
    cnts, hierarchy = cv.findContours(imgaus, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        cv.drawContours(frame, cnt, -1, (0,255,0), 3)
    print("Contours:", len(cnts))

    cv.imshow("frame", frame)
    cv.imshow("gray", gray)
    cv.imshow("imgaus", imgaus)


# capture video from camera 0
# video saved in "media/recording.mp4"
def capture_video(isSave=0):
    cap = cv.VideoCapture(0)

    # for saving, I need define codec and create VideoWriter object
    if isSave:
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter("media/recording.mp4", fourcc, 20.0, (640,480))

    if (not cap.isOpened()):
        print("Error: Can't open camera")
        exit()

    while True:
        # capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly, ret is True
        if (not ret):
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if isSave: out.write(frame)

        # resize
        frame = resize_frame(frame, (640,100))
        
        # show the frame
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if (cv.waitKey(1) == ord('q')):
            break
    
    cap.release()
    if isSave: out.release()
    cv.destroyAllWindows()


# play video from file
def play_video(file_path="media/media1.mp4"):
    cap = cv.VideoCapture(file_path)

    if (not cap.isOpened()):
        print("Error: Can't open camera")
        exit()

    frame_counter = 0       # used in reverse_playback()
    while True:
        # capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly, ret is True
        if (not ret):
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # resize
        #frame = resize_frame(frame, (640,480))

        # playback video by reset the frame_counter
        cap, frame_counter = reverse_playback(cap, frame_counter)
        
        # image processing for every frame
        processing_frame(frame)

        # show the frame
        # cv.imshow("frame", frame)

        # exit the window
        if (cv.waitKey(1) == ord('q')):
            break
    
    cap.release()
    cv.destroyAllWindows()