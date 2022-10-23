from urllib import response
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models.data_upload import Data_upload
from search_in_document import look_for_document
from upload_file import upload_file

app = FastAPI()


@app.get("/test-connection")
async def root():
    return {"message": "Conecction Status OK"}

@app.get("/search-in-doc/{file_id}")
async def search_in_doc(file_id, word:str ="default"):
    if look_for_document(file_id, word) != -1:
        return JSONResponse(status_code=200,content={})
    else:
        return JSONResponse(status_code=500,content={})

@app.post("/file/")
async def create_file(data_upload: Data_upload):
    reponse_if_null = data_upload.check_if_null()
    if reponse_if_null:
        return reponse_if_null
    response_especial_character = data_upload.check_if_special_character_title()
    if response_especial_character:
        return response_especial_character
    print(type(data_upload.descripcion))
    return upload_file(data_upload)
