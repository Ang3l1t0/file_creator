# from sys import argv
import subprocess

file_name = input("File name: ")

f = open(file_name, "w")
f.write("#!/usr/bin/node")
f.close()
subprocess.call(['chmod', 'a+x', file_name])
