notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))
notaC = float(input("Digite a terceira nota: "))
mediaAluno = (notaA + notaB + notaC)/3
if mediaAluno >= 6:
    print(f"O aluno passou com a média de {mediaAluno:.2f}")
else:
    print(f"O aluno foi reprovado com a media de {mediaAluno:.2f}, faltou {6-mediaAluno:.2f} para ser aprovado")