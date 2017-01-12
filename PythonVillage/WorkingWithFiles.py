
f = open('teste.txt', 'r')

#print(f.readline().strip() + ' "próxima linha" ' + f.readline())
print(f.readlines())

f = open('teste.txt', 'r')
print(f.readlines()[1])

f = open('teste.txt', 'r')
for line in f:
    print (line.split())


f = open('teste.txt', 'w')
f.write('famfafsom \nápkfak \nwkfkwq\nwopfjojfẃ\n')


f = open('teste.txt', 'a')
inscription = 'Rosalind Elsie Franklin ', 1920, 1958
s = str(inscription)
f.write(s + '\n')

for i in inscription:
  f.write(str(i) + '\n')

f.close()

p = open('rosalind_ini5.txt', 'r')
r = open('Resposta.txt', 'w')



for index, text in enumerate(p):
    if index % 2 == 1:
        r.write(text)
    #print(index)

p.close()
r.close()