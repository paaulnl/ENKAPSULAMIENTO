##Encapsulamiento 
##- Mejora el control de acceso a los datos
##- Filtra acceso a los datos
##- Mayor seguridad del sistema
## _ es protegida y __ es privado

## INICIO SIN ENCAPSULAMIENTO
class Employe:
    def __init__(self,full_name,salary):
        self.full_name = full_name
        self.salary = salary
        
empleado_1 = Employe("Juanito Alimaña",20000)

empleado_1.salary = 2012314
print(empleado_1.salary)
print(empleado_1.salary)

##FIN DE SIN ENCAPSULAMIENTO 
## INICIO DE ENCAPSULAMIENTO    _
class Employe:
    def __init__(self,full_name,salary):
        self.full_name = full_name
        self._salary = salary
    ## metodo publico que me devuelve un dato privado/protegido    
    def get_salary(self):
        return self._salary
    
    def set_salary(self,value):
        self._salary = value 
        
empleado_1 = Employe("Juanito Alimaña",20000)


empleado_1.salary = 2012314
print(empleado_1.salary)
print(empleado_1.salary)