# this file contains any function that modify json file

import os
import json
import sys

working_path = os.path.dirname(__file__)
project_path = os.path.join(working_path, "../")


# GENERAL FUNCTION

def read_filejson(file_path="tmp/file.json"):
    try:
        path = os.path.join(project_path, file_path)

        with open(path, "r") as f:
            data = json.load(f)
        
        return data
    except:
        sys.exit("Error: Cannot find %s" %file_path)


def write_obj_to_filejson(file_path="tmp/file.json", obj={}):
    path = os.path.join(project_path, file_path)

    # initialize file if it's not already
    with open(path, "a"):
        pass
    
    if (obj == {}):
        while True:
            ans = input("Write empty obj to %s? (y/n) " %file_path)
            if (ans == "y"): break
            elif (ans == "n"): sys.exit("Canceled")

    with open(path, "w") as f:
        json.dump(obj, f, indent=4)


# i use this to write FPS, CONTOURS, ets in frame_text.json
# format json file: {"key1":value1, "key2":value2}
def write_keyvalue(file_path="tmp/file.json", key="keyname", value=None):
    path = os.path.join(project_path, file_path)
    with open(path, "r+") as f:
        data = json.load(f)

        if key in data.keys():
            data[key] = value
        else:
            sys.exit("Error: There is no key named \"%s\"" %key)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# (END) GENERAL FUNCTION




if __name__ == "__main__":
    # initialization format of some file.json
    write_obj_to_filejson(file_path="tmp/frame_text.json", obj={"fps": None, "contours": None})
    write_obj_to_filejson(file_path="tmp/track_centroid.json", obj={})
    
    # write_keyvalue(file_path="tmp/frame_text.json", key="fps", value=24)