import mysql.connector
import mysql.connector.connection

def getData():

    try:
        connection = mysql.connector.connect(
            user='sql10336547', password='PrElzjSLVT',
            host='sql10.freemysqlhosting.net', port=3306,
            database='sql10336547'
        )
        c = connection.cursor()

        c.execute("SELECT * FROM blackbelts")
        rows = c.fetchall()
        # listaresultado = []
        # for e in rows:
        #     nome = e[0]
        #     faixa = e[1]
        #     equipe = e[2]
        #     academia = e[3]
        #     datagraduacao = e[4]
        #     apelido = e[5]
        #     listaresultado.append(nome)
        #     listaresultado.append(faixa)
        #     listaresultado.append(equipe)
        #     listaresultado.append(academia)
        #     listaresultado.append(datagraduacao)
        #     listaresultado.append(apelido)

        return rows

    except Exception as err:
        print(err)
    finally:
        connection.close()


def insertData(nome, faixa, time, academia, datagraduacao, apelido):

    try:
        connection = mysql.connector.connect(
            user='sql10336547', password='PrElzjSLVT',
            host='sql10.freemysqlhosting.net', port=3306,
            database='sql10336547'
        )
        c = connection.cursor()

        params = nome, faixa, time, academia, datagraduacao, apelido

        c.execute(f'''INSERT INTO blackbelts (nome, faixa, time, academia, datagraduacao, apelido) VALUES('{nome}',
                  '{faixa}', '{time}', '{academia}', '{datagraduacao}', '{apelido}')''')
        connection.commit()
        return True
    except Exception as err:
        print(err)
        return False
    finally:
        connection.close()

def removeData(nome):
    try:
        conn = mysql.connector.connect(user='sql10336547', password='PrElzjSLVT',
            host='sql10.freemysqlhosting.net', port=3306,
            database='sql10336547')
        c = conn.cursor()
        c.execute(f"DELETE FROM blackbelts WHERE nome like '{nome}' ")
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

def updateData(nome, faixa, time, academia, datagraduacao, apelido):

    try:
        conn = mysql.connector.connect(user='sql10336547', password='PrElzjSLVT',
            host='sql10.freemysqlhosting.net', port=3306,
            database='sql10336547')
        c = conn.cursor()
        c.execute(f'''UPDATE blackbelts SET faixa = '{faixa}', time = '{time}', academia = '{academia}', 
datagraduacao = '{datagraduacao}', apelido = '{apelido}' WHERE nome like '{nome}' ''')
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return False
    finally:
        conn.close()