import src.mafunction as f
import cv2 as cv


def main():
    #f.read_img(file_path="media/img1.jpg")
    #f.capture_video(isSave=0)
    #f.play_video(file_path="media/media1.mp4")
    #f.play_video(file_path=0)

    frame = f.read_img()
    frame = f.resize_frame(frame, (640,480))

    # img = f.processing_frame(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    f.show_frame("img", frame)
    f.show_frame("gray", gray)
    f.show_frame("hsv", hsv)

    cv.waitKey(0)






if __name__ == "__main__":
    main()