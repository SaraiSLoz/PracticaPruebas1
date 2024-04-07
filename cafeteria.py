def es_entero(numero):
    # Verificar si el número es un entero
    return numero.is_integer()

def validar_enteros(tamanos):
    # Validar si todos los tamaños son enteros
    return all(es_entero(tam) for tam in tamanos)

def validar_bebida(entrada):
    # Eliminar espacios en blanco de la entrada
    entrada = entrada.replace(' ', '')
    
    # Dividir la entrada en el nombre de la bebida y los tamaños
    partes = entrada.split(",", 1)
    
    if '' in partes:
        return False
    
    nombre, tamanos_str = partes
    # Validar el nombre de la bebida(si contiene letras del abecedario) y su tamaño
    if not nombre.isalpha() or len(nombre) < 2 or len(nombre) > 15:
        return False
    
    #pasar a decimal para después comprobar en enteros
    tamanos_float = [float(tam) for tam in tamanos_str.split(',')]

    # Verificar si los tamaños son enteros
    if not validar_enteros(tamanos_float):
        return False
    # Convertir los tamaños a una lista de enteros
    tamanos = [int(tam) for tam in tamanos_str.split(',')]
    
    # Verificar que los tamaños estén en orden ascendente
    if tamanos != sorted(tamanos):
        return False

    # Verificar que haya máximo cinco tamaños y que sean enteros dentro del rango de 1 a 48
    if len(tamanos) > 5 or any(tam < 1 or tam > 48 for tam in tamanos):
        return False
    
    return True
