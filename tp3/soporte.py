class Tratamiento: 
    def __init__(self, dni, nombre, apellido, icd10, montobase, complejidad, algoritmoid, letra, bloque, montofinal):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.icd10 = icd10
        self.montobase = montobase
        self.complejidad = complejidad
        self.algoritmoid = algoritmoid
        self.letra = letra
        self.bloque = bloque
        self.montofinal = montofinal
    
    def __str__(self): # ACOMODAR LOS VALORES {} EN RELACION AL ESPACIO A OCUPAR...
        r = "DNI: {:<5} - Nombre: {:<5}- Apellido: {:<5}".format(self.dni, self.nombre, self.apellido)
        r += " - ICD10: {:<5} - Monto Base: {:<5} - Complejidad: {:<5}".format(self.icd10, self.montobase, self.complejidad)
        r += "- Algoritmo: {:<5} - Letra: {:<5} - Bloque: {:<5} - Monto Final: {:<5}".format(self.algoritmoid, self.letra, self.bloque, self.montofinal)
        
        return r
    
    
if __name__ == "__main__":
    p = Tratamiento()
    print(p)
        


        
        
        