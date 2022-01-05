import os
import humanize

# Obtiene todos los ficheros

search_dir = os.listdir('/')

print(search_dir)

# Recorre todos los archivos

downloads = '/home/ken/Descargas'

with os.scandir(downloads) as all_content:
    for content in all_content:
        print(content.name)

# Imprime en pantalla sólo los ficheros

with os.scandir(downloads) as specific_content:
    specific_content = [file.name for file in specific_content if file.is_file()]

print(specific_content)

# Lista los tamaños de los ficheros en formato human friendly

all_files = filter(lambda x: os.path.isfile(os.path.join(downloads, x)), os.listdir(downloads))

files_sizes = [(content, os.stat(os.path.join(downloads, content)).st_size) for content in all_files]

for content, size in files_sizes:
    print(content, ': ', (humanize.naturalsize(size)))

