import os
import subprocess
import sys

# Function that sends confirmation questions.
def confirm_question(question):
	question = raw_input(question + '(y / n)')

	if (question == 'y' or question == 'yes' or question == 'Y'):
		return True
	elif (question == 'n' or question == 'N' or question == 'no'):
		return False
	else:
		return False


confirm_question('Testing shit.')
