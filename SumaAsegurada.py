from abc import ABC, abstractmethod

class VerificadorDatos(ABC):
    @abstractmethod
    def verificar_fumador(self):
        pass

    @abstractmethod
    def verificar_sexo(self):
        pass

    @abstractmethod
    def verificar_extra_prima(self):
        pass

    @abstractmethod
    def verificar_edad(self):
        pass

    @abstractmethod
    def verificar_suma_asegurada(self):
        pass

class Persona(VerificadorDatos):
    def __init__(self, X, F, S, EP, SA):
        self.fumador = self.verificar_fumador(F)
        self.sexo = self.verificar_sexo(S)
        self.EP = self.verificar_extra_prima(EP)
        self.anos1 = self.verificar_edad(X)
        self.SA = self.verificar_suma_asegurada(SA)
        self.edad = max(18, min(self.anos1, 99))
        self.fe = self.fe()  # Supongo que tienes una implementación para este método

    def verificar_fumador(self, F):
        while F != 'Si' and F != 'No':
            F = input('¿Es usted fumador? (Si, No)')
        return F

    def verificar_sexo(self, S):
        while S != 'M' and S != 'F':
            S = input('¿Cuál es su sexo? (F, M)')
        return S

    def verificar_extra_prima(self, EP):
        while EP != 'Si' and EP != 'No':
            EP = input('¿Usted tiene extra prima? (Si, No)')
        return EP

    def verificar_edad(self, X):
        while X < 18 or X > 99:
            X = int(input('Ingrese su edad (18 años-99 años)'))
        return X

    def verificar_suma_asegurada(self, SA):
        while SA < 500000 or SA > 3000000:
            SA = float(input('¿Cuál es la suma que desea asegurar? (no mayor a 3,000,000 MXN ni menor a 500,000 MXN)'))
        return SA


    def anos(self):
      #Calcula la edad luego de las consideraciones de la aseguradora
      if self.fumador == "No":
          self.anos1 += -5

      if self.sexo == "F":
          self.anos1 += -10

      if self.EP == "Si":
        self.anos1 += 10

      return self.anos1

    def fe(self):
      if self.sexo == 'F':
        if self.edad < 25:
          self.fe = self.edad*1.5
        elif self.edad < 45:
          self.fe = self.edad*1.7
        elif self.edad < 65:
          self.fe = self.edad*2
        else:
          self.fe = self.edad*2.2
      else:
        if self.edad < 25:
          self.fe = self.edad*2
        elif self.edad < 45:
          self.fe = self.edad*2.3
        elif self.edad < 69:
          self.fe = self.edad*2.5
        else:
          self.fe = self.edad*3

      return self.fe

    def carnet(self):
      P = self.costo_prima()
      C = self.conversion()
      x = print(f'\n CARNET \n Edad: {self.anos1} \n Sexo: {self.sexo} \n Fumador = {self.fumador} \n Indicador de extra prima: {self.EP} \n Suma asegurada: ${self.SA} \n Costo de prima(MXN): ${P} \n Costo de prima(USD): ${C}')
      return x

    def costo_prima(self):
        P = self.SA * self.fe / 1000
        return P

    def conversion(self):
        P = self.costo_prima()
        C = P/21.13
        return C

X = int(input('Ingrese su edad (18 años-99 años)'))
F = input('¿Usted fuma con regularidad? (Si, No)')
S = input('¿Cuál es su sexo? (F, M)')
EP = input('¿Usted tiene extra prima? (Si, No)')
SA = float(input('¿Cuál es la suma que desea asegurar? (no mayor a 3,000,000 MXN ni menor a 500,000 MXN)'))

a = Persona(X,F,S,EP,SA)
a.carnet()