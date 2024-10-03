usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
id_usuario = '007'

try:
    print(usuarios[id_usuario])
except KeyError:
    print(f'La clave {id_usuario} no esta en el diccionario, Anyadiendo clave....')
    usuarios[id_usuario] = None
print(usuarios)