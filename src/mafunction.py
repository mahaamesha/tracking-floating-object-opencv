from time import sleep
import cv2 as cv
import sys
import numpy as np
from imutils import grab_contours


def show_frame(winname, img, isSave=0):
    cv.imshow(winname=winname, mat=img)
    cv.waitKey(0)
    if isSave: cv.imwrite(filename=winname, img=img)


# read image
def read_img(file_path="media/img1.jpg"):
    img = cv.imread(file_path)

    if img is None:
        sys.exit("Error: Could not read the image")

    return img


# set size video
def set_frame_size(cap, size=(640, 480)):
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


def get_cap_fps(cap):
    fps = cap.get(cv.CAP_PROP_FPS)
    return fps


def get_cap_size(cap):
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    heigth = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    return width, heigth


def get_frame_shape(frame):
    height, width, channels = frame.shape
    return width, height, channels


def crop_frame(frame):
    
    return frame


def get_lower_upper_hsv(color=[30,200,127], err_range=50, v_range=50):
    lower_color = []
    upper_color = []
    
    for i in range(3):
        # set wide error range only for V value
        if i == 2: err_range = v_range

        # initialize lower upper
        lower_i = color[i] - err_range
        upper_i = color[i] + err_range
        
        # ensure lower_i not negative
        if lower_i < 0: lower_i = 0

        # ensure upper_i is in range
        # H: [0,179], S: [0,255], V: [0,255]
        if i == 0:      # check H
            if upper_i > 179: upper_i = 179
        else:       # check S and V
            if upper_i > 255: upper_i = 255

        # append the value_i to the suitable array
        lower_color.append(lower_i)
        upper_color.append(upper_i)

    # convert to numpy array: [ H S V]
    lower_color = np.array(lower_color)
    upper_color = np.array(upper_color)

    return lower_color, upper_color


# use background substractor to detect object
def background_substractor(method="MOG2/KNN"):
    if (method == "MOG2"):
        backSub = cv.createBackgroundSubtractorMOG2()
    elif (method == "KNN"):
        backSub = cv.createBackgroundSubtractorKNN()
    else:
        sys.exit("Error: choose mode 'MOG2' or 'KNN'")
    
    return backSub


# apply background substractor on certain frame to detect object
def apply_background_substractor(frame, method="MOG2/KNN"):
    backSub = background_substractor(method)
    fgMask = backSub.apply(frame)
    return fgMask


def processing_frame(frame):
    # convert original img as gray/hsv img
    cvt = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cvt = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # bluring to removes noise
    imgaus = cv.GaussianBlur(cvt, (5,5), 0)

    # Set BACKGROUND to Black and OBJECT to White
    ret, thresh = cv.threshold(imgaus, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)


    # finding contours
    cnts, hierarchy = cv.findContours(imgaus, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for cnt in cnts:
        cv.drawContours(frame, cnt, -1, (0,255,0), 3)
    print("Contours:", len(cnts))

    cv.imshow("frame", frame)
    # cv.imshow("gray", gray)
    cv.imshow("imgaus", imgaus)
    cv.imshow("thresh", thresh)

    return frame


def processing_frame2(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    imgaus = cv.GaussianBlur(hsv, (11,11), 0)

    # extract only red color in certain range
    lower_hsv, upper_hsv = get_lower_upper_hsv(color=[30,200,127], err_range=50)
    mask = cv.inRange(imgaus, lower_hsv, upper_hsv)

    kernel = np.ones( (3,3), np.uint8 )
    erodila = cv.erode(mask, kernel, iterations=5)
    erodila = cv.dilate(erodila, kernel, iterations=20)
    erodila = cv.erode(erodila, kernel, iterations=15)

    edge = cv.Canny(erodila, 0, 255)

    res = cv.bitwise_and(frame, frame, mask=erodila)

    cnts = cv.findContours(erodila, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = grab_contours(cnts)
    
    contoured = frame.copy()
    contoured = cv.drawContours(contoured, cnts, -1, (0,255,0), 2)
    
    final = contoured.copy()

    print("Contours:", len(cnts))


    # gray = cvtColor(frame, cv.COLOR_BGR2GRAY)
    # ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # f.show_frame("img", frame)
    # # f.show_frame("gray", gray)
    # f.show_frame("hsv", hsv)
    # f.show_frame("imgaus", imgaus)
    # f.show_frame("mask", mask)
    # f.show_frame("erodila", erodila)
    # f.show_frame("edge", edge)
    # f.show_frame("res", res)
    # f.show_frame("final", final)
    # # f.show_frame("thresh", thresh)

    # cv.waitKey(0)

    return final


def processing_frame3(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    imgaus = cv.GaussianBlur(hsv, (5,5), 0)

    # extract only red color in certain range
    lower_hsv, upper_hsv = get_lower_upper_hsv(color=[179,200,127], err_range=50, v_range=50)
    mask = cv.inRange(imgaus, lower_hsv, upper_hsv)

    kernel = np.ones( (3,3), np.uint8 )
    erodila = cv.erode(mask, kernel, iterations=2)
    erodila = cv.dilate(erodila, kernel, iterations=20)
    erodila = cv.erode(erodila, kernel, iterations=15)

    edge = cv.Canny(erodila, 0, 255)

    res = cv.bitwise_and(frame, frame, mask=erodila)

    cnts = cv.findContours(erodila, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = grab_contours(cnts)
    
    contoured = frame.copy()
    contoured = cv.drawContours(contoured, cnts, -1, (0,255,0), 2)
    
    final = contoured.copy()

    print("Contours:", len(cnts))

    return final


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
def play_video(file_path="media/media1.mp4", process_func=None):
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
        frame = resize_frame(frame, (640,480))

        # playback video by reset the frame_counter
        cap, frame_counter = reverse_playback(cap, frame_counter)
        
        # image processing for every frame
        frame = process_func(frame)

        # show the frame
        cv.imshow("frame", frame)

        # exit the window
        if (cv.waitKey(1) == ord('q')):
            break
    
    cap.release()
    cv.destroyAllWindows()