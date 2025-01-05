from pytubefix import YouTube 

# where to save 
SAVE_PATH = "/download" #to_do 

url = input("Enter URL of the video: ")

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()
print(f"Downloading {yt.title}")
stream.download(output_path="downloads/")
print("Download successful")