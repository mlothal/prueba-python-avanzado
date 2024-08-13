from datetime import date
from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self._crear_anuncio(anuncio) for anuncio in anuncios]

    def _crear_anuncio(self, anuncio_data):
        tipo = anuncio_data.get("tipo")
        sub_tipo = anuncio_data.get("sub_tipo")
        url_archivo = anuncio_data.get("url_archivo", "")
        url_clic = anuncio_data.get("url_clic", "")

        if tipo == "Video":
            return Video(1, 1, url_archivo, url_clic, sub_tipo, anuncio_data.get("duracion", 5))
        elif tipo == "Display":
            return Display(anuncio_data.get("ancho", 1), anuncio_data.get("alto", 1), url_archivo, url_clic, sub_tipo)
        elif tipo == "Social":
            return Social(anuncio_data.get("ancho", 1), anuncio_data.get("alto", 1), url_archivo, url_clic, sub_tipo)
        else:
            raise ValueError("Tipo de anuncio no soportado")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoException("El nombre de la campaña no debe superar los 250 caracteres")
        self.__nombre = value

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        cant_video = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Video))
        cant_display = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Display))
        cant_social = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Social))
        return f"""
        nombre de la campaña: {self.nombre}
        Anuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social
        """

    @staticmethod
    def mostrar_formatos():
        Anuncio.mostrar_formatos()
