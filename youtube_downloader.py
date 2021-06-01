#import the required modules

from pytube import YouTube
from pytube.cli import on_progress

#creating colour functions for quick reference..

def red(content): print("\033[91m {}\033[00m" .format(content))

def green(content): print("\033[92m {}\033[00m" .format(content))

def yellow(content): print("\033[93m {}\033[00m" .format(content))

def lightpurple(content): print("\033[94m {}\033[00m" .format(content))

def purple(content): print("\033[95m {}\033[00m" .format(content))

def cyan(content): print("\033[96m {}\033[00m" .format(content))

def lightgray(content): print("\033[97m {}\033[00m" .format(content))

def black(content): print("\033[98m {}\033[00m" .format(content))


def downloader_vid(url):
	try:
		yt=YouTube(url,on_progress_callback=on_progress)
		red("FETCHING....")
		name=str(yt.title)
		purple("do you wish to download  "+name)
		cyan("\n yes or no")
		red("type 0 for yes 1 to abort the download")
		choice=int(input())


		if(choice==0):
			lightgray("downloading")

			yellow("downloaded file will be save in the current directory ")
			cyan("it will automatically download the high quality")
			cyan("\n\n DOWNLOADING PLEASE WAIT.....")

			stream=yt.streams.first()
			stream.download()
			green("download success")
			
		elif(choice==1):
			red("downloading aborted...")
		else:
			red("enter the valid choice")
	except Exception as e:
		red("an error occured or try again with valid url")



def downloader_audio(url):
	try:
		yt=YouTube(url,on_progress_callback=on_progress)
		red("FETCHING....")
		name=str(yt.title)
		purple("do you wish to download  "+name)
		cyan("\n yes or no")
		red("type 0 for yes 1 to abort the download")
		choice=int(input())


		if(choice==0):
			lightgray("downloading")

			yellow("downloaded file will be save in the current directory ")
			cyan("it will automatically download the high quality")
			cyan("\n\n PLEASE WAIT DOWNLOADING.....")

			stream=yt.streams.filter(only_audio=True).first()
			stream.download()
			green("download success")
			
		elif(choice==1):
			red("downloading aborted...")
		else:
			red("enter the valid choice")
	except Exception as e:
		#red("an error occured or try again with valid url")
		raise e

#main function

lightpurple("Enter the valid url of Youtube")
url=input()

purple("do you want to download only audio or video")
red("enter 1 for audio and 0 for video")

choice=int(input())

#get the choice audio or video

if choice==1:
	downloader_audio(url)

else:
	downloader_vid(url)

yellow("Download completed and saved in the current directory")