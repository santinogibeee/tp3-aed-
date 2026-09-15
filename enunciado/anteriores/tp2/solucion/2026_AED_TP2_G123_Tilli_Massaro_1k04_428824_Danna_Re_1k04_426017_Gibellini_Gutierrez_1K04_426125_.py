#Caracter 0: Es siempre un numeral (#)
#Caracter 1: Es siempre un espacio
#Caracteres del 2 al 7 (6 caracteres) el monto para A-L
#Caracteres del 8 al 13 (6 caracteres) el monto para M-Z (sin U)
#Caracteres del 14 al 19(6 caracteres) el monto para la letra U.

def procesar_linea(linea):
    nombre = linea[:25]
    icd10 = linea[25: 31]
    base = int(linea[31:39])
    alta_comp = linea[39:]


    return nombre, icd10, base, alta_comp


def procesar_linea_especial(linea):
    monto_AL = monto_MZ = monto_U = 0
    monto_AL = int(linea[2 : 8])
    monto_MZ = int(linea[8 : 14])
    monto_U = int(linea[14 :20])
    return monto_AL, monto_MZ, monto_U


def porcentaje(icd10):
    porc = int(icd10[4: ])
    return porc

def letra(icd10, r2, r3, r4, r5, r6):

    if icd10[0] in "ABCEP":
        if icd10[0] == "A":
            r2 += 1
        if icd10[0] == "B":
            r3 += 1
        if icd10[0] == "C":
            r4 += 1
        if icd10[0] == "E":
            r5 += 1
        if icd10[0] == "P":
            r6 += 1
    return r2, r3, r4, r5, r6

def calcular_monto_final(base, icd10, alta_comp, monto_AL, monto_MZ, monto_U):
    inicial = icd10[0]

    if inicial == "U":
        extra = monto_U
    elif "A" <= inicial <= "L":
        extra = monto_AL
    else:
        extra = monto_MZ

    subtotal = base + extra
    porc = porcentaje(icd10)
    subtotal = subtotal + subtotal * porc / 100

    if alta_comp == "X":
        subtotal = subtotal * 1.05 # esto suma el 5%

    return subtotal

def monto_menor(base, monto_final, menor_base, r11):
    if menor_base is None or base < menor_base:
        menor_base = base
        r11 = monto_final
    return menor_base, r11




def no_es_U(icd10, nombre, monto_final, r8 , r9):
    if icd10[0] != "U":
        if monto_final > r9:
            r9 = round(monto_final, 2)
            r8 = nombre
    return r8, r9


#Resultado r10: El porcentaje entero que representaron los tratamientos identificados
# como de alta complejidad cuyo monto final superó el promedio pagado por TODOS
# los tratamientos, respecto del total de tratamientos identificados como de alta
# complejidad.

def total_tratamientos(monto_final, total):
    total = total + monto_final
    return total

def promedio_todos(total, r1):
    prom = total/r1
    return prom

def monto_final_X(monto_final, alta_comp, prom, x , x_totales):
    if alta_comp == "X":
        x_totales += 1
        if monto_final > prom:
            x += 1
    return x,x_totales

def porcentaje_de_alta_complejidad(x, x_totales):
    resultado10 = (x/x_totales)*100
    return resultado10




def principal():
    m = open("tratamientos.txt")
    bandera = False
    menor_base = None
    montofinal = 0
    suma_cap19 = 0
    cant_cap19 = prom = 0
    total = 0
    r1 = 0
    r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = r10 = r11 = 0
    x = 0
    x_totales = 0

    for linea in m:
        if linea[-1] == "\n":
            linea = linea[:-1]


        if linea[0] == "#":
            monto_AL, monto_MZ , monto_U = procesar_linea_especial(linea)
            bandera = True


        else:
            nombre, icd10, base, alta_comp = procesar_linea(linea)
            r1 += 1
            r2, r3, r4, r5, r6 = letra(icd10, r2, r3, r4, r5, r6)
            monto_final = calcular_monto_final(base, icd10, alta_comp, monto_AL, monto_MZ, monto_U)
            if icd10[0] == "S" or icd10[0] == "T":
                suma_cap19 += monto_final
                cant_cap19 += 1
            r8 , r9 = no_es_U(icd10, nombre, monto_final, r8, r9)
            total = total_tratamientos(monto_final, total)
            if bandera and alta_comp == "X":
                menor_base, r11 = monto_menor(base, monto_final, menor_base, r11)
            bandera = False




    prom = promedio_todos(total, r1)
    r7 = round(suma_cap19 / cant_cap19, 2)
    print('(r1) - Cantidad de tratamientos cargados:', r1)
    print('(r2) - Cantidad de tratamientos "A":', r2)
    print('(r3) - Cantidad de tratamientos "B":', r3)
    print('(r4) - Cantidad de tratamientos "C":', r4)
    print('(r5) - Cantidad de tratamientos "E":', r5)
    print('(r6) - Cantidad de tratamientos "P":', r6)
    print('(r7) – Importe final promedio (capítulo 19):', r7)
    print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8)
    print('(r9) - Mayor importe pagado por ese paciente):', r9)


    #Segundo for: necesito el promedio ya calculado para comparar cada monto, sino me da división sobre 0.
    m2 = open("tratamientos.txt")
    for linea in m2:
        if linea[-1] == "\n":
            linea = linea[:-1]
        if linea[0] == "#":
            monto_AL, monto_MZ , monto_U = procesar_linea_especial(linea)
        else:
            nombre, icd10, base, alta_comp = procesar_linea(linea)
            monto_final = calcular_monto_final(base, icd10, alta_comp, monto_AL, monto_MZ, monto_U)
            x, x_totales = monto_final_X(monto_final, alta_comp, prom, x, x_totales)
    r10 = int(porcentaje_de_alta_complejidad(x, x_totales))
    print('(r10)- Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)
    print('(r11):', r11)

if __name__ == "__main__":
    principal()

