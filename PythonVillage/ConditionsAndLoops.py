a = 8
if a < 10:
  print ('the number is less than 10')
else:
  print ('the number is greater or equal to 10')


greetings = 1
while greetings <= 1:
  print ('Hello! ' * greetings)
  greetings = greetings + 1



names = ['Alice', 'Bob', 'Charley']
for name in names:
  print ('Hello, ' + name)



n = 10
for i in range(n):
  print (i)



print (list(range(5, 12)))

soma = 0;
inicial = 4851;
final = 9379;
while inicial <= final:
    if inicial % 2 == 1:
        soma = inicial + soma
    inicial = inicial + 1
print(soma)