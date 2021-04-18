def dividir2(numero,pos):
  print ( numero)
  if not(len (numero) < 2):
    #dividir2 (numero[int(len(numero)/2):])
    #dividir2 (numero[:int(len(numero)/2)])
    dividir2 (numero[pos: ],pos)
  
dividir2("1234",1)
          