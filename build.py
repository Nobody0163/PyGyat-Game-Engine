from os import listdir
from os.path import isfile, join
from subprocess import run

pypath = input("Enter full path to the folder python.exe is in (do not include a slash at the end): ")
command = pypath + r"\python.exe " + pypath + r"\Scripts\pygyat --compile "
files = [f for f in listdir("src/") if isfile(join("src/", f))]

print(files)

for f in files:
    command += "src/" + f + " "

run(command)