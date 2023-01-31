from sensor.utils import get_collection_as_dataframe
import sys,os

if __name__=="__main__":

    try:

        get_collection_as_dataframe(database_name="airpressuresys",collection_name="sensor")

    except:

        print(e)

