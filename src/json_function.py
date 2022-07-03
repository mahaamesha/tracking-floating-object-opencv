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


# similar with write_obj_to_filejson, but only for clear file purpose
def clear_filejson(path):
    with open(path, "w") as f:
        json.dump({}, f, indent=4)
        pass


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



# SPECIFIC FUNCTION


def write_trackcentroidjson(centroid_arr=[]):
    file_path = "tmp/track_centroid.json"
    path = os.path.join(project_path, file_path)

    with open(path, "r") as f:
        data = json.load(f)
        
        # add new KEY if detect new cnt
        if len(data) < len(centroid_arr):
            new_id = len(centroid_arr)
            data["id_%s" %(new_id)] = []

        # append centroid to suitable KEY
        for n in range( len(centroid_arr) ):
            data["id_%s" %(n+1)].append(centroid_arr[n])
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def write_trackvelocityjson(key, speed, theta):
    file_path = "tmp/track_velocity.json"
    path = os.path.join(project_path, file_path)

    with open(path, "r") as f:
        data = json.load(f)
        
        ( data[key]["speed"] ).append(speed)
        ( data[key]["theta"] ).append(theta)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def init_tmp_files():
    write_obj_to_filejson(file_path="tmp/frame_text.json", obj={"fps": None, "contours": None})
    write_obj_to_filejson(file_path="tmp/track_centroid.json", obj={"id_1": []})
    write_obj_to_filejson(file_path="tmp/track_velocity.json", obj={"id_1": {"speed": [], "theta": []}})



# (END) SPECIFIC FUNCITION



if __name__ == "__main__":
    init_tmp_files()
    print("Run json_function.py ... Done")