from urllib import response
from fastapi import FastAPI

from models.data_upload import Data_upload
from search_in_document import look_for_document
from upload_file import upload_file

#Esta es la estructura de la API
app = FastAPI()


@app.get("/test-connection")
async def test_connection():
    """Este es un request get para verificar la conexion.
    """
    return {"message": "Conecction Status OK"}

@app.get("/search-in-doc/{file_id}")
async def search_in_doc(file_id, word:str ="default"):
    """Este es un request get va a obtener el contenido de un archivo en el drive a partir del file ID.
    Y va a verificar si dentro del contenido del archivo esta el string word.
    """
    return look_for_document(file_id, word)

@app.post("/file/")
async def create_file(data_upload: Data_upload):
    """Este es un request post para la creacion de un archivo en drive con un titulo y descripcion ingresado.
    """
    reponse_if_null = data_upload.check_if_null()
    if reponse_if_null:
        return reponse_if_null
    response_especial_character = data_upload.check_if_special_character_title()
    if response_especial_character:
        return response_especial_character
    print(type(data_upload.descripcion))
    return upload_file(data_upload)
