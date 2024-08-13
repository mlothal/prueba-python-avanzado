from datetime import date
from campaña import Campaña
from error import SubTipoInvalidoException, LargoExcedidoException

anuncios_data = [
    {"tipo": "Video", "sub_tipo": "instream", "duracion": 10, "url_archivo": "archivo.mp4", "url_clic": "http://ejemplo.cl"},
    {"tipo": "Display", "sub_tipo": "tradicional", "ancho": 300, "alto": 250, "url_archivo": "display.jpg", "url_clic": "http://ejemplo.cl"},
    {"tipo": "Social", "sub_tipo": "facebook", "ancho": 600, "alto": 400, "url_archivo": "social.png", "url_clic": "http://ejemplo.cl"}
]
fecha_inicio = date(2024, 5, 26)
fecha_termino = date(2024, 6, 26)

campaña = Campaña(nombre="", fecha_inicio=fecha_inicio, fecha_termino=fecha_termino, anuncios=anuncios_data)

Campaña.mostrar_formatos()

try:
    nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
    campaña.nombre = nuevo_nombre

    nuevo_subtipo = input("Ingrese un nuevo subtipo para el anuncio de video: ")
    campaña.anuncios[0].sub_tipo = nuevo_subtipo

except LargoExcedidoException as e:
    with open("error.log", "a") as error_file:
        error_file.write(f"Error al cambiar el nombre de la campaña: {e}\n")
    print(e)

except SubTipoInvalidoException as e:
    with open("error.log", "a") as error_file:
        error_file.write(f"Error al cambiar el subtipo del anuncio: {e}\n")
    print(e)

print(campaña)


