from PIL import Image, ImageDraw, ImageFont
from funcionsemana import *


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
        rectangulocoords= [(0, 800), (1792,1024)]
        negrotransparente = (255,255,255,200)
        dibujo.rectangle(rectangulocoords, fill=negrotransparente)

         imagen.logo=Imagen.open("tame.png").convert("RGBA")
        imagen.paste(imagenlogo(1450,850))

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

inicio = '2024-09-01'
final = '2024-10-01'


fechas = generate_specific_weekday_dates(inicio,final, 2)
generaimagenes("marcas.jpg","Lenguaje de Marcas",fechas)






