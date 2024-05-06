import sqlite3

#impotar banco de dados


sexo=input("DIgite seu sexo (M/F): ")
idade=int(input("Digite sua idade: "))
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
TMB=0

if sexo=="M":
  TMB=88.362 + (13.397*peso)+ (4.799* altura) - (5.677*idade)
  print("seu TMB é: ",TMB)

elif sexo=="F":
  TMB=447.593 + (9.247*peso) + (3.098*altura) - (4.330*idade)
  print("seu TMB é: ",TMB)

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_usuarios.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, sexo TEXT, idade INTEGER, peso REAL, altura REAL, TMB REAL)''')



# Inserir os dados do usuário no banco de dados
cursor.execute("INSERT INTO usuarios (sexo, idade, peso, altura, TMB) VALUES (?, ?, ?, ?,?)", (sexo, idade, peso, altura, TMB))
conn.commit()
# Fechar a conexão com o banco de dados
conn.close()


  
