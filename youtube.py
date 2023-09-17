from pytube import YouTube
link=input("enter url to download: ")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download
