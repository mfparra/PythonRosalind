

# We've already used lists and strings to store and process bunch of data.
# Python also has a variable type to matching one items (i.e. keys) to others (i.e. values) called dictionary.
# Dictionary is similar to list but instead of automatic index you provide your own index called key.
# You can assign data to a dictionary as follows: phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}.
# As with lists for a value could be used any type: string, number, float even dict or list.
# For keys you can use only strings, numbers, floats and other immutable types. Accessing values also similar to lists:

phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
print (phones['Zoe'])

#Note that new 'Bill' appeared in the beginning not in the end as you might expected.
#The thing is that dictionary basically does not have any ordering. New value appear in random place.
#Remember that the dictionary is case-sensitive if you are using strings as keys. Keep in mind that 'key' and 'Key' are different keys:
phones['Zoe'] = '658-99-55'
phones['Bill'] = '342-18-25'
print (phones)


#case sensitive
d = {}
d['key'] = 1
d['Key'] = 2
d['KEY'] = 3
print (d)

#Procura uma entrada em phones
if 'Peter' in phones:
    print("We know Peter's phone")
else:
    print("We don't know Peter's phone")


#In case you need to delete a value from a dictionary please use del:
#phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
del phones['Zoe']
print(phones)

string = 'We tried list and we tried dicts also we tried Zen'


#To iterate over words in string you can split it by space:
for word in string.split(' '):
    print(word)

#To have nice output of dictionary you can use .items() method:
for key, value in phones.items():
    print(key + ' = ' + value)



string = 'We tried list and we tried dicts also we tried Zen'
contadorPalavras = {}
for palavra in string.split(' '):
    if palavra not in contadorPalavras:
        contadorPalavras[palavra] = 1

    else:contadorPalavras[palavra] += 1

print(contadorPalavras)

for palavra_temp, valor in contadorPalavras.items():
    print(palavra_temp + ' ' + str(valor))



"""

#Problema Proposto
string = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
contadorPalavras = {}
for palavra in string.split(' '):
    if palavra not in contadorPalavras:
        contadorPalavras[palavra] = 1

    else:contadorPalavras[palavra] += 1


for palavra_temp, valor in contadorPalavras.items():
    print(palavra_temp + ' ' + str(valor))

"""