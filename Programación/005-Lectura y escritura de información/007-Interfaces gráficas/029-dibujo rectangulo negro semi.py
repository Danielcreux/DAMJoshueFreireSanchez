from PIL import Image, ImageDraw, ImageFont

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

rectangulocoords= [(0, 700), (1920,1080)]
negrotransparente = (0,0,0,200)

try:
    fuente = ImageFont.truetype("parrafo.ttf",80)
    
except IOError:
    fuente = ImageFont.load_default()

texto="Lenguaje de Marcas"
posiciontexto =(200, 860)

colortexto = (250,250,250)

dibujo.text(posiciontexto, texto, font=fuente, fill=text_color)

ruta = 'imagenes/imagen.jpg'

imagen.save(ruta)


