class Profile:
    ##Atributos##
    #username = ""
    #email = ""
    #password = ""
    ##Fin Atributos
    def __init__(self, id, username, email, password, status = "online", level = 0):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.level = level
    
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password

    def get_status(self):
        return self.status

    def get_level(self):
        return self.level

    def set_id(self,number):
        if number < 0:
            print("id invalido, ingrese un id superior a 0")
        else:
            self.id = number
    
    def set_username(self, name):
        self.username = name

    def set_email(self, correo):
        self.email = correo
        
    def set_password(self, contraseña):
        self.password = contraseña
        
    def set_status(self, estado):
        self.status = estado
        
    def set_level(self, nivel):
        if nivel <=0:
            print("nivel invalido, ingrese un nivel valido")
        else:
            self.level = nivel

    




profile1 = Profile("1", "sad", "asd", "sad", "asd", "5")

profile1.set_id(200000)

# empleado_1.salary=2000000
print(profile1.get_id())
#print(empleado_1.salary)

print(profile1.set_id)