from flask import Flask,redirect, url_for, request,render_template,jsonify
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name__)
#Get request
@app.route('/<foldername>')
def fun(foldername):
    res = []
    connect_str ='DefaultEndpointsProtocol=https;AccountName=storageabhinav;AccountKey=O7e7ahS63elKWp/tbO8NjZu6KiJGmn+wlEs3r/JjdbYQnuJOILXjcR8pEhOuS9FtVtvQGO/X8tqu+AStlPk0Gg==;EndpointSuffix=core.windows.net'
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="newcontainer")
    blob_list = blob_service_client.list_blobs()
    print(blob_service_client)
    print(blob_list)
    for blob in blob_list:
        temp = str(blob.name)
        folder,file = temp.split('/')
        if folder  ==  foldername:
            res.append(file)
    return jsonify(res)
if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True)
