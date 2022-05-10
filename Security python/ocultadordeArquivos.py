import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada ex(C:/pasta")
atributos_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributos_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")