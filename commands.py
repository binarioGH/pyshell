#-*-coding: utf-8-*-
from os import getcwd, chdir, listdir, path, system
from platform import platform

class Shell:
	def __init__(self):
		'''
		each index of 'cmds' has a tuple as value, the
		first value in the tuple is de method  that will
		be called from other file, the second value is if
		the method needs arguments or not.'''
		self.cmds = {
		"ls": (self.ls, False),
		"cd": (self.cd, True),
		"clear": (self.clear, False),
		"echo": (self.echo, True),
		"cp": (self.cp, True)
		}
	def ls(self):
		for file_or_dir in listdir():
			if path.isdir(file_or_dir):
				print("		{}   <DIR>".format(file_or_dir))
			else:
				print("		{}".format(file_or_dir))
	def cd(self, dir):
		try:
			chdir(dir[0])
		except:
			print("Path not found")
	def clear(self):
		if platform()[0] == "W":
			clear = "cls"
		else:
			clear = "clear"
		system(clear)
	def echo(self, toprint):
		print(" ".join(toprint))
	def cp(slef, args):
		try:
			with open(args[0], "rb") as tocopy:
				content = tocopy.read()
			with open(args[1], "wb") as copier:
				copier.write(content)
		except Exception as e:
			print(e)