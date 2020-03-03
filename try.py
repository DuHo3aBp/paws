from paws.s3 import download

download(bucket='gdelt-open-data',\
    key='events/1979.csv',filename='1979.csv')