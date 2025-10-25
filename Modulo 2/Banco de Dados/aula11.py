'''Passo 1

- importar sqlite3

-não precisa instalar nada

Passo 2 

- criar conexão com o banco de dados

-Na primeira execução sera criado o arquivo

passo 3 
- criar um cursor

- serve para executar scripts SQL dentro do banco'''


import sqlite3


conexao = sqlite3.connect('sega.db')


cursor = conexao.cursor()


print(' conexão bem-sucedida ')

cursor.execute('''


    CREATE TABLE IF NOT EXISTS sega (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT NOT NULL,

        espécie TEXT NOT NULL,

        idade INTEGER NOT NULL

    );

''')

'''cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Sonic','ourico',15))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Tails','raposa',8))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Amy','ourico',13))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Knuckles','echidna',16))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Rouge','morcego',18))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Blaze','gato',14))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Shadow','ourico',50))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Silver','ourico',15))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Cream','coelho',6))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('robotnik','humano',50))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Vector','crocodilo',30))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Espio','camaleao',15))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Charmy','abelha',4))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Big','gato',29))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Maria','humano',13))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Cubot','robo',2))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Orbot','robo',2))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Metal Sonic','robo',5))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Sege','I.A',7))

cursor.execute("INSERT INTO sega ('nome','espécie','idade')VALUES (?,?,?)",('Vanila','coelho',29))
'''
conexao.commit()

conexao.close()


conexao = sqlite3.connect('sega.db')


cursor = conexao.cursor()


consulta = cursor.execute("SELECT nome, espécie, idade FROM sega")
print()

print("------------★★★-------------SONIC CARACTERS--★--")

for lista in consulta.fetchall():

    print(f'''

     PERSONAGEM: {lista[0]} 

     ESPÉCIE: {lista[1]} 

     IDADE: {lista[2]}
     -----------------------''') 


'''jls_extract_var = "UPDATE sega SET idade = ? WHERE id = ?"
cursor.execute(jls_extract_var, (30,20))

conexao.commit()
conexao.close()

conexao = sqlite3.connect('sega.db')


cursor = conexao.cursor()

cursor.execute("DELETE FROM sega WHERE id = ?", ('19',))

conexao.commit()
conexao.close()