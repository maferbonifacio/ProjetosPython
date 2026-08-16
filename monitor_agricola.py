print("Monitor Agrícola de Irrigação e Solo\n")

print("Explicação para usuários: A umidade do solo (ou seja, o conteúdo de água do solo/potencial de água do solo) é a fonte imediata de água para a maioria das plantas.\n")

print("O pH do solo é uma medida que indica o nível de acidez ou alcalinidade do solo, utilizando uma escala que varia de 0 a 14. "
      "Esse é um fator fundamental que determina a saúde do solo e a produtividade de plantas em qualquer ambiente.\n")

umidadesolo = float(input("Digite a porcentagem do solo: "))
phsolo = float(input("Digite o nível do PH do solo: "))

print("\n--- DIAGNÓSTICO ---")

if umidadesolo < 30:
    print("Sua irrigação é de", umidadesolo, "%, ou seja, nível CRÍTICO! Você deve ligar bombas no nível máximo.\n")

elif umidadesolo <= 60:
    print("Sua irrigação é de", umidadesolo, "%, ou seja, nível MODERADO. Ligar bombas no nível médio.\n")

else:
    print("A umidade do seu solo é de", umidadesolo, "ou seja, ele está ÚMIDO. Você deve manter a irrigação desligada.\n")

if phsolo < 5.5:
    print("O nível do PH do solo é de", phsolo, "ou seja: ÁCIDO (Recomendado aplicar calcário).")

elif phsolo <= 7:
    print("O nível do PH do solo é de", phsolo, "ou seja, IDEAL.")

else:
    print("O nível do PH do solo é de", phsolo, "ou seja, necessário manejo para redução de pH.")
