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

## Questions to confirm
confirmed_1 = True 	# 'Did you open bubble-app.slack.com?'
confirmed_2 = True	# 'Please go to bubble-bot and type in "new_developer"'
confirmed_3 = True	# 'Did you open bubble-app.slack.com?'

# Function that sends confirmation questions.
def confirm_question(question):
	question = raw_input(question + '(y / n)')

	if (question == 'y' or question == 'yes' or question == 'Y'):
		return True
	elif (question == 'n' or question == 'N' or question == 'no'):
		return False
	else:
		return False

# Function that creates files for us in other paths.
def file_creator(path, data, filename):

	print('Creating a file named ' +  '"' + filename + '"' + ' inside of ' + path)

	# Create a file with the open function.
	f = open(path + filename ,"w+")

	# Write the new data inside of the file.
	f.write(data)

	# Print closing message.
	print('Created ' + '"' + filename + '"'   + '')

	# Close the fie stream.
	f.close()

# Function that downloads the repos.
def download_repo(repo):

	## Clone "bubble_private" INSIDE of "bubble"
	if(repo == repo_urls[1]):

		## Split the repo because subprocess requires the repos to be broken into a list. --> ['git', 'clone', 'repo']
		repo_split = ('git clone ' + repo).split()

		## This is the repo path. It is supposed to download "bubble_private" inside of the bubble repository.
		repo_path = os.path.dirname(os.path.abspath(__file__)) + '/bubble'

		try:
			# Call the command that is split in the command line.
			subprocess.Popen(repo_split, cwd=repo_path).communicate()
			print('Finished Cloning: ' + repo)
		except OSError as Err:
			print(Err)
			## Incase there's some error, catch that fucker.
			print('ERORR - Error while cloning ' + repo)

	else:
		## Split the repo because subprocess requires the repos to be broken into a list. --> ['git', 'clone', 'repo']
		repo_split = ('git clone ' + repo).split()

		try:
			# Call the command that is split in the command line.
			subprocess.call(repo_split)
			print('Finished Cloning: ' + repo)
		except OSError as Err:
			print(Err)
			## Incase there's some error, catch that fucker.
			print('ERORR - Error while cloning ' + repo)


def file_editor(path, old_tag, new_tag):
	print('FILE EDITED')

################################################################################
'''

	Fifth Step  - Download the REPOS

'''

## Download the motherfucking repos.
# for repo in repo_urls:
# 	download_repo(repo)


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

		# Path for the file that we should edit.
		edit_path = 'HAHAHA'

		# Old tag to locate the part of the file that we want to edit.
		old_tag = 'AHAHAH'

		# New data to place inside of the old tag.
		new_tag = 'ASDFSADF'

		# Pass data to file creator, and create the file with the data.
		file_creator(credential_path, input_credentials, 'credentials.coffee')

		# Edit the file, so the localhost becomes local.bubble.is
		file_editor(edit_path, old_tag, new_tag)
