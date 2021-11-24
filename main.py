# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
from optparse import Option


def exercise1():
    i = input("We are going to cut a BBB Video in N seconds. Enter the initial second.")
    N = input("How long do you want the cut to last? Enter the number.")
    command = ["ffmpeg", "-ss", i, "-i", "BBB.mp4", "-c", "copy", "-t", N, "BBB_cut.mp4"]  # with this line we do the
    # cutting process
    subprocess.call(command)

    command2 = ["ffplay", "BBB_cut.mp4"]  # we reproduce the cut we have done
    subprocess.call(command2)


def exercise2():
    command = ["ffmpeg", "-i", "BBB_cut.mp4", "-vf",
               "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay", "BBBhistogramYUV.mp4"] # extracting
    # the YUV histogram
    subprocess.call(command)

    command2 = ["ffplay", "BBBhistogramYUV.mp4"]
    subprocess.call(command2)


def exercise3():
    option = int(input("Choose the resolution you want \n\n\t 1 - 720p\n\n\t 2 - 480p\n\n\t 3 - 360x240\n\n\t "
                       "4 - 160x120p\n\n\t"))

    if option == 1:
        command = ["ffmpeg", "-i", "BBB_cut.mp4", "-s", "1280x720", "-c:a", "copy", "BBB_720p.mp4"]
        subprocess.call(command)

        command2 = ["ffplay", "BBB_720p.mp4"]
        subprocess.call(command2)

    elif option == 2:
        command = ["ffmpeg", "-i", "BBB_cut.mp4", "-s", "852x480", "-c:a", "copy", "BBB_480p.mp4"]
        subprocess.call(command)

        command2 = ["ffplay", "BBB_480p.mp4"]
        subprocess.call(command2)

    elif option == 3:
        command = ["ffmpeg", "-i", "BBB_cut.mp4", "-s", "360x240", "-c:a", "copy", "BBB_360x240p.mp4"]
        subprocess.call(command)

        command2 = ["ffplay", "BBB_360x240p.mp4"]
        subprocess.call(command2)

    elif option == 4:
        command = ["ffmpeg", "-i", "BBB_cut.mp4", "-s", "160x120", "-c:a", "copy", "BBB_160x120p.mp4"]
        subprocess.call(command)

        command2 = ["ffplay", "BBB_160x120p.mp4"]
        subprocess.call(command2)

    else:
        print("Not available option. Choose a correct one, please")


def exercise4():
    opt = int(input("We want to change the audio signal into a mono output. \nPlease, choose a codec:\n\n\t 1 - "
                    "MPEG4""\n\n\t 2 - H264\n\n\t"))
    command = ["ffmpeg", "-i", "BBB_cut.mp4", "-ac", "1", "BBB_Mono.mp4"]
    subprocess.call(command)
    if opt == 1:
        command = ["ffmpeg", "-i", "BBB_cut.mp4", "-acodec", "mpeg4", "-vcodec", "copy", "BBB_Mono.mp4"]
        subprocess.call(command)

        command2 = ["ffplay", "BBB_Mono.mp4"]
        subprocess.call(command2)
    elif opt == 2:
        command = ["ffmpeg", "-i", "BBB_cut.mp4", "-acodec", "h264", "-vcodec", "copy", "BBB_Mono.mp4"]
        subprocess.call(command)

        command2 = ["ffplay", "BBB_Mono.mp4"]
        subprocess.call(command2)

    else:
        print("Choose a correct option please")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt = int(input("Please, select the exercise you want"
                       "\n\n\t 1 -Cutting a BBB video"
                       "\n\n\t 2 -YUV histogram"
                       "\n\n\t 3 -Changing the resolution of a video"
                       "\n\n\t 4 -Converting an audio into mon and changing the codec of it  \n\n\t"))

    if opt == 1:
        exercise1()
    elif opt == 2:
        exercise2()
    elif opt == 3:
        exercise3()
    elif opt == 4:
        exercise4()

    else:
        print("Please, choose a correct number")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
