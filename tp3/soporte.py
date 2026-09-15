class Tratamiento: 
    def __init__(self, dni, nombre, apellido, icd10, montobase, complejidad, algoritmoid):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.icd10 = icd10
        self.montobase = montobase
        self.complejidad = complejidad
        self.algoritmoid = algoritmoid
    
    def __str__(self): # ACOMODAR LOS VALORES {} EN RELACION AL ESPACIO A OCUPAR...
        
        r = "DNI: {:<5} - Nombre: {:<5}- Apellido: {:<5}".format(self.dni, self.nombre, self.apellido)
        r += " - ICD10: {:<5} - Monto Base: {:<5}".format(self.icd10, self.montobase)
        r += " - Complejidad: {:<5} - Algoritmo: {:<5}".format(self.complejidad,self.algoritmoid)
        
        return r

def procesarlinea(linea):
    partes = linea.split(",") # Split lo devuelve en partes, separa en una lista las partes de la cadena segun el criterio ","
    dni = int(partes[0])
    nombre = partes[1]
    apellido = partes[2]
    icd10 = partes[3]
    monto = float(partes[4])
    complejidad = partes[5]
    algoritmo = int(partes[6])

    t = Tratamiento(dni, nombre, apellido, icd10, monto, complejidad, algoritmo)
    return t





        
if __name__ == "__main__":
    linea = "new.csv"
    procesarlinea(linea)