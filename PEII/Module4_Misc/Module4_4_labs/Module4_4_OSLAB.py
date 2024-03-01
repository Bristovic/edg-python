# LAB program to make a directory-finder function
import os


def find(path, direc="."):
    os.chdir(direc)
    path_list = [x[0] for x in os.walk(direc)]
    path_count = 0
    for path_string in path_list:
        if path_string[-len(path):] != path:
            continue
        else:
            if (path_string[-len(path) - 1] == "/" or
                    path_string[-len(path) - 1] == "\\"):
                print(path_string)
                path_count += 1
            else:
                continue

    print(path_count, "matching paths found.")
    return


find("ardo", "..")
