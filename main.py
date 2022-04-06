from kivy.storage.jsonstore import JsonStore

store = JsonStore('hello.json')

# put alguns valores
#store.put('tito', name='Mathieu', age=30)
#store.put('tshirtman', name='Gabriel', age=27)
#store.put('Ziel', name='Jesiel', age=21)

# pegando por uma key
print('tito is', store.get('tito'))

# or guess the key/entry for a part of the key
#key, tshirtman = store.find(name='Gabriel')
#print('tshirtman is', tshirtman)

# Filtrando items
res = store.find()
for item in res:
    #print("Nome=", str(item))
    print('Nome: ', str(item[1]['name']))
    print("Idade: ", str(item[1]['age']))