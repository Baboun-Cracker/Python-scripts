import zipfile

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
	my_zip.write('caesar.py') # ça ne créer pas des fichiers vides,
	my_zip.write('favicon.png') # ça copie les fichiers locaux

with zipfile.ZipFile('files.zip', 'r') as my_zip:
	print(my_zip.namelist()) # les noms des fichiers contenus
	my_zip.extractall('files') # extraction de tous les fichiers vers le dossier files
	my_zip.extract('caesar.py') # extrait seulement le fichier caesar.py