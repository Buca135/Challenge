from fastapi import FastAPI, status
from googleapi import look_for_document
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/test-connection")
async def root():
    return {"message": "Conecction Status OK"}

@app.get("/search-in-doc/{file_id}")
async def search_in_doc(file_id, word:str ="default"):
    print(file_id)
    print(word)
    if look_for_document(file_id, word) != -1:
        return JSONResponse(status_code=200,content={})
    else:
        return JSONResponse(status_code=500,content={})

