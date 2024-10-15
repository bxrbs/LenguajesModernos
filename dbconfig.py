import pymysql

def getDBConnection():
    connection = pymysql.connect(
        host='localhost',         
        user='root',    
        password='password777', 
        database='musica'  
    )
    return connection