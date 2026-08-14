soma = 0

for i in range(5):
    num = float(input("Digite um numero a ser somado: "))
    soma += num
    if soma == 67:
        while soma == 67:
            print(soma)

print(f"O total da soma foi: {soma}")