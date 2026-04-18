class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b

def calculadora_interativa():
    calc = Calculadora()

    # O "map" de funções
    # Guardamos a referência do método, sem os parênteses ()
    operacoes = {
        "+": calc.somar,
        "-": calc.subtrair,
        "*": calc.multiplicar,
        "/": calc.dividir
    }

    print("Bem-vindo à Fantástica Calculadora Python!")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        nome = input("Qual seu nome? ")

        if nome.lower() == 'sair':
            print("Até logo!")
            break

        entrada = input("Operação (ex: 10 + 5): ").lower()

        if entrada.lower() == 'sair':
            print("Até logo!")
            break  # Encerra o loop

        try:
            num1_str, operador, num2_str = entrada.split()
            num1, num2 = float(num1_str), float(num2_str)

            # Aqui acontece a mágica:
            if operador in operacoes:
                tarefa = operacoes[operador] # Pega a função no dicionário
                resultado = tarefa(num1, num2) # Executa a função
                print(f"{nome}, o resultado de {num1} {operador} {num2} é: {resultado}\n")
            else:
                print("Operador não reconhecido!")
            
        
        except ValueError:
            print("Erro: Formato inválido. Use: numero operador numero")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    calculadora_interativa()