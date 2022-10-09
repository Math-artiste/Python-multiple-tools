import pytube
import sys, time
import os

def progressBar(count, total, suffix=''):
    barLength = 60
    filledLength = int(round(barLength * count / float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = "*" * filledLength + "-" * (barLength - filledLength)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, "%", suffix))
    sys.stdout.flush()


url = input("Enter the video url : ")

#for path, uncomment :
#path = input("Enter path of storage")

path = "C:\\Users\\montage du 60\\Documents\\Python\\daily_life\\dl_vid_yout"
print("Videos is downloading........")
for i in range(11) :
    time.sleep(1)
    progressBar(i, 10)
print("Done !")
pytube.YouTube(url).streams.get_highest_resolution().download(path)
os.system("cls")

