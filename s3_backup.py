
///////////////////////////////////////////////

#listoout buckets

import boto3
import datetime
import shutil
import os


s3 = boto3.resource('s3')

def list_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)



///////////////////////////////////////////////////////////////////////////////////

#create bucket


def Create_bucket(s3,bucket_name , region):
    s3.create_bucket(Bucket = bucket_name ,
                     CreateBucketConfiguration = {
                         'LocationConstraint' : region
                     })
    print("Bucket Created")


# bucket_name = "krishna-trial-id-s3"
# region = "ap-south-1"
    
# Create_bucket(s3)
# Create_bucket(s3,"disco-dancer-niki","ap-south-1")

////////////////////////////////////////////////////////////////////////////////


#upload file to s3


def upload_s3(s3,file_name,bucket_name,key_name):
    s3.Bucket(bucket_name).put_object(Key= key_name , Body = 'data')

    print("backup uploaded successfully")

# file_name = r"C:\Users\Krishna\OneDrive\Desktop\s3-python\backed_up\backup_2025-01-29.tar.gz"

upload_s3(s3,"backup_2025-01-29.tar.gz","disco-dancer-niki","krishna-backup.zip")


//////////////////////////////////////////////////////////////////////////////////////////

#takes backup of folder 


def backup_files(source, destination):
    today = datetime.date.today()
    backup_name = os.path.join(destination, f"backup_{today}.tar.gz")

    shutil.make_archive(backup_name, "gztar", source)
source =""
destination = ""





