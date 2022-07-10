import pandas as pd
import matplotlib.pyplot as plt
from math import sin, cos, pi

from json_function import read_filejson


def build_data_obj(fps=30):
    # data from track_centroid.json
    data_centroid = read_filejson(file_path="tmp/track_centroid.json")
    vals_centroid = list( data_centroid.values() )
    val_centroid = vals_centroid[0].copy()  # this only handle single object
    
    # data from track_vector.json
    data_vector = read_filejson(file_path="tmp/track_vector.json")
    vals_vector = list( data_vector.values() )
    val_vector = vals_vector[0].copy()  # this only handle single object

    # calculate time per frame
    time = 1 / fps

    # create new obj to store all data
    obj = {}

    # create new KEY: "frame" and "time" in object
    obj["frame"] = []
    obj["time"] = []
    # create new KEY: "xc" and "yc" in object
    obj["xc"] = []
    obj["yc"] = []
    # create new KEY: "xc" and "yc" in object
    # Iam not use update() because handling same length issue
    obj["speed"] = []
    obj["acceleration"] = []
    obj["theta"] = []

    # append data to obj
    for i in range( len(val_centroid) ):
        obj["frame"].append( i )
        obj["time"].append( i*time )
        obj["xc"].append( val_centroid[i][0] )
        obj["yc"].append( val_centroid[i][1] )
        obj["speed"].append( val_vector["speed"][i] )
        obj["acceleration"].append( val_vector["acceleration"][i] )
        obj["theta"].append( val_vector["theta"][i] )

    return obj


def add_vector_component_to_obj(obj, param="speed", add_key=["vx", "vy"]):
    # add key to obj
    for key in add_key:
        obj[key] = []

    # assign value to the new key
    for i in range( len(obj[param]) ):
        # get vector components
        num = obj[param][i]
        theta = obj["theta"][i]
        ex = num * cos(theta * pi / 180)      # convert theta_degree to theta_radian
        ey = num * sin(theta * pi / 180)      # convert theta_degree to theta_radian
        
        # append data to list: obj[key]
        obj[add_key[0]].append(ex)
        obj[add_key[1]].append(ey)

    return obj


def plot_centroid_data(obj):
    x = obj["xc"]
    y = obj["yc"]

    fig, axs = plt.subplots(2, figsize=(12,8))
    fig.suptitle("Centroid Position", size="xx-large", weight="bold")
    
    for ax in axs:
        ax.plot(x, y)
        ax.set_ylim(max(y), min(y))     # reverse y axis
        ax.set(xlabel="x (px)", ylabel="y (px)")
        # ax.label_outer()        # Hide x labels and tick labels for top plots and y ticks for right plots.
        ax.grid(True)

    axs[1].set_xlim(int(max(x)*2/5), int(max(x)*3/5))
    
    plt.tight_layout()
    
    # save it
    try:    # for notebook environment
        fig.savefig("../media/plot_centroid.jpg")
        plt.show()
    except:     # for local python environment
        fig.savefig("media/plot_centroid.jpg")


def plot_param_per_time(obj, params=["xc", "yc", "speed", "acceleration"]):
    # define x_data for plotting
    x = obj["time"]

    # define y_data for every plot
    for param in params:
        y = obj[param]

        # define figure and axis
        # I want to plot curve in (1) full range x axis, (2) middle range x axis
        fig, axs = plt.subplots(nrows=2, figsize=(12,8))
        suptitle_text = "%s vs time" %param
        fig.suptitle(suptitle_text, size="xx-large", weight="bold")
        
        # plotting every data
        for ax in axs:
            ax.plot(x, y)
            ax.grid(True)

            # set label
            ax.set_xlabel("time (s)")
            if param in ["xc", "yc"]:
                ax.set_ylabel("%s (px)" %param)
            elif param in ["speed", "vx", "vy"]:
                ax.set_ylabel("%s (px/s)" %param)
            elif param in ["acceleration", "ax", "ay"]:
                ax.set_ylabel("%s (px/s^s)" %param)
            elif param == "theta":
                ax.set_ylabel("%s (°)" %param)

            # set axis limit
            if param == "yc":
                ax.set_ylim(max(y), min(y))     # reverse y axis

            # set x limit for subplots in row=1, set limit in midle range
            if ax == axs[len(axs)-1]:
                ax.set_xlim(int(max(x)*2/5), int(max(x)*3/5))

        plt.tight_layout()

        # save it
        try:    # for notebook environment
            fig.savefig("../media/plot_%s.jpg" %param)
            plt.show()
        except:     # for local python environment
            fig.savefig("media/plot_%s.jpg" %param)


# plot position, velocitiy, and acceleration in a graph
def plot_params_in_one_graph(obj, params=["xc", "vx"]):  
    # define figure and axis. I only want to have 1 figure
    # I want to plot curve in (1) full range x axis, (2) middle range x axis
    fig, axs = plt.subplots(nrows=2, figsize=(12,8))
    suptitle_text = "Plot %s and %s" %(params[0], params[1])
    fig.suptitle(suptitle_text, size="xx-large", weight="bold")

    # define x y data for plotting
    x = obj["time"]
    y1 = obj[params[0]]
    y2 = obj[params[1]]

    # plotting every data
    for ax in axs:
        l1, = ax.plot(x, y1)

        ax2 = ax.twinx()
        l2, = ax2.plot(x, y2, color="gray")

        ax.grid(True)

        # set label
        ax.set_xlabel("time (s)")
        ax.set_ylabel("%s (px)" %params[0])
        ax2.set_ylabel("%s (px/s)" %params[1])

        # set axis limit
        if "yc" in params:
            ax.set_ylim(max(y1), min(y1))     # reverse y axis

        # set x limit for subplots in row=1, set limit in midle range
        if ax == axs[len(axs)-1]:
            ax.set_xlim(int(max(x)*2/5), int(max(x)*3/5))
                

        ax.legend([l1, l2], [params[0], params[1]])

    plt.tight_layout()
    
    # save it
    try:    # for notebook environment
        fig.savefig("../media/plot_%s_%s.jpg" %(params[0], params[1]))
        plt.show()
    except:     # for local python environment
        fig.savefig("media/plot_%s_%s.jpg" %(params[0], params[1]))


if __name__ == "__main__":
    data_obj = build_data_obj(fps=24.76)
    data_obj = add_vector_component_to_obj(data_obj, param="speed", add_key=["vx", "vy"])

    plot_centroid_data(data_obj)

    params=["xc", "yc", "vx", "vy", "speed", "acceleration", "theta"]
    plot_param_per_time(data_obj, params=params)


    params = ["xc", "vx"]
    plot_params_in_one_graph(data_obj, params=params)

    params = ["yc", "vy"]
    plot_params_in_one_graph(data_obj, params=params)