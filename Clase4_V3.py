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
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: ")) 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            p = sis.verDatosPaciente(c) 
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
        
if __name__ == "__main__":
    main()    
        
        
        
        
        
        
        
