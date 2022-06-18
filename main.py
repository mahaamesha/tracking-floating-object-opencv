import src.mafunction as f
# import cv2 as cv
# import numpy as np
# from imutils import grab_contours


def main():
    #f.read_img(file_path="media/img1.jpg")
    #f.capture_video(isSave=0)
    path1 = "media/media1.mp4"
    path2 = "E:/_TUGAS/_ITBOneDrive/OneDrive - Institut Teknologi Bandung/_Kuliah/_sem7/7_tugas akhir I/media/video-eksperimen/20-1.mp4"
    f.play_video(file_path=path2, process_func=f.processing_frame3, isSave=0, isLoop=0)
    # f.play_video(file_path=0, isSave=1)

    # frame = f.read_img()
    # frame = f.resize_frame(frame, (640,480))

    # img = f.processing_frame2(frame)
    # gray = cv.cvtColor(imgaus, cv.COLOR_BGR2GRAY)
    

if __name__ == "__main__":
    main()