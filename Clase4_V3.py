# NO hay herencia
# No hay polimorfismo

# el constructor ('__init__') se encuentra en las clases 'Paciente' y 'Sistema'
# Hay encapuslamiento en pacientes para mantener los atributos privados
class Paciente:

    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
 # los metodos 'verNombre(),'verCedula()','verGenero()','verServicio()' son getters             
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 

 # los metodos 'asignarNombre(n)','asignarCedula(c)','asignarGenero(g)'. son setters  
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self,cedula):
        return any(cedula == p.verCedula() for p in self.__lista_pacientes)
        
    def ingresarPaciente(self,pac):
        if not self.verificarPaciente(pac.verCedula()):
            self.__lista_pacientes.append(pac)
            return True
        return False
            

    def verDatosPaciente(self, c):
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    
            
    def verNumeroPacientes(self):
        print(f"En el sistema hay:{len(self.__lista_pacientes)} pacientes")

def main():
    sis = Sistema() 
    
    while True:
        print("\nMenu:")
        print("0. salir")
        print("1. Ingresar nuevo paciente")
        print("2. Ver datos de un paciente")
      
        opcion = input("Ingrese  una opción del menú: ")

        if opcion == "0":
            break
       
        if opcion == "1":
            
            print("A continuacion se solicitaran los datos ...") 
          
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                
                pac = Paciente() 
                
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            c = int(input("Ingrese la cedula a buscar: ")) 
            p = sis.verDatosPaciente(c) 
            
            if p:
                print(f"Nombre:{p.verNombre()}") 
                print(f"Cedula: {p.verCedula()}")
                print(f"Genero: {p.verGenero()}")
                print(f"Servicio: {p.verservicio()}")
            
            else:
                print("No existe un paciente con esa cedula") 
        else:
            print("Opcion no valida. Intente nuevamente")
    
            break 

        
if __name__ == "__main__":
    main()    
        
        
        
        
        
        
        
