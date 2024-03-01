# getting info about the OS
import os
import platform

# print(os.uname())  # will not work on Windows
print(platform.uname())  # returns detail about OS and machine
print(os.name)  # returns posix, nt, or java (Unix, Windows, or Jython)

# # making a new directory
# os.mkdir("./my_first_directory")
# # printing dir contents list
# print(os.listdir())

# making multiple directories
os.makedirs("./my_first_dir/my_second_dir")
# changes directory
os.chdir("./my_first_dir")
print(os.listdir())

# get current working directory
print(os.getcwd())
os.chdir("../")
print(os.getcwd())

# removing single directory
# os.rmdir("") # will cause error if directory has subdirectories

# removing multiple directories
os.removedirs("./my_first_dir/my_second_dir")

# using system function to process commands
end_val = os.system("mkdir another_dir")
print(end_val)
end_val = os.system("rmdir another_dir")
print(end_val)
