from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

account_name = os.getenv('ACCOUNT_NAME')
account_key = os.getenv('ACCOUNT_KEY')

blob_service_client = BlobServiceClient(f'https://{account_name}.blob.core.windows.net', credential=account_key).get_container_client(container='testcon')
blobsin = blob_service_client.get_blob_client(blob='emp_tt.xlsx')

r = blobsin.download_blob()
with open ('downloadxl.xlsx', 'wb') as f:
    f.write(r.readall())

#blob_service_client.upload_blob(data='requirements.txt', name='fos.txt')