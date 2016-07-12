#-------------------------------------------------------------------------------
# Name:        module2_testing
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
                if 'REJECT' in line:
                    temp=line.split()
                    sourceip=str(temp[4])
                    if sourceip in string_dict:
                        string_dict[sourceip] += 1
                    else:
                        string_dict[sourceip] = 1
            json_string = json.dumps(string_dict)
            print type(json_string)

        return json_string

    except:
        print("Error executing getCountRejects")


def uploadingtos3(json_formatted_string,bucket_key,bucket_name):
    try:

        # Upload the file to S3

        c = boto.connect_s3('AKIAJZ2XM7R62KEFGTWQ','jOSdsljj7CoPyiIX7wJal9QrK0GOzMQdNZbZwr8Q')
        b = c.get_bucket(bucket_name)
        k=Key(b)
        k.key=bucket_key
        k.set_contents_from_string(json_formatted_string)

    except:
        print("Error in uploading file")


def main():
    pass

if __name__ == '__main__':
    main()
    string_dict={}
    file_path=sys.argv[1]
    s3_path=sys.argv[2]
    #Assuming the file path as s3://dwollatechnicalexercise/problem1 where bucketname =dwollatechnicalexercise key= problem1
    name=str(s3_path).split("/")
    bucket_name= name[2]
    bucket_key=name[3]
    json_formatted_string=getCountRejects(file_path)
    uploadingtos3(json_formatted_string,bucket_key,bucket_name)










