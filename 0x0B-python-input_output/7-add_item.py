#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    filename = "add_item.json"
    try:
        pyList = load_from_json_file(filename)

    except:
        pyList = []

    pyList += sys.argv[1:0]
    save_to_json_file(pyList, filename)
