from PIL import Image, ImageDraw, ImageFont
from funcionsemana import *

fechasmarcas1 = generate_specific_weekday_dates(
    '2024-09-01',
    '2024-06-01',
    2
    )


for fecha in fechasmarcas1:
    imagencargada = Image.open('marcas.jpeg')
    escalada = imagencargada.resize((1920,1080))
    width, height = 1024, 1024
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

    texto="Lenguaje de Marcas - clase "+str(numeroclase)
    posiciontexto =(200, 860)

    colortexto = (250,250,250)

    dibujo.text(posiciontexto, texto, font=fuente, fill=colortexto)

    ruta = 'imagenes/imagen.jpg'+str(fecha)+'.jpg'

    imagen.save(ruta)



