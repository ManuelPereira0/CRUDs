# criar uma conexão
import pymysql.cursors

conexao = pymysql.connect(
    host='ip',
    user='root',
    database='database',
    password='passwd',
    cursorclass=pymysql.cursors.DictCursor
    )
cursor = conexao.cursor()

# CRUD
#comando = ''
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados
#resultado = cursor.fetchall() # ler o banco de dados -> somente read

#cursor.close()
#conexao.close()

# creat
# comando = 'insert into cadastro values (1,"Livro",50)'
# cursor.execute(comando)
# conexao.commit() 

# cursor.close()
# conexao.close()

# read
#comando = f'select * from cadastro'
#cursor.execute(comando)
#resultado = cursor.fetchall() 
#print(resultado)
#cursor.close()
#conexao.close()

# update
# comando = f'update  set preco = 200 where id = 1'
# cursor.execute(comando)
# conexao.commit() 

# cursor.close()
# conexao.close()

# delete
# comando = 'delete from cadastro where id = 1'
# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()
