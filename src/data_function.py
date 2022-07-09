import matplotlib.pyplot as plt
import pandas as pd

from json_function import read_filejson


# return dataframe and dict
def build_centroid_obj():
    data = read_filejson(file_path="tmp/track_centroid.json")
    vals = list( data.values() )
    val = vals[0].copy()  # this only handle single object
    
    # create new KEY: "xc" and "yc" in DATA object
    data["xc"] = []
    data["yc"] = []
    for i in range( len(val) ):
        data["xc"].append(val[i][0])
        data["yc"].append(val[i][1])

    return data


def plot_centroid_data(obj):
    x = obj["xc"]
    y = obj["yc"]

    fig, axs = plt.subplots(2, figsize=(8,3*2))
    fig.suptitle("Centroid Position")
    
    axs_flat = axs.flat
    for ax in axs_flat:
        ax.plot(x, y)
        ax.set_ylim(max(y), min(y))     # reverse y axis
        ax.set(xlabel="x (px)", ylabel="y (px)")
        # ax.label_outer()        # Hide x labels and tick labels for top plots and y ticks for right plots.
        ax.grid(True)

    axs_flat[1].set_xlim(max(x)//3, int(max(x)*2/3))
    
    fig.tight_layout()
    plt.show()
    fig.savefig("media/plot_centroid.jpg")


# fps used to calculate time
def build_vector_obj(fps=30):
    data = read_filejson(file_path="tmp/track_vector.json")
    vals = list( data.values() )
    
    obj = vals[0].copy()        # only handle single object
    
    # time elapsed per frame
    time = 1 / fps
    # create new key to store time
    obj["frame"] = []
    obj["time"] = []
    for i in range( len(obj["speed"]) ):
        obj["frame"].append(i)
        obj["time"].append(i * time)
    # print(len(obj["speed"]))

    return obj


def plot_vector_data(obj, key="speed/acceleration", x_data="frame/time"):
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
    centroid_obj = build_centroid_obj()
    # df = pd.DataFrame(centroid_obj)
    # print(df)

    plot_centroid_data(centroid_obj)


    vector_obj = build_vector_obj(fps=24.76)
    # df = pd.DataFrame(vector_obj)
    # print(df)

    plot_vector_data(vector_obj, key="speed", x_data="time")
    plot_vector_data(vector_obj, key="acceleration", x_data="time")