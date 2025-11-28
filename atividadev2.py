while True:
    try:
        v1 = float(input("digite o valor 1:"))
        op = input('digite o operador:')
        v2 = float(input('digite o valor 2:'))

        operadores = {"+", "-", "/", "*"}

        if op not in operadores:
            raise ValueError('Erro: operador invalido')
        
        if op == "/" and v2 == 0:
            raise ZeroDivisionError('Não é possivel dividir por zero!!')
        if op == "+":
            res = v1 + v2
        elif op == "-":
            res = v1 - v2
        elif op == "/":
            res = v1/v2
        elif op == "*":
            res = v1*v2

        print(f"Resultado: {v1} {op} {v2} = {res}")

        break

    except ValueError as ve:
        print(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")
    except Exception as e:
        print(f"Erro: {e}")
