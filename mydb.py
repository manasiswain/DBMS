import psycopg2
import getpass
from tabulate import tabulate
from psycopg2 import sql
from psycopg2.extensions import AsIs
con = psycopg2.connect(
            host = "127.0.0.1",
            database="blood_bank_dbms",
            user = "postgres",
            password = "postgres")
y='yes'
isp=2
f='yes'
while(isp==2 and f=='yes'):
    print("USER:")
    u=input()
    p=getpass.getpass()
    if(u=='admin'):
        if(p=='rootme'):
            isp=1
        else:
            isp=2
            print("INVALID\nDo you want to login again(yes,no)")
            f=input()
    else:
        if(p==u):
            isp=0
        else:
            isp=2
            print("INVALID\nDo you want to login again(yes,no)")
            f=input()
while(y=='yes' and f=='yes'):
    if(isp==1):
        print('''Which operation would you like to perform:
1.INSERT
2.DISPLAY
3.DELETE TABLE
4.DROP TABLE
5.CREATE TABLE
6.SELECT QUERY
7.UPDATE QUERY
8.TABLES PRESENT
9.EXIT''')
    else:
        print('''Which operation would you like to perform:
1.DISPLAY
2.SELECT QUERY
3.TABLES PRESENT
4.EXIT''')
    x=int(input())
    if(x==1 and isp==1):
        try:
            cur = con.cursor()
            cur.execute('''SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name''')
            rows = cur.fetchall()
            b=[]
            for i in rows:
                b.append(i)
            print(tabulate(b, headers=['TABLE']))
            print("\nWhich table:")
            name=input()
            cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(name)))
            colname=[j[0] for j in cur.description]
            print("for these",colname,"\n ENTER VALUES SEPRATED BY SPACE")
            res=list(map(str,input().split(' ')))
            p='('
            for i in range(0,len(colname)):
                if(i==len(colname)-1):
                    p+='%s'
                else:
                    p+='%s,'
            p+=')'
            cur.execute(sql.SQL('INSERT INTO {} VALUES'+p).format(sql.Identifier(name)),tuple(res))
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif((x==2 and isp==1) or (x==1 and isp==0)):
        try:
            cur = con.cursor()
            cur.execute('''SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name''')
            rows = cur.fetchall()
            b=[]
            for i in rows:
                b.append(i)
            print(tabulate(b, headers=['TABLE']))
            print("\nWhich table:")
            name=input()
            cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(name)))
            colname=[j[0] for j in cur.description]
            rows = cur.fetchall()
            b=[]
            for i in rows:
                b.append(list(i))
            print(tabulate(b, headers=colname))
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif(x==3 and isp==1):
        try:
            cur = con.cursor()
            cur.execute('''SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name''')
            rows = cur.fetchall()
            b=[]
            for i in rows:
                b.append(i)
            print(tabulate(b, headers=['TABLE']))
            print("\nWhich table:")
            name=input()
            cur.execute(sql.SQL('DELETE FROM {}').format(sql.Identifier(name)))
            con.commit()
            cur.close()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif(x==4 and isp==1):
        try:
            cur = con.cursor()
            cur.execute('''SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name''')
            rows = cur.fetchall()
            b=[]
            for i in rows:
                b.append(i)
            print(tabulate(b, headers=['TABLE']))
            print("\nWhich table:")
            name=input()
            cur.execute(sql.SQL('DROP TABLE {}').format(sql.Identifier(name)))
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif(x==5 and isp==1):
        try:
            name=input("Enter Table name:")
            n=int(input("Enter no of attributes:"))
            l=[]
            cur = con.cursor()
            for i in range(0,n):
                print("Enter Attribute Name,type,condition\nEnter condition if you want otherwise leave empty")
                s=input()
                l.append(s)
            s='CREATE TABLE '+name+' ('
            ct=0
            for i in l:
                i=i.replace(',',' ')
                s+=i
                if(ct!=n-1):
                    s+=','
                ct+=1
            s+=');'
            cur.execute(s)
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif((x==6 and isp==1) or (x==2 and isp==0)):
        try:
            s=input("Enter Select Query:")
            cur = con.cursor()
            cur.execute(s)
            colname=[j[0] for j in cur.description]
            rows = cur.fetchall()
            b=[]
            for i in rows:
                b.append(list(i))
            print(tabulate(b, headers=colname))
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif(x==7 and isp==1):
        try:
            s=input("Enter Update Query:")
            cur = con.cursor()
            cur.execute(s)
            print("UPDATED \nNo of rows updated:"+str(cur.rowcount))
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif((x==8 and isp==1)or(x==3 and isp==0)):
        try:
            cur = con.cursor()
            cur.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
            b=[]
            for i in cur.fetchall():
                b.append(i)
            print(tabulate(b, headers=['TABLE']))
            con.commit()
            cur.close()
        except:
            con.rollback()
            print("Invalid Request")
    elif((x==9 and isp==1)or(x==4 and isp==0)):
        break
    print('Do you want to continue(yes,no)')
    y=input()

con.close()
