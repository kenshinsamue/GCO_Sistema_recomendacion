import sys
import math

class Matriz:

  def __init__(self):
    self.linea = []
    self.valores = []
    self.pos =[]
    self.sim = []
    pass
  
  def NuevaLinea(self, linea):
    self.linea.append(linea) 
  
  def DarFormato(self):
    size = len(self.linea)
    vector = []
    for x in range(size):
      linea = self.linea[x]
      for y in linea: 
        if linea[0] != " " and linea[0] != "\n":
          vector.append(linea[0])
          linea = linea[1:]
        else:
          linea = linea[1:]
      self.valores.append(vector)
      vector = []

  def Buscar (self):
    for y in range(len(self.valores)):
      for x in range(len(self.valores[y])):
        if (self.valores[y][x]=="-"):
          self.pos = [y,x]
          # 0,4
          break

  def Calcular (self):
    self.Buscar()
    print("Seleccione una de las siguientes opciones :")
    print("1)Correlacion de Pearson")
    print("2)Distancia Coseno")
    print("3)Distancia Euclidea")
    metodo = input()
    if metodo == "1":
      self.Pearson()
      print(self.sim)
    if metodo == "2":
      self.Coseno()
      print(self.sim)
    if metodo == "3":
      self.Euclideo()
      print(self.sim)
      
  def Euclideo(self):
    for y in range(len(self.valores)):
      if(y != self.pos[0]):
        distancia =0
        for i in range(len(self.valores[y])):
          if i != self.pos[1] and self.valores[y][i] != "-":
            p = float(self.valores[self.pos[0]][i]) - float(self.valores[y][i])
            distancia = distancia + pow((p),2)
        sim = math.sqrt(distancia)
        self.sim.append(sim) 

  def Coseno(self):
    for y in range(len(self.valores)):
      if(y != self.pos[0]):
        nominador = 0.0
        # calculamos el nominador
        for i in range(len(self.valores[y])):
          if i != self.pos[1] and self.valores[y][i] != "-":
            nominador = nominador + ((float(self.valores[self.pos[0]][i]))*(float(self.valores[y][i])))
        # Calculamos el denominador
        denominador = 0.0
        primero = 0
        segundo =0
          #calculamos los valores dentro de ambas raices cuadradas 
        for i in range(len(self.valores[y])):
          if i != self.pos[1] and self.valores[y][i] != "-":
            primero = primero + pow((float(self.valores[self.pos[0]][i])),2)
            segundo = segundo + pow((float(self.valores[y][i])),2)
          # aplicamos ambas raices
        primero = math.sqrt(primero)
        segundo = math.sqrt(segundo)
        # obtenemos el valor final del sim(u,v)
        denominador = primero * segundo
        sim = nominador / denominador
        self.sim.append(sim)
    pass
  def MediaUsuario(self,pos_usuario):
    media_u = 0
    contador =0
    for x in range(len(self.valores[pos_usuario])):
      if(self.valores[pos_usuario][x]!="-"):
        media_u = media_u + float(self.valores[pos_usuario][x])
        contador = contador + 1
    media_u = media_u/contador
    return media_u
  
  def Pearson(self):
    Media_usuario = self.MediaUsuario(self.pos[0])
    Media_usuario_nuevo =0.0
    for y in range(len(self.valores)):
      if(y != self.pos[0]):
        Media_usuario_nuevo = self.MediaUsuario(y)
        nominador = 0.0
        # calculamos el nominador
        for i in range(len(self.valores[y])):
          if i != self.pos[1] and self.valores[y][i] != "-":
            nominador = nominador + ((float(self.valores[self.pos[0]][i])-Media_usuario)*(float(self.valores[y][i])-Media_usuario_nuevo))
        # calculamos el denominador
        denominador = 0.0
        primero = 0
        segundo =0
          #calculamos los valores dentro de ambas raices cuadradas 
        for i in range(len(self.valores[y])):
          if i != self.pos[1] and self.valores[y][i] != "-":
            primero = primero + pow((float(self.valores[self.pos[0]][i])-Media_usuario),2)
            segundo = segundo + pow((float(self.valores[y][i])-Media_usuario_nuevo),2)
          # aplicamos ambas raices
        primero = math.sqrt(primero)
        segundo = math.sqrt(segundo)
        # obtenemos el valor final del sim(u,v)
        denominador = primero * segundo
        sim = nominador / denominador
        self.sim.append(sim)

# ------------------------------------------------------------
def main ():
  # primer elemento de los argumentos
  # python example.py one two three
  # ['example.py', 'one', 'two', 'three']
  matriz = sys.argv[1]
  # leer ficheros
  f = open(matriz,"r")
  mi_matriz = Matriz()
  while True:
    line = f.readline()
    if(""==line):
      break
    else:
      mi_matriz.NuevaLinea(line)

  f.close()
  
  mi_matriz.DarFormato()
  mi_matriz.Calcular()

main()