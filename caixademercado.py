print("Caixa do Varejo - Mercado BOM-BOM")

colocarcpf = str(input("Cliente deseja colocar CPF? (S/N):"))

if colocarcpf.lower() == 's':
        cpfcliente = str(input("CPF cliente:"))

while True:
        nomeproduto = str(input("Nome do Produto:"))
        quantidade = int(input("Quantidade:"))
        preco = float(input("Valor individual do Produto:"))
        totalproduto = (quantidade * preco)

        print(f"O total da compra do CPF número: {cpfcliente}, foi de {totalproduto:.2f} reais.")
          
        recomecar = str(input("Deseja registrar outra compra? (S/N):"))

        if recomecar.lower() == 's':
            print("Próxima compra...")

        else:
            print("Caixa encerrado")
            break