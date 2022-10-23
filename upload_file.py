from __future__ import print_function

from create_token import create_token

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from models.data_upload import Data_upload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def upload_file(data_upload: Data_upload):
    """Crea documento en drive con su respectivo titulo y descripcion.
    Args:
        data_upload (Data_upload): [data_upload]
    Returns:
        bool
        """
    creds = create_token()

    try:
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': data_upload.titulo, 'description': data_upload.descripcion}

        file = service.files().create(body=file_metadata,
                                      fields='id, name, description').execute()
        print(F'File ID: {file.get("id")}')
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
        file = None
    return {"id": file.get("id"),"titulo": file.get("name"), "descripcion”:": file.get("description")}