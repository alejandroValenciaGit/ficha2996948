a = 5;
b = 6;
c = a+b;

print(c);


num1 = int(input("Escriba un numero "));
num2 = int(input("Escriba otro numero "));
op = input("Escribe la operacion ")
suma = num1+num2;
resta = num1-num2;
multiplicacion = num1*num2;
division = num1/num2;
potencia = num1**num2
print('El total de la suma es; ', suma);
print('El resultado de la resta es; ', resta);
print('El producto de la multiplicacion es; ', multiplicacion);
print('El cociente de la division es; ', division);
print("La potencia es; ", potencia);

if op == '+':
    print('El total de la suma es; ', suma);
elif op == '-':
    print('El resultado de la resta es; ', resta);
elif op == '*':
    print('El producto de la multiplicacion es; ', multiplicacion);
elif op == '/':
    print('El cociente de la division es; ', division);
elif op == '**':
    print("La potencia es; ", potencia);
else:
    print("Asigne valores validos")



