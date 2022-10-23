from __future__ import print_function

import io
from create_token import create_token

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from fastapi.responses import JSONResponse
from googleapiclient.http import MediaIoBaseDownload

def look_for_document(file_id, word):
    """Busca un docmento por medio del file_ID en el drive del usuario y despues se descarga para 
    buscar si en el documento hay una palabra igual al word.
    Args:
        file_id (str): [file_id]
        word (str): [word]
    Returns:
        bool
        """
    creds = create_token()
    try:
        service = build('drive', 'v3', credentials=creds)

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
        file = None
    if not file:
        return JSONResponse(status_code=500,content={"message": "No existe el archivo para el ID ingresado: " + file_id})
    elif str(file.getvalue()).find(word) == -1:
        return JSONResponse(status_code=500,content={"message": f"No se encontro la palabra {word} en el archivo con el file_id {file_id} "})
    else:
        return JSONResponse(status_code=200,content={"message": f"Se encontro la palabra {word} en el {file_id} "})


