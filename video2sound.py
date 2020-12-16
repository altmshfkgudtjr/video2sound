from moviepy.editor import *

FILE_PATH = './video/'
SAVE_PATH = './sound/'
FILE_NAME = 'dynamite.mp4'

videoclip = VideoFileClip(FILE_PATH + FILE_NAME)
audioclip = videoclip.audio