#Programa para definir se um aluno está aprovado, em recuperação ou reprovado

nota = float(input("Digite a nota: "))
if nota >= 6.0 and nota <= 10.0:
    print("Aluno(a) APROVADO! ")
elif nota > 4.0 and nota < 6.0:
    print("Aluno em RECUPERAÇÃO!")
else:
    print("Aluno(a) REPROVADO!")