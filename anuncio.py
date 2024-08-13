from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    SUB_TIPOS = ()

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.alto = alto
        self.ancho = ancho
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        self._alto = value if value > 0 else 1

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        self._ancho = value if value > 0 else 1

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value in self.SUB_TIPOS:
            self._sub_tipo = value
        else:
            raise SubTipoInvalidoException("Subtipo inválido")

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    @staticmethod
    def mostrar_formatos():
        for subclass in Anuncio.__subclasses__():
            print(f"FORMATO {subclass.formato.upper()}:")
            print("=" * 10)
            for subtipo in subclass.SUB_TIPOS:
                print(f"- {subtipo}")
            print()

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    SUB_TIPOS = ("instream", "outstream")
    formato = "video"

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    SUB_TIPOS = ("tradicional", "native")
    formato = "display"

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    SUB_TIPOS = ("facebook", "linkedin")
    formato = "social"

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
