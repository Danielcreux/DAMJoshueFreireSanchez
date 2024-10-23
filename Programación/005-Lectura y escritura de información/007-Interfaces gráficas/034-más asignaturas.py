from PIL import Image, ImageDraw, ImageFont
from funcionsemana import *

fechasmarcas1 = generate_specific_weekday_dates(
    '2024-09-01',
    '2024-06-01',
    2
    )

def generaimagenes(imagen,asignatura,fechas):
    for fecha in fechasmarcas1:
        imagencargada = Image.open('marcas.jpeg')
        escalada = imagencargada.resize((1792, 1024))
        width, height = 1792, 1024
        imagen = Image.new(
            'RGB',
            (width, height),
            color = (255, 0, 0)
            )
        imagen.paste(
            imagencargada,
            (0,0)
            )
        dibujo = ImageDraw.Draw(imagen, "RGBA")

        rectangulocoords= [(0, 800), (1920,1080)]
        negrotransparente = (0,0,0,200)

        try:
            fuente = ImageFont.truetype("parrafo.ttf",120)
            
        except IOError:
            fuente = ImageFont.load_default()

        texto=asgnatura+"- clase "+str(fecha)
        posiciontexto =(200, 860)

        colortexto = (250,250,250)

        dibujo.text(posiciontexto, texto, font=fuente, fill=colortexto)

        ruta = 'imagenes/'+asignatura+'-'+str(fecha)+'.jpg'

        imagen.save(ruta)

fechas = generate_specific_weekday_dates(
    '2024-09-01',
    '2024-06-01',
    2
    )
generaimagenes("marcas.jpg","Lenguaje de Marcas",fechas)

fechas = generate_specific_weekday_dates(
    '2024-09-01',
    '2024-06-01',
    3
    )
generaimagenes("marcas.jpg","Lenguaje de Marcas",fechas)

fechas = generate_specific_weekday_dates(
    '2024-09-01',
    '2024-06-01',
    4
    )
generaimagenes("sistemas.jpg","Sistemas informáticos",fechas)






