from PIL import Image, ImageDraw, ImageFont

imagencargada = Image.open('marcas.jpeg')

escalada = imagencargada.resize((1792,1024))

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
dibujo = ImageDraw.Draw(imagen)

try:
    fuente = ImageFont.truetype("parrafo.ttf",80)
    
except IOError:
    fuente = ImageFont.load_default()

texto="Lenguaje de Marcas"
posiciontexto =(300,860)
colortexto = (255,255,255)

dibujo.text(posiciontexto, texto, fuente=fuente, fill=colortexto)

ruta = 'imagenes/imagen1.jpg'

imagen.save(ruta)


