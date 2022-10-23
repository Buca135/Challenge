from pydantic import BaseModel

class Data_upload(BaseModel):
    titulo: str
    descripcion: str
