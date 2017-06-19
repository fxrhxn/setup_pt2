import os
import subprocess



# Function to change the background.
def background_change(path):

	full_command = """osascript -e 'tell application "Finder" to set desktop picture to "{0}" as POSIX file'""".format(path)

	os.system(full_command)

	print('Changed Hompepage!')

# Download logos folder for the homepage and other things like that.
os.system('git clone https://github.com/fxrhxn/change_homepage')


# Get the current path where the folder is downloaded.
current_path = os.getcwd() + '/change_homepage/images/main.jpg'

# Call the function that gets the images. and turns the background into it. Pass the path of the image.
background_change(current_path)
