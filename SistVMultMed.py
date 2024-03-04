#No hay polimorfismo
#No hay herencia

# 'asignarNombre','asignarDosis' actuan como setters y 'verNombre','verDosis' actuan getters
# En 'Medicamento' hay constructores ('__init__') para crear un nuevo objeto  de la clase Medicamento.
# En 'Medicamento' hay encapsulamiento ('__')  para proteger los atributos internos de la clase (nombre, dosis y

class Medicamento:
    def __init__(self, nombre="",dosis=0):
        self.__nombre = nombre
        self.__dosis = dosis
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 

#'asignarNombre','asignarHistoria','asignarPeso' actuan como setters y 'verNombre','verHitoria','verPeso' actuan getters
# En 'Mascota' hay encapsulamiento ('__')  para proteger los atributos internos de la clase 
# En 'Mascota' hay constructores ('__init__') para crear un nuevo objeto  de la clase Mascota.        

class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
       
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  
                return True  
        return False 

def main():
    servicio_hospitalario = sistemaV()
    
    while True:
        try:

            menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
            if menu==1: 
                if servicio_hospitalario.verNumeroMascotas() >= 10:
                        print("No hay espacio ...") 
                        continue
                historia=int(input("Ingrese la historia clínica de la mascota: "))
                if not servicio_hospitalario.verificarExiste(historia):
                    nombre = input("Ingrese el nombre de la mascota: ")
                    tipo = input("Ingrese el tipo de mascota (felino o canino): ")
                    peso = ("Ingrese el peso de la mascota: ")
                    fecha = ("Ingrese la fecha de ingreso (dia/mes/año): ")
                    nm = ("Ingrese cantidad de medicamentos: ")
                    lista_med = []

                    for i in range (nm):
                        nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                        dosis = int(input("Ingrese la dosis: "))
                        medicamento = Medicamento(nombre_medicamento, dosis)
                        lista_med.append(medicamento)

                    mas= Mascota()
                    mas.asignarNombre(nombre)
                    mas.asginatHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)
                    mas.asignarLista_Medicamentos(lista_med)
                    servicio_hospitalario.ingresarMascota(mas)
                
                else:
                    print("Ya existe la mascota con el numero de historia clinica")

            elif menu ==2:
                historia = int(input("Ingrese la historia clinica de la mascota"))
                fecha = servicio_hospitalario.verFechaIngreso(historia)
                if fecha is not None:
                    print("La fecha de ingreso de la mascota es: " + fecha)

                else: 
                    print("La historia clinica ingresada no corresponde con ninguna mascota en el sistema. ")

            elif menu ==3:
                numero = servicio_hospitalario.verNumeroMascotas()
                print("El numero de pacientes en el sistema es: " + str(numero))

            elif menu == 4:
                historia = int(input("Ingrese la historia clinica de la mascota: "))
                medicamento = servicio_hospitalario.verMedicamento(historia)
                if medicamento is not None:
                    print("Los medicamento suministrados son: ")
                    for m in medicamento:
                        print(f"\n- {m.verNombre()}")

                else:
                    print("la historia clinica ingresada no corresponde con ninguna mascota del sistema")

            
            elif menu == 5:
                historia = int(input("Ingrese ka historia clinica de la mascota: "))
                resultado_operacion = servicio_hospitalario.eliminarMascota(historia)
                if resultado_operacion:
                    print("Mascota eliminada del sistema con exito")

                else:
                    print("No se ha podido eliminar la mascota")

            
            elif menu == 6:
                print ("Usted ha salido del sistema de servicion de hospitalizacion...")
                break

            else:
                print("Usted ingresó una opcion no valida, intentelo nuevamente...")

        except ValueError:
            print("Error: Ingrese un valor numerico valido")


if __name__ ==  '__main__':
    main()

            





            

                

