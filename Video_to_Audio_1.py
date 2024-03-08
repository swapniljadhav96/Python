
# Video to Audio Converter
# Mp4 to Mp3 Converter
# Audio converter
# Extract Audio from Video

# Import necessary libraries
from moviepy.editor import VideoFileClip  # for video processing
from PyQt5 import QtWidgets  # for building GUI
import sys  # for system-specific parameters and functions
from PyQt5.QtWidgets import *  # widgets for adding text messages in the GUI
from PyQt5.QtGui import *  # used to edit fonts in GUI


# Function to generate output file name with .mp3 extension
def output_name(name):
    name = name.split("/")[-1]  # Extract file name from the path
    name = name.split(".")[0]   # Extract file name without extension
    return name + ".mp3"


# Function to convert MP4 to MP3
def convert(mp4):
    mp3_file = output_name(mp4)  # Generate output file name
    videoclip = VideoFileClip(mp4)  # Open the video file
    audioclip = videoclip.audio  # Extract audio from the video
    audioclip.write_audiofile(mp3_file)  # Save audio as MP3 file
    audioclip.close()  # Close the audio clip
    videoclip.close()  # Close the video clip


# Class for the main application window
class Convertmp(QtWidgets.QWidget):
    def __init__(self):
        super(Convertmp, self).__init__()
        self.initUI()

    # Initialize the GUI
    def initUI(self):
        self.setGeometry(600, 300, 400, 300)  # Set window geometry
        self.setWindowTitle("MP4 TO MP3 Converter")  # Set window title

        # Add labels for instructions
        a = QLabel('*** Welcome *** ', self)
        a.setFont(QFont('Arial Rounded MT Bold', 15))
        a.move(100, 10)
        a = QLabel('Convert Video to Audio ', self)
        a.setFont(QFont('Arial Rounded MT Bold', 15))
        a.move(70, 35)

        # Add Browse button
        btn = QtWidgets.QPushButton("Browse", self)
        btn.setToolTip('Click to import video')
        btn.clicked.connect(self.Browse)
        btn.setFont(QFont('Arial', 15))
        btn.resize(200, 60)
        btn.move(100, 100)

        # Add Convert button
        btn = QtWidgets.QPushButton("Convert", self)
        btn.setToolTip('Click to convert into audio')
        btn.clicked.connect(self.conv)
        btn.clicked.connect(self.show_info_messagebox)
        btn.setFont(QFont('Arial', 15))
        btn.resize(200, 60)
        btn.move(100, 200)
        self.show()

    # Browse method to select MP4 file
    def Browse(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(
            self, "Single File", "*.mp4")
        self.c = filepath[0]  # Store selected file path
        print("Filepath: ", self.c)

    # Method to show confirmation message after conversion
    def show_info_messagebox(self):
        a = QLabel('Convert Video to Audio ', self)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setGeometry(680, 440, 400, 300)
        msg.setText("Your video is converted")
        msg.setWindowTitle("Converter")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    # Method to handle conversion process
    def conv(self):
        try:
            convert(self.c)  # Call convert function with selected file path
        except:
            pass  # Catch exceptions if file path is not provided


# Main function to start the application
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Convertmp()
    app.exec_()


# Check if the script is being run directly
if __name__ == "__main__":
    main()
