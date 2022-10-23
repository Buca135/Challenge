from pydantic import BaseModel
from fastapi.responses import JSONResponse
import re

class Data_upload(BaseModel):
    def check_if_null(self):
        if self.descripcion == None or self.descripcion == '':
            return JSONResponse(status_code=404,content={"message": "Por favor ingresa la descripción"})
        if self.titulo == None or self.titulo == '':
            return JSONResponse(status_code=404,content={"message": "Por favor ingresa el titulo"})
        return False

    def check_if_special_character_title(self):
        ## esta función sirve para verificar si el titulo llega vacio
        ## pararamente
        if re.search("[^A-Za-z0-9 ]", self.titulo):
            return JSONResponse(status_code=404,content={"message": "Por favor no ingresar caracteres especiales"})

    titulo: str
    descripcion: str
