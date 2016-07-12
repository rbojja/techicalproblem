#-------------------------------------------------------------------------------
# Name:        Script to count number of rejects per source ip and uploading to aws s3 bucket 
# Purpose:
#
# Author:      Rajesh
#
# Created:     11/07/2016
# Copyright:   (c) Rajesh 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import json
import sys
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

def getCountRejects(file_path):
    try:

        with open(file_path) as f_handle:
            for line in f_handle:
#Finding REJECT in each line and then using split function to store the sourceip address which is field srcaddress after interface-id field 
                if 'REJECT' in line:
                    temp=line.split()
                    sourceip=str(temp[4])
                    if sourceip in string_dict:
#If sourceip already exists in dictionary ,incrementing the number of rejects for this specific sourceip
                        string_dict[sourceip] += 1
                    else:
#If sourceip does not exist in dictionary key ,then creating key and initializing the value to 1 
                        string_dict[sourceip] = 1
#Converting dictionary to json format without creating temporary file in local folder
            json_string = json.dumps(string_dict)

        return json_string

    except:
        print("Error executing getCountRejects")


def uploadingtos3(json_formatted_string,bucket_key,bucket_name):
    try:

# Upload the file to S3
#Establishing connection assuming access keys as environment variables otherwise need to pass access key and secret access key as parameters to the function
        c = boto.connect_s3()
        b = c.get_bucket(bucket_name)
#Getting bucket name from the s3 url given and assigning key 
        k=Key(b)
        k.key=bucket_key
#Storing the json formatted result to the s3 key 
        k.set_contents_from_string(json_formatted_string)

    except:
        print("Error in uploading file")


#main function
def main():
    pass

if __name__ == '__main__':
    main()
#Initializing dictionary 
    string_dict={}
#Getting arguments and storing into file_path and s3_path variables
    file_path=sys.argv[1]
    s3_path=sys.argv[2]
    #Assuming the file path format as s3://dwollatechnicalexercise/problem1 where bucketname =dwollatechnicalexercise key= problem1
    name=str(s3_path).split("/")
    bucket_name= name[2]
    bucket_key=name[3]
#counting number of rejects per source ip by calling function getCountRejects which returns the json result 
    json_formatted_string=getCountRejects(file_path)
#uploading to s3 bucket
    uploadingtos3(json_formatted_string,bucket_key,bucket_name)










