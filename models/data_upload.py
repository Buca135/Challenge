from pydantic import BaseModel
from fastapi.responses import JSONResponse
import re

class Data_upload(BaseModel):
    """Este es el modelo de datos para manejo de datos. Se imprime en data_upload.
    Args:
        titulo (str): [titulo]
        descripcion (str): [descripcion]
    """
    titulo: str
    descripcion: str
    def check_if_null(self):
        """Si no tiene ningun dato valido genera mensaje de error.
            Returns:
                    bool o HTTP response
        """
        if self.descripcion == None or self.descripcion == '':
            return JSONResponse(status_code=404,content={"message": "Por favor ingresa la descripción"})
        if self.titulo == None or self.titulo == '':
            return JSONResponse(status_code=404,content={"message": "Por favor ingresa el titulo"})
        return False

    def check_if_special_character_title(self):
        """Si ingresa caracteres especiales en el titulo genera mensaje de error.
            Returns:
                    bool HTTP response
        """
        ## esta función sirve para verificar si el titulo llega vacio
        ## pararamente
        if re.search("[^A-Za-z0-9 ]", self.titulo):
            return JSONResponse(status_code=404,content={"message": "Por favor no ingresar caracteres especiales"})
        return False


