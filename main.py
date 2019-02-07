#-*-coding: utf-8-*-
from platform import python_version as pv
from commands import *

def getflags(string):
	args = ["", []]
	index = 0
	for arg in string.split():
		if index == 0:
			args[index] = arg
			index += 1
			continue
		args[index].append(arg)
	return args

if __name__ == '__main__':
	shell = Shell()
	inputcmd = ""
	if pv()[0] == "3":
		raw_input = input
	while inputcmd != "exit":
		inputcmd = raw_input("{}>".format(getcwd()))
		cmd, flags = getflags(inputcmd)
		if cmd in shell.cmds:
			if shell.cmds[cmd][1]:
				shell.cmds[cmd][0](flags)
			else:
				shell.cmds[cmd][0]()
		else:
			print("Command '{}' not found.".format(cmd))