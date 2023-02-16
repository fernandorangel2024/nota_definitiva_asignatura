# Programa para realizar las operraciones, usando las diferentes formulas

print("------------------------------------------")
print("---El resultado de las operaciones son:---")
print("------------------------------------------")

# input
nc = int(input("Digite el valor de la nota cognitiva:"))
np = int(input("Digite el valor de la nota procedimental:"))
na= int(input("Digite el valor de la nota actitudinal:"))
au = int(input("Digite el valor de la nota autoevaluacion:"))
bi = int(input("Digite el valor de la nota bimestral:"))

# processing

nd = (nc*0.3) + (np*0.3) + (na*0.1) + (au*0.1) + (bi*0.2)

# output
print("----------------------------------")
print("---Resultado de las operaciones---")
print("----------------------------------")

print("nota definitiva " + str(nd))