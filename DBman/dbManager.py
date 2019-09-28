import sqlite3
from sqlite3 import Error


def insert_assg(squad,rank,userID,name):
    conn=sqlite3.connect("data.db")
    l = []
    l.append(squad)
    l.append(rank)
    l.append(userID)
    l.append(name)
    query = tuple(l)
    c = conn.cursor()
    try:
        statement = ("""
        Insert into 
        assignmentData
        values(
        ?,
        ?,
        ?,
        ?
        )
        """)
        print(query)
        print(statement)
        c.execute(statement,query)
        conn.commit()
        print("Success!")
        conn.close()

    except Error as e:
        print(e)
        conn.close()

def retrieve_assg(userID):
    conn = sqlite3.connect("data.db")
    l = []
    i = []
    i.append(userID)
    query = tuple(i)
    try:
        statement = (
            """
            select * 
            from 
            assignmentData
            where userID=?
            """
        )
        c.execute(statement,query)
        output=" "
        for i in c:
            output+=str(i)
        conn.commit()
        print(output)
        print("Success!")
        conn.close()
        return output
    except Error as e:
        print(e)
        conn.close()
        return e




def remove_assg(userID):
    conn = sqlite3.connect("data.db")
    l=[]
    l.append(userID)
    query = tuple(l)
    try:
        statement = (
            """
            delete from assignmentData where
            userID=?
            """
        )
        c.execute(statement,query)
        conn.commit()
        output = " "
        for i in c:
            output+=str(i)
        conn.close()
        return output
    except Error as e:
        print(e)
        conn.close()
        return str(e)


conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute('''
CREATE TABLE 
IF NOT EXISTS 
assignmentData (squad text,
                rank text,
                userID text primary key,
                name text
                )
            ''')

#-----------------------------------------------------------

"""
This is default state data, in case something bad happens.

insert_assg("Chosen Undead","Demon Lord","814418325","KuroAkuma")
insert_assg("Senpai's Squad","Taichou","140860604","Mika Senpai")
insert_assg("Prime Eractus","Captain","932138471","Lucifer")
insert_assg("soaperS","Captain","609134614","Uzumaki Konzoku")
insert_assg("BlackSquad","Captain","945257374","Asuna")
insert_assg("Elemental","High King","691607802","Escanor")
insert_assg("Maou","Maō","740866586","Prinz")
insert_assg("Punishers","Captain","316541168","Rick Sanchez")
insert_assg("Yorozuya","SakataGintoki","791289016","Sakata Gintoki")

c.execute("Select * from assignmentData")

for i in c:
    print(i)
"""
