# Cargar datos por teclado

nombre = input("Ingrese su nombre: ")
codigo = input("Ingrese su codigo: ")
montobase = int(input("Ingrese su monto base: "))

# En caso de error: Codigo Inválido.

if len(codigo) != 5 or not codigo[1:5]:
    print("Código inválido")
else:

    letra = codigo[0]
    numeral = int(codigo[1]) + int(codigo[2])
    montofinal = 0
    porcentaje = int(codigo[4])
    montofijo = 25000
    montoporletra = 0
    enfermedad = ""
    descuento = 0

    #   Agregado del monto base por letra

    if letra == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L":
        montoporletra = 25000
    elif letra == "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "V" or "W" or "X" or "Y" or "Z":
        montoporletra = 40000
    elif letra == "U":
        montoporletra = 100000

    #   Capitulos con su enfermedad

    if letra == "A" or letra == "B":
        enfermedad = "Ciertas enfermedades infecciosas y parasitarias"
    elif letra == "C" or (letra == "D" and numeral <= 48):
        enfermedad = "Tumores [neoplasias]"
    elif letra == "D" and numeral >= 50 or (letra == "D" and numeral <= 89):
        enfermedad = "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad"
    elif letra == "E":
        enfermedad = "Enfermedades endocrinas nutricionales y metabolicas"
        if porcentaje > 5:
            porcentaje = 37
    elif letra == "F":
        enfermedad = "Trastornos mentales y del comportamiento"
        if porcentaje % 2 == 0:
            porcentaje = 45
    elif letra == "G":
        enfermedad = "Enfermedades del sistema nervioso"
    elif letra == "H" and numeral >= 59:
        enfermedad = "Enfermedades del ojo y sus anexos"
    elif letra == "H" and numeral >= 60 or (letra == "H" and numeral <= 95):
        enfermedad = "Enfermedades del oído y de la apófosis mastoides"
    elif letra == "I":
        enfermedad = "Enfermedades del sistema circulatorio"
    elif letra == "J":
        enfermedad = "Enfermedades del sistema respiratorio"
    elif letra == "K" and numeral <= 93:
        enfermedad = "Enfermedades del sistema digestivo"
    elif letra == "L":
        enfermedad = "Enfermedades de la piel y del tejido subcutáneo"
    elif letra == "M":
        enfermedad = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
    elif letra == "N":
        enfermedad = "Enfermedades del sistema genitourinario"
    elif letra == "O":
        enfermedad = "Embarazo parto y puerperio"
    elif letra == "P" and numeral <= 96:
        enfermedad = "Ciertas afecciones originadas en el periodo perinatal"
    elif letra == "Q":
        enfermedad = "Malformaciones congénitas, deformidades y anomalías cromosómicas"
    elif letra == "R":
        enfermedad = "Sintomas, signos y hallazgos anormales clinicos y de laboratorio, no clasificados en otra parte"
    elif letra == "S" or (letra == "T" and numeral <= 98):
        enfermedad = "Traumatísmos, envenenamientos y algunas otras consecuencais de causas externas"
    elif letra == "V" and numeral >= 1 or (letra == "Y" and numeral <= 98):
        enfermedad = "Causas externas de morbilidad y de mortalidad"
    elif letra == "Z":
        enfermedad = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
    elif letra == "U":
        enfermedad = "Codigos para propósitos especiales"

    #   Calculo del monto final

    if porcentaje > 50:
        montocompleto = (montobase + montofijo + montoporletra)
        montofinal = montocompleto



    if letra == "E" or "F":
        if montofinal > montocompleto / 2:
            porcentaje = 0
        else:
            montocompleto = (montobase + montofijo + montoporletra)
            montofinal = montocompleto - (montocompleto * (porcentaje / 100))


    else:
        montocompleto = (montobase + montofijo + montoporletra)
        montofinal = montocompleto + (montocompleto * (porcentaje / 100))

    # Dar en pantalla los valores correspondientes

    print("Nombre:", nombre)
    print("Codigo:", codigo)
    print("Capítulo:", enfermedad)
    print("Monto final: $", montofinal)

