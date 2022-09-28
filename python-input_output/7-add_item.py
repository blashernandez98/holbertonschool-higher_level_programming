#!/usr/bin/python3
""" Task 7 module """

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []

for idx, arg in enumerate(sys.argv):

    if idx != 0:
        obj.append(str(arg))

save_to_json_file(obj, "add_item.json")
