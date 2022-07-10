import matplotlib.pyplot as plt
import pandas as pd

from json_function import read_filejson


# return dataframe and dict
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


def plot_centroid_data(obj):
    x = obj["xc"]
    y = obj["yc"]

    fig, axs = plt.subplots(2, figsize=(8,3*2))
    fig.suptitle("Centroid Position")
    
    for ax in axs:
        ax.plot(x, y)
        ax.set_ylim(max(y), min(y))     # reverse y axis
        ax.set(xlabel="x (px)", ylabel="y (px)")
        # ax.label_outer()        # Hide x labels and tick labels for top plots and y ticks for right plots.
        ax.grid(True)

    axs[1].set_xlim(max(x)//3, int(max(x)*2/3))
    
    fig.tight_layout()
    plt.show()
    fig.savefig("media/plot_centroid.jpg")


def plot_param_per_time(obj, params=["xc", "yc", "speed", "acceleration"]):
    # define x_data for plotting
    x = obj["time"]

    # define figure and axis
    fig, axs = plt.subplots(nrows=len(params)//2, ncols=2)
    fig.suptitle("Plot Data")

    # define y_data for every plot
    for param in params:
        y = obj[param]
        
        # plotting every data
        for ax in axs:
            ax.plot(x, y)

            ax.grid(True)

    
    plt.show()
            
        
    

    

def plot_vector_data(obj, key="speed/acceleration/theta", x_data="frame/time"):
    x = obj[x_data]
    y = obj[key]

    fig, axs = plt.subplots(2, figsize=(8,3*2))
    fig.suptitle("%s vs %s" %(key, x_data))

    for ax in axs:
        ax.plot(x, y)
        ax.set_xlabel(x_data)
        if "speed" in key: ax.set_ylabel("speed (px/s)")
        elif "acceleration" in key: ax.set_ylabel("acceleration (px/s^2)")

        ax.grid(True)

    axs[1].set_xlim(max(x)//3, int(max(x)*2/3))
    fig.tight_layout()
    plt.show()
    fig.savefig("media/plot_%s.jpg" %key)


if __name__ == "__main__":
    data_obj = build_data_obj()
    df = pd.DataFrame(data_obj)
    print(df)

    plot_param_per_time(data_obj)

    # centroid_obj = build_centroid_obj()
    # df = pd.DataFrame(centroid_obj)
    # print(df)

    # plot_centroid_data(centroid_obj)


    # vector_obj = build_vector_obj(fps=24.76)
    # df = pd.DataFrame(vector_obj)
    # print(df)

    # plot_vector_data(vector_obj, key="speed", x_data="time")
    # plot_vector_data(vector_obj, key="acceleration", x_data="time")