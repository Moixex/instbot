import requests

# Tu token de acceso de Instagram Graph
access_token = 'IGQWRONXZAuelkxUWFEbGE5YWl3V0QtYjF4Q0ZAzaTk4MEppVmhCTWR5dUxIZAlo5VnhQNmNTMFFneWZAVU3VTa2lTY2FhS3FzMWNJQXJOckkyeDRscFcwZAURGektHdndRQjdLZAFVHeTdVSkFuQkZAPNFJaVmZAoMUdLbUEZD'

# URL de la API de Instagram Graph para subir una foto
url = f'https://graph.instagram.com/me/media?access_token={IGQWRONXZAuelkxUWFEbGE5YWl3V0QtYjF4Q0ZAzaTk4MEppVmhCTWR5dUxIZAlo5VnhQNmNTMFFneWZAVU3VTa2lTY2FhS3FzMWNJQXJOckkyeDRscFcwZAURGektHdndRQjdLZAFVHeTdVSkFuQkZAPNFJaVmZAoMUdLbUEZD}'

# Datos del archivo de imagen a subir
image_file_path = 'ruta/a/tu/imagen.jpg'

# Parámetros de la solicitud
params = {
    'image_url': image_file_path,
    'caption': 'Descripción de tu publicación'
}

# Realizar la solicitud POST para subir la imagen
response = requests.post(url, data=params)

# Analizar la respuesta JSON
response_json = response.json()

# Imprimir la respuesta
print(response_json)
