conta = 1

print("===========================")
print("CALCULADORA FODA DO PADERU")
print("===========================")

while conta == 1: 

            num1 = float(input("Digite um numero "))
            
            operador = input("")

            num2 = float(input("digite ou numero "))

            if operador == "+":              
                resultado = (num1 + num2)
          
            elif operador == "-":           
               resultado = (num1 - num2)

            elif operador == "*":                
                resultado = (num1 * num2)
            
            elif operador == "/":
                 resultado = (num1 / num2)

            elif operador != "/" or "+" or "*" or "-":
                 print("n e calc cientifica burrao")

            print(resultado)

            if resultado > 100:
                
                print ("resultado invalido")

            pergunta = (input("fazer outra conta? "))

            if pergunta == "nao":
                
                print ("viu oq eu aprendi erick")
                conta = 0       
            
            
            
        
#resto do suposto codigo
                