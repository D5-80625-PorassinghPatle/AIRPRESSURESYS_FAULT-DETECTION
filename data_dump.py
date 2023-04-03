import pymongo
import pandas as pd
import json
from sensor.config import mongo_client
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="airpressuresys2"
COLLECTION_NAME="sensor"

if __name__=="__main__":

    df=pd.read_csv(DATA_FILE_PATH)

    print(F"ROWS AND COLUMN: {df.shape}")


    ##convert dataframe in jason format so that we can dump record in mongodb

    df.reset_index(drop=True,inplace=True )

    json_record=list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    ## git --version 
    ## git add
    ## git remote v
    ## git remote --v
    ## git reset 
    

    









