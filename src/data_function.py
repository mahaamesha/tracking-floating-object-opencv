import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from json_function import read_filejson


# return dataframe and dict
def build_obj():
    data = read_filejson(file_path="tmp/track_centroid.json")

    for val in data.values():   # length_of_val = 603   iteration = 1
        val_arr = val.copy()
    
    # create new KEY: "xc" and "yc" in DATA object
    data["xc"] = []
    data["yc"] = []
    for i in range( len(val_arr) ):
        data["xc"].append(val_arr[i][0])
        data["yc"].append(val_arr[i][1])

    return data


def plot_centroid_data(obj):
    x = obj["xc"]
    y = obj["yc"]

    fig, axs = plt.subplots(2)
    fig.suptitle("Centroid Position")
    
    axs_flat = axs.flat
    for ax in axs_flat:
        ax.plot(x, y)
        ax.set_ylim(max(y), min(y))     # reverse y axis
        ax.set(xlabel="x (px)", ylabel="y (px)")
        # ax.label_outer()        # Hide x labels and tick labels for top plots and y ticks for right plots.
        ax.grid(True)

    axs_flat[1].set_xlim(max(x)//3, max(x)//1.5)
    
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    obj = build_obj()
    
    df = pd.DataFrame(obj)
    print(df)

    plot_centroid_data(obj)