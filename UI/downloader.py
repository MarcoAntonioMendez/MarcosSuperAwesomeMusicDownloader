import subprocess
import logging
import tkinter as tk

APPLICATION_NAME = "Marco's Super Awesome Music Downloader"

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540

FFMPEG_NOT_INSTALLED_MESSAGE = "Sorry, FFMPEG is not installed on your computer :("

class Downloader:
    def __init__(self):
        # Initializing the root to contain the main frame of the GUI application
        self.__root = tk.Tk()


        # Checking if ffmpeg is installed
        self.__ffmpeg_installed = False
        try:
            subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True, check=True)
            self.__ffmpeg_installed = True
        except FileNotFoundError:
            logging.warning("ffmpeg is not installed in this computer, please install ffmpeg.")



    def start(self):
        # Calculating some coordinates to center the window frame in the middle of computer screen
        self.__root.minsize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.__root.maxsize(WINDOW_WIDTH,WINDOW_HEIGHT)
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x_pos = int((screen_width - WINDOW_WIDTH)/2)
        y_pos = int((screen_height - WINDOW_HEIGHT)/2)
        self.__root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}")


        # Setting the icon of the application
        icon = tk.PhotoImage(file = "Images/flag.png")
        self.__root.iconphoto(True,icon)


        # Setting the application name
        self.__root.title(APPLICATION_NAME)


        # Setting the background image of the application
        background = tk.PhotoImage(file = "Images/background.png")
        label = tk.Label(self.__root, image=background)
        label.place(x = 0, y = 0, relwidth = 1, relheight = 1)


        # Depending of the ffmpeg status on the computer, the UI will change.
        # If ffmpeg is installed, then the noral interface will be shown and the program
        # will start withtou problems.

        # If ffmpeg is NOT installed, then a message will inform user to install ffmpeg for
        # the program to work.
        if(self.__ffmpeg_installed):
            logging.warning("ffmpeg is installed, continue.")
        else:
            logging.warning("ffmpeg is not installed, impossible to continue.")
            label = tk.Label(self.__root, text = FFMPEG_NOT_INSTALLED_MESSAGE, font=("Arial", 16, "bold"))
            label.place(x = 10, y = 10)

        # Starting the windows
        self.__root.mainloop()


