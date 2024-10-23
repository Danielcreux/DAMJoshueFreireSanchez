from PIL import Image

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

ruta = 'imagenes/imagen.jpg'

imagen.save(ruta)


