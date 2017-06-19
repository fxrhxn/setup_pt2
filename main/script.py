import os
import subprocess
import sys


'''
TODO

IN ONE COMMAND, this script should....

1) Download Bubble, and Bubble Private.

2) Create the credentials.coffee file, and allow users to paste their data in there.

3) Edit etc folder so the localhost is local.bubble.is


'''


## Repo urls to clone.
repo_urls = ['https://github.com/bubblegroup/bubble', 'https://github.com/jphaas/bubble_private']


# Function that downloads the repos.


################################################################################
'''

	Fifth Step  - Download the REPOS

'''

## Download the motherfucking repos.
for repo in repo_urls:
	download_repo(url)


################################################################################
'''

	Sixth Step  - Bubble Site SETUP

'''
# Make the first confirmed question False to start the process..
confirmed_1 = False

# Repeating question to be answered.
while confirmed_1 == False:

	if confirm_question('Did you open bubble-app.slack.com?  ') == False:

		print("We can't proceed unless you verify that you have opened bubble-app.slack.com.")
	else:

		# Set confirmed_1 to True( AKA closing it. )
		confirmed_1 = True

		# Set confirmed_2 to False( AKA activating it. )
		confirmed_2 = False

# Repeating question to be answered.
while confirmed_2 == False:

	if confirm_question('Please send a direct message to bubblebot and type in "new_developer"') == False:

		print("We can't move on unless this is done.")
	else:

		# Set confirmed_2 to True( AKA closing it. )
		confirmed_2 = True

		# Set confirmed_3 to False( AKA activating it. )
		confirmed_3 = False


# Repeating question to be answered.
while confirmed_3 == False:


	if confirm_question('Did the credentials to print out? It may take a while. [20 - 30 minutes]') == False:

		print("We can't move on unless this is done.")
	else:
		confirmed_3 = True

		# Ask for the user's credentials!
		print('Enter the Credentials. Press Ctrl D to Save.')
		input_credentials = sys.stdin.read()

		# Path for the credentials file.
		credential_path = os.getcwd() + '/bubble/lib/'

		# Pass data to file creator, and create the file with the data.
		file_creator(credential_path, input_credentials, 'credentials.coffee')
