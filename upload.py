from azure.storage.blob import BlobServiceClient
import os


#change cridentials detils with your's details 
storage_account_key = "6728dc8Zr0yA8wgtk8Aub6ztIHz83YgF5h638hTfWWNcW4cXHMXXRF6CP0aEKmUPUt2JAQMiYRVJ+AStESzi1w=="
storage_account_name = "rdatastore"
connection_string = "DefaultEndpointsProtocol=https;AccountName=rdatastore;AccountKey=6728dc8Zr0yA8wgtk8Aub6ztIHz83YgF5h638hTfWWNcW4cXHMXXRF6CP0aEKmUPUt2JAQMiYRVJ+AStESzi1w==;EndpointSuffix=core.windows.net"
container_name = "uploadfile"

def uploadToBlobStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client =blob_service_client.get_blob_client(container=container_name,blob=file_name)

    with open(file_path,"rb") as data:
        blob_client.upload_blob(data)
        print("Upload "+file_name+" file")

uploadToBlobStorage('C:\\Users\\Hrashil Yogi\\OneDrive\\Documents\\cloud\\task.png','cloud')  