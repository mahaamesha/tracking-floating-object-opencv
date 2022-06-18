import src.mafunction as f


def main():
    #f.capture_video(isSave=0)
    path1 = "media/media1.mp4"
    path2 = "E:/_TUGAS/_ITBOneDrive/OneDrive - Institut Teknologi Bandung/_Kuliah/_sem7/7_tugas akhir I/media/video-eksperimen/20-1.mp4"
    f.play_video(file_path=path2, process_func=f.processing_frame3, isSave=1, isLoop=0)
    # f.play_video(file_path=0, isSave=1)
    

if __name__ == "__main__":
    main()