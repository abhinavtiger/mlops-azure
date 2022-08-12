# mlops-azure
# Azure Fundamentals
This is repository contains the flask app, that displays the name the files present in my Azure Container.
This is the first assignment of the MLOps-Azure training.
# Running the app on a local machine
In order to run the flask app, perform the following steps

1. Make sure you have set up the environment with all the dependencies.
2. Activate the virtual environment by typing `source azure_env/bin/activate`
2. Login to your Azure Account, using `az login` command in your terminal.
3. Go to the root directory of the project, that is just outside of the `app` folder in the project directory.
4. Run the command `flask run` and copy the url with the public ip of yours vitrtual machine with the folder name name
5. Your app should run perfectly!

# Running the app deployed on the Azure Server
1. Make sure that the app is running on the Azure VM.
 

# Code Explanation
## `hello.py`
In this file, the code first connects with the Azure Storage Container and then fetches the blob names. 

* For creating a blob service client, the following code is executed
```
# Creating the blob service client 
connect_str = os.getenv('YOUR_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
```

* For connecting with a specific container, we provide the name of that container to the service client
```
# Getting the existing container from the storage account
container_name = 'your container name'
container_client = blob_service_client.get_container_client(container_name)

# Billing Information
![7](https://user-images.githubusercontent.com/101202870/184298668-e37dd5e5-fcd2-4dc2-b084-51136cf07b93.PNG)

