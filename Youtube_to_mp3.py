# importing packages 
from pytube import YouTube 
from pytube import Search
import os 

# Takes in a user input (link or search) and downloads the audio from the video
def Download(userInput, destination = os.path.dirname(__file__)):
    # if the user input is not a url, search for the video and get the first result
    if len(userInput) < 29 or (userInput[:29] != "https://www.youtube.com/watch" and userInput[:21] != "www.youtube.com/watch"):
        userInput = Search(userInput).results[0].watch_url

    # create YouTube video object with url either from input or search
    yt = YouTube(userInput) 
    
    try:
        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 
        
        # download the file 
        out_file = video.download(output_path=destination) 

    except:
        print("An error has occurred")
        return
    
    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    
    # result of success 
    print(yt.title + " has been successfully downloaded.")


userInput = str(input("Search for or enter the URL of the video you want to download: \n>> "))
Download(userInput)
