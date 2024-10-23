from PIL import Image

# Definir el tamaño de la imagen (ancho, alto) y el color (en este caso, blanco)
width, height = 800, 600
color = (255, 255, 255)  # Blanco (RGB)

# Crear una imagen en blanco
blank_image = Image.new('RGB', (width, height), color)

# Guardar la imagen en formato PNG
blank_image.save('blank_image.png')

# Mostrar el mensaje cuando la imagen se guarda correctamente
print("Imagen en blanco generada y guardada como 'blank_image.png'.")
