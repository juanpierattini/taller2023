def validar_rut(rut):
## Verificar si rut  cumple formato XX.XXX.XXX-X
    if len(rut) != 12 or rut[2] != '.' or rut[6] != '.' or rut[10] != '-':
        return False

## Retira los puntos desde el 0 al 9
    digitos = rut[:10].replace('.', '')
    digito_verificador = rut[11]

    if not digitos.isdigit():
        return False

    # Calculando digito verificador
    suma = 0
    multiplicador = 2
    for digito in reversed(digitos):
        suma += int(digito) * multiplicador
        multiplicador = (multiplicador + 1) % 8 or 2

    resto = suma % 11
    digito_esperado = str(11 - resto) if resto else '0'
    return digito_esperado == digito_verificador

# Pidiendo rut
rut_ingresado = input("Ingresa tu RUT(en formato XX.XXX.XXX-X): ")

if validar_rut(rut_ingresado):
    print("El RUT es válido.")
else:
    print("El RUT no es válido. Ingresa un RUT en el formato correcto.")
