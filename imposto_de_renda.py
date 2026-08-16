print("diga qual opção de salario vc tem:")
print("anual--->1")
print("mensal--->2")
opção_de_sal = int(input())
if opção_de_sal == 1:
    salanual = float(input("digite seu salario anual ex(####.##):"))
    salmensal = salanual/12
    
    
    
    if salmensal <=2428.80:
        print("Seu imposto esta insento")
    elif salmensal >= 2428.80 and salmensal <= 2826.65:
        imposto = salmensal * 0.075
        impostoapagar = (imposto - 182.16) - 312.89
        if impostoapagar <= 0:
            print("seu imposto esta insento")
        else:
            print("o imposto que vc deve pagar é:", impostoapagar)
    elif salmensal >= 2826.66 and salmensal <= 3751.05:
        imposto = salmensal * 0.15
        impostoapagar = (imposto - 394.16) - 312.89
        if impostoapagar <= 0:
            print("seu imposto esta insento")
        else:
            print("o imposto que vc deve pagar é:", impostoapagar)
    elif salmensal >= 3751.06 and salmensal <= 4664.68:
        imposto = salmensal * 0.225
        impostoapagar = (imposto - 675.49) - 312.89
        if impostoapagar <= 0:
            print("seu imposto esta insento")
        else:
            print("o imposto que vc deve pagar é:", impostoapagar)
    elif salmensal > 4664.68:  
        imposto = salmensal * 0.275
        impostoapagar = (imposto - 908.73)
        if salmensal > 4664.68 and salmensal <= 5000:
            impostoapagar = impostoapagar - 312.89
            print("o imposto que vc deve pagar é:", impostoapagar) 
        elif  salmensal >= 5000.01 and salmensal <= 7350:
            impostoapagar = impostoapagar - (978.62 - (0,133145 * salmensal))
            
        if impostoapagar <= 0:
                print("seu imposto esta insento")
        else:
            print("o imposto que vc deve pagar é:", impostoapagar)
        if salmensal >= 7350.01:
            imposto = salmensal * 0.275
            impostoapagar = (imposto - 908.73)
            print("o imposto que vc deve pagar é:", impostoapagar, "não tem redução") 
                
            
     
elif opção_de_sal == 2:
        salmensal = float(input("digite seu salario mensal ex(####.##):"))
        if salmensal <=2428.80:
            print("Seu imposto esta insento")
        elif salmensal >= 2428.80 and salmensal <= 2826.65:
            imposto = salmensal * 0.075
            impostoapagar = (imposto - 182.16) - 312.89
            if impostoapagar <= 0:
                print("seu imposto esta insento")
            else:
                print("o imposto que vc deve pagar é:", impostoapagar)
        elif salmensal >= 2826.66 and salmensal <= 3751.05:
            imposto = salmensal * 0.15
            impostoapagar = (imposto - 394.16) - 312.89
            if impostoapagar <= 0:
                print("seu imposto esta insento")
            else:
                print("o imposto que vc deve pagar é:", impostoapagar)
        elif salmensal >= 3751.06 and salmensal <= 4664.68:
            imposto = salmensal * 0.225
            impostoapagar = (imposto - 675.49) - 312.89
            if impostoapagar <= 0:
                print("seu imposto esta insento")
            else:
                print("o imposto que vc deve pagar é:", impostoapagar)
        elif salmensal > 4664.68:  
            imposto = salmensal * 0.275
            impostoapagar = (imposto - 908.73)
            if salmensal > 4664.68 and salmensal <= 5000:
                impostoapagar = impostoapagar - 312.89
                print("o imposto que vc deve pagar é:", impostoapagar) 
            elif salmensal >= 5000.01 and salmensal <= 7350:
                impostoapagar = impostoapagar - (978.62 - (0.133145 * salmensal))
            if impostoapagar <= 0:
                print("seu imposto esta insento")
            else:
                print("o imposto que vc deve pagar é:", impostoapagar)
            if salmensal >= 7350.01:
                imposto = salmensal * 0.275
                impostoapagar = (imposto - 908.73)
                print("o imposto que vc deve pagar é:", impostoapagar, "não tem redução") 
else:
    print("essa opção não é valida!")
    
