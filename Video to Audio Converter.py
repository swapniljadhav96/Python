# Video to Audio Converter
# Mp4 to Mp3 Converer
# Audio converter
# Extract Audio from Video

from moviepy.editor import VideoFileClip   #for doing operations on video
from PyQt5 import QtWidgets                #for building GUI
import sys                                 #organize large code into small reusable pieces.
from PyQt5.QtWidgets import *              #widgets for add text messages in the GUI.
from PyQt5.QtGui import *                  #used to edit fonts in GUI.

def output_name(name):
    name = name.split("/")[-1]
    name = name.split(".")[0]               #file name and extention
    return name + ".mp3"

def convert(mp4):
    mp3_file = output_name(mp4)
    videoclip = VideoFileClip(mp4)
    audioclip = videoclip.audio                     #converts the video to audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()

class Convertmp(QtWidgets.QWidget):
    def __init__(self):
        super(Convertmp,self).__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(600, 300, 400, 300)
        self.setWindowTitle("MP4 TO MP3 Convertor")                 #GUI is created

        a = QLabel('*** Welcome *** ',self )
        a.setFont(QFont('Arial Rounded MT Bold', 15))               #Text label is added , font.
        a.move(100, 10)
        a = QLabel('Convert Video to Audio ', self)
        a.setFont(QFont('Arial Rounded MT Bold', 15))
        a.move(70, 35)

        #Buttons
        btn = QtWidgets.QPushButton("Browse",self)                 #button is created
        btn.setToolTip('Click to import video')

        btn.clicked.connect(self.Browse)                           #given path to button on clicked
        btn.setFont(QFont('Arial', 15))
        btn.resize(200,60)
        btn.move(100, 100)

        btn = QtWidgets.QPushButton("Convert", self)              #second button created for converting vedio on clicked
        btn.setToolTip('Click to covert into audio')

        btn.clicked.connect(self.conv)
        btn.clicked.connect(self.show_info_messagebox)
        btn.setFont(QFont('Arial', 15))
        btn.resize(200,60)
        btn.move(100, 200)
        self.show()

    def Browse(self):                                       #path for importing vedio file to convert
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Single File", "*.mp4")
        self.c = filepath[0]
        print("Filepath: ", self.c)

    def show_info_messagebox(self):                           #confirmation message after converting to audio.
        a = QLabel('Convert Vedio to Audio ', self)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setGeometry(680, 440, 400, 300)

        # setting message for Message Box
        msg.setText("your vedio is converted ")

        # setting Message box window title
        msg.setWindowTitle("convertor")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # start the app
        retval = msg.exec_()

    def conv(self):                                   #execption cases
        try:
            convert(self.c)
        except:                                       # if file is not imported it is a exepctional cass it will pass
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Convertmp()
    app.exec_()

if __name__ == "__main__":

    main()
