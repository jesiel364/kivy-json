## Declarando arquivo json

` store = JsonStore('hello.json') `

## PUT, GET, POST E DELETE

### PUT

` store.put('Ziel', name='Jesiel', age=21) `

### GET

` print('tito tem ', store.get('tito')['age']) `

### READ

``` 
res = store.find()
for item in res:
    print('Nome: ', str(item[1]['name']))
    print("Idade: ", str(item[1]['age']))
```

### DELETE

` store.delete('tito') `
