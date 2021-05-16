#!/usr/bin/python3
""" Script that adds all args to Python list, then save them to a file """

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists("add_item.json"):
    List = load_from_json_file('add_item.json')
else:
    List = []

args = sys.argv[1:]
List.extend(args)

save_to_json_file(List, 'add_item.json')
