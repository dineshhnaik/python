import turtledemo as d
import turtle as t

tt = t.getturtle()
tt.speed(1)

while True:
    tt.distance(10, 10)
    tt.forward(-11)
    # tt.backward(20)

# input("")
# import datetime as d
# # from datetime import datetime
#
# dat = d.datetime
# print(dat.now().ctime())

# from io import FileIO, BytesIO
# from pathlib import Path, WindowsPath
#
# path = WindowsPath()
# current_dir = path.cwd()
# # print(current_dir)
#
# dir_path = Path(current_dir.joinpath('test'))
# # print(f'dir name: {dir_path.name}') # returns directory name
# # print(f'dir cwd: {dir_path.cwd()}') # returns directory path
#
# if not dir_path.exists():
#     print(f'Directory does not exists in the path: {dir_path.cwd()}')
#     dir_path.mkdir(1)
#     print('Directory created successfully!')
# counter = 22
# # for file in dir_path.glob("*.txt"):
# #     print(f'File: {file.name}')
# #     file.rename(file.name+ '_'+str(counter))
# b = bytes("Hello, how are you?", "utf-8")
# b2 = bytearray()

# Creates files with contents
# for i in range(5):
#     fileName = FileIO(dir_path.cwd().joinpath("test", "file_"+ str(i + 1) + ".txt"), 'a')
#     # b2 = bytearray()
#     # fileName.readinto(b2)
#     fileName.write(b)
#     fileName.close()

# counter = 23
# for file in dir_path.glob("*.txt"):
#     file.rename(file.cwd().joinpath(file.name + "_" +str(counter)))
#     counter += 2
#
# print('Reading files...')
# for i in range(5):
#     fileName = FileIO(dir_path.cwd().joinpath("test", "file_" + str(i + 1) + ".txt"), 'r')
#     s = str(fileName.readall(), "utf-8")
#     print(f'File name: {fileName.name} : Content: {s}')
#     # print(f'File name: file_{i+1}.txt: Content: {fileName.readall()}')
#     # fileName.write(b)
#     fileName.close()


# b = bytes("hello", "utf-8")
# print(b)
# f = FileIO("C:\\Dinesh\\Code\\Python\\PythonExercises\\test\\1.txt", mode="a")
# f.write(b)
# f.close()



# from pathlib import Path, WindowsPath
# from fileinput import FileInput

# path = WindowsPath()
# current_dir = path.cwd()
#
# new_dir_name = input('Enter the new folder name: ')
# new_dir_path = Path(current_dir.joinpath(new_dir_name))
#
# file = FileInput("C:\Dinesh\Code\Python\PythonExercises\test\1.txt")
# print(file.filename)


# Iterates the folder
# for p in current_dir.iterdir():
#     print(p.name)

# print(f'New directory name: {new_dir_path}')
# if new_dir_path.exists():
#     print('Directory already exists')
#     # new_dir_path.rmdir() # Removes the directory
#     print('Removed the directory')
# else:
#     new_dir_path.mkdir(1)
#     print('New folder is created.')

# print(f'Current dir is: {current_dir}')
# new_dir = input('Enter the new folderName:')
# Iterates the folder
# for p in path.glob('*.*'):
#     print(p.name)


# import datetime as d
# from datetime import datetime, date
# from threading import currentThread, Timer
# import os
# import io
#
# print(os.getcwd())
# i = io()

# a = datetime.today()
# c = date.today()
# # print(c.today())
# th = currentThread()
# th.

# def print_time():
#     print(datetime.today())
#

# print_time()

# timer = Timer(1, print_time(), args=None, kwargs=None)

# timer.run()
# timer.start()
