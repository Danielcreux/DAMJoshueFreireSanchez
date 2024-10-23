from PIL import Image, ImageDraw, ImageFont

for numeroclase in range(0,10):
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

    ruta = 'imagenes/imagen.jpg'+str(numeroclase)+'.jpg'

    imagen.save(ruta)



