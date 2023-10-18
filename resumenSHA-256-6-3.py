import hashlib

def calcular_sha256(file_path):
    try:
        # Abre el archivo en modo binario
        with open(file_path, "rb") as file:
            # Lee el contenido del archivo
            file_content = file.read()
            
            # Calcula el resumen SHA-256 del contenido
            sha256_hash = hashlib.sha256()
            sha256_hash.update(file_content)
            
            # Devuelve el resumen SHA-256 en formato hexadecimal
            return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)

def comprobar_archivos(archivo1, archivo2):
    try:
        # Leer el contenido de ambos archivos
        with open(archivo1, "r") as file1, open(archivo2, "r") as file2:
            contenido1 = file1.read()
            contenido2 = file2.read()

            # Comprobar si el contenido de archivo2 comienza con el contenido de archivo1
            if contenido2.startswith(contenido1):
                # Calcular el resumen SHA-256 del archivo2
                sha256_summary = calcular_sha256(archivo2)

                # Verificar que el resumen SHA-256 comience con una secuencia de 0s
                if sha256_summary.startswith('0'):
                    return True
                else:
                    return False

        return False
    except Exception as e:
        return False

if __name__ == "__main__":
    archivo1 = input("Ingrese la ruta del primer archivo de entrada: ")
    archivo2 = input("Ingrese la ruta del segundo archivo de entrada: ")

    resultado = comprobar_archivos(archivo1, archivo2)

    if resultado:
        print("Ambas condiciones se cumplen.")
    else:
        print("Al menos una de las condiciones no se cumple.")
