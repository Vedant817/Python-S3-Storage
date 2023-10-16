
#* Doc: https://www.linode.com/docs/products/storage/object-storage/guides/aws-sdk-for-python/
import boto3
import os

#? Uploading a folder:
def uploadFolder(client, folder):
    files = []
    for dirpath, dirname, filenames in os.walk(folder):
        for file in filenames:
            files.append(os.path.join(dirname, file))
            client.upload_file(
                Filename=dirname.replace('\\', '/')+file, #? Name of the file to be uploaded with the path. 
                Bucket='bucket-label',
                Key=dirname.replace('\\', '/')+file,
                ExtraArgs={"ACL": "public-read"}),


linode_obj_config = { #! Add the secret-key, access-key from the cloud provider.
    "aws_access_key_id": "[access-key]",
    "aws_secret_access_key": "[secret-key]",
    "endpoint_url": "[cluster-url]",
}

#? Initializing the Client
client = boto3.client("s3", **linode_obj_config)

#? List of all the buckets created by the user.
buckets = client.list_buckets()
for bucket in buckets['Buckets']:
    print(bucket['Name'])

#? List all the objects in the bucket => Bucket Name: example-bucket
objects = client.list_objects(Bucket='example-bucket')
for object in objects['Contents']:
    print(object['Key'])

#? Uploading a file as an Object
#! Key [required]: The name of the object you wish to create, including any prefix/path.
client.upload_file(
    Filename='Sample.txt',
    Bucket='bucket-label',
    Key='Sample.txt')

#? Uploading Files from the folder:
uploadFolder(client, 'folder_name')
