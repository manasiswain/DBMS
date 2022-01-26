from flask import Flask, redirect, url_for, request,render_template
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
con = psycopg2.connect(
            host = "127.0.0.1",
            database="blood_bank_dbms",
            user = "postgres",
            password = "postgres")
app = Flask(__name__)
class DataStore():
    user=''

data = DataStore()

@app.route("/back/", methods=['POST'])
def back():
    return render_template('index.html')
@app.route("/backprev/", methods=['POST'])
def backprev():
    if(data.user=='admin'):
        return render_template('dbpage.html')
    else:
        return render_template('x.html')
@app.route("/create1/", methods=['POST'])
def create1():
    try:
        na=request.form['af']
        no=request.form['ac']
        name=[]
        cur = con.cursor()
    
        for i in range(0,int(no)):
            name.append(request.form[str(i)])
        s='CREATE TABLE '+na+' ('
        ct=0
        for i in name:
            i=i.replace(',',' ')
            s+=i
            if(ct!=int(no)-1):
                s+=','
            ct+=1
        s+=');'
        cur.execute(s)
        con.commit()
        cur.close()
        x='''<form action="/disp/" method="post"><p><input type = "text" name = "nm" readonly="readonly" value='''
        x+=na
        x+='''></p>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Display Table</button>
            </form>
            <form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>'''
        return(x)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/create/", methods=['POST'])
def create():
    try:
        name1=request.form['nm']
        no=request.form['ab']
        l=['''<form action="/create1/" method="post">''']
        s='''<p>Table Name:</p>
                <p><input type = "text" readonly="readonly" name = "af" style="background-color:#CBC3E3;" value='''
        s+=name1
        s+='''></p>'''
        s+='''<p>No of attributes:</p>
            <p><input type = "text" readonly="readonly" name = "ac" style="background-color:#CBC3E3;" value='''
        s+=no
        s+='''></p>'''
        l.append(s)
        for i in range(0,int(no)):
            s='''<p>Enter Attribute Name,type,condition</br>Enter condition if you want otherwise leave empty:</p>
                <p><input type = "text" style="background-color:#CBC3E3;" name ='''
            s+=str(i)
            s+='''></p>'''
            l.append(s)
        l.append('''<button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Create</button></form>''')
        l.append('''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
        st=' '.join(l)
        return(st)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
    
@app.route("/digi/", methods=['POST'])
def digi():
    try:
        cur = con.cursor()
        cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        l=['''<html>
    <style>
    table, th, td {
    border:1px solid black;
    border-collapse: collapse;
    }
    td {
    background-color:#CBC3E3;
  
    }
    </style>
    <body>

    <h2>TABLE NAME</h2>
    <table style="width:10%">
    <tr>''']
        l.append('</tr>')
        for table in cur.fetchall():
            l.append('<tr>')
            for i in table:
                l.append('<td>'+str(i)+'</td>')
            l.append('</tr>')
        l.append('''</table>''')
        l.append('''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
        st=' '.join(l)
        con.commit()
        cur.close()
        return(st)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/disp/", methods=['POST'])
def display():
    try:
        #Moving forward code
        name1=request.form['nm']
        cur = con.cursor()
        cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(name1)))
        rows = cur.fetchall()
        st=''
        l=['''<html>
    <style>
    table, th, td {
    border:1px solid black;
    border-collapse: collapse;
    }
    th {
    background-color:SlateBlue;
        color:White;
    }
    td {
    background-color:#CBC3E3;
  
    }
    </style>
    <body>

    <h2>''']
        l.append(name1.upper())
        l.append('''</h2>
    <table style="width:60%">
    <tr>''')
        colname=[j[0] for j in cur.description]
        for i in colname:
            l.append('<th>'+i.upper()+'</th>')
        for i in rows:
            l.append('<tr>')
            for j in i:
                l.append('<td>'+str(j)+'</td>')
            l.append('</tr>')
        l.append('''</table>''')
        l.append('''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
        st=' '.join(l)
        con.commit()
        cur.close()
        return(st)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/delete/", methods=['POST'])
def delete():
    try:
        cur = con.cursor()
        cur.execute('''SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name''')
        rows = cur.fetchall()
        name=request.form['nm']
        cur.execute(sql.SQL('DELETE FROM {}').format(sql.Identifier(name)))
        con.commit()
        cur.close()
        cur.close()
        s='''<p>Table name:</p><form action="/disp/" method="post"><p><input type = "text" name = "nm" value='''
        s+=name
        s+='''></p>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Display Table</button>
            </form>
            <form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>'''
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/drop/", methods=['POST'])
def drop():
    try:
        cur = con.cursor()
        cur.execute('''SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name''')
        rows = cur.fetchall()
        name=request.form['nm']
        cur.execute(sql.SQL('DROP TABLE {};').format(sql.Identifier(name)))
        con.commit()
        cur.close()
        s='''<p>Table name:</p><form action="/disp/" method="post"><p><input type = "text" name = "nm" value='''
        s+=name
        s+='''></p>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Display Table</button>
            </form>
            <form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>'''
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/insert1/", methods=['POST'])
def insert1():
    try:
        name=request.form['nm']
        cur = con.cursor()
        cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(name)))
        colname=[j[0] for j in cur.description]
        s1='</br>'.join(colname)
        s='FOR THESE COLUMNS</br></br>'+s1.upper()
        s+='''<p>Table name:</p><form action="/insert/" method="post"><p><input type = "text" readonly="readonly" name = "nm"   style="background-color:#CBC3E3;" value='''
        s+=name
        s+='''></p><p>Enter values comma separated:</p>
                <p><input type = "text" name = "ab" style="background-color:#CBC3E3;"/></p>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Insert into Table</button></form><form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>'''
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/Uquerry/", methods=['POST'])
def Uquerry():
    try:
        s='''<form action="/query3/" method="post"><p>Write Update based query you want to perform</p><p><input type = "text" name = "a" style="background-color:#CBC3E3;"/></p>
            <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Querry it</button></form>'''
        s+='''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button></form>'''
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
        </form>''')
@app.route("/Squerry/", methods=['POST'])
def Squerry():
    try:
        s='''<form action="/query2/" method="post"><p>Write select based query you want to perform</p><p><input type = "text" name = "a" style="background-color:#CBC3E3;"/></p>
            <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Querry it</button></form>'''
        s+='''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button></form>'''
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
        </form>''')
@app.route("/query2/", methods=['POST'])
def querry2():
   try:
        name=request.form['a']
        cur = con.cursor()
        cur.execute(name)
        x=cur.fetchall()
        l=['''<html>
        <style>
        table, th, td {
        border:1px solid black;
        border-collapse: collapse;
        }
        th {
        background-color:SlateBlue;
        color:White;
        }
        td {
        background-color:#CBC3E3;
  
        }
        </style>
        <body>

        <h2>''']
        l.append('''</h2>
        <table style="width:60%">
        <tr>''')
        colname=[j[0] for j in cur.description]
        for i in colname:
            l.append('<th>'+i.upper()+'</th>')
        m=[]
        for i in x:
            l.append('<tr>')
            for j in i:
                l.append('<td>'+str(j)+'</td>')
            l.append('</tr>')
        l.append("</table>")
        l.append('''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
        st=' '.join(l)
        con.commit()
        cur.close()
        return(st)
   except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
@app.route("/query3/", methods=['POST'])
def querry3():
    try:
        name=request.form['a']
        cur = con.cursor()
        cur.execute(name)
        s="UPDATED</br>"+"No of rows updated:"+str(cur.rowcount)
        s+='''<form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
                </form>'''
        con.commit()
        cur.close()
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
    
@app.route("/insert/", methods=['POST'])
def insert():
    try:
        name=request.form['nm']
        y=request.form['ab']
        res=y.split(',')
        if(res==[]):
            res.append(name)
        cur = con.cursor()
        cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(name)))
        colname=[j[0] for j in cur.description]
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
        s='''<form action="/disp/" method="post"><p><input type = "text" name = "nm" value='''
        s+=name
        s+='''></p>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Display Table</button>
            </form>
            <form action="/backprev/" method="post">
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>'''
        return(s)
    except:
        con.rollback()
        return('''<form action="/backprev/" method="post">
                <h1>Invalid Request</h1>
                <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
            </form>''')
    
@app.route('/failure/<name>')
def fail(name):
   return '''<h1>Invalid Entry</h1></br><form action="/back/" method="post">
            <button name="forwardBtn" type="submit" style="background-color:SlateBlue;color:white">Back</button>
        </form>'''

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      data.user = request.form['nm']
      password=request.form['ab']
      if(data.user=='admin'):
        if(password=='rootme'):
            return render_template('dbpage.html',name=data.user)
        elif(password!='rootme'):
            return redirect(url_for('fail',name =data.user))
      else:
        if(password==data.user):
            return render_template('x.html',name=data.user)
        elif(password!='rootme'):
            return redirect(url_for('fail',name =data.user))
   else:
      data.user = request.args.get('nm')
      password=request.form['ab']
      if(password=='rootme'):
        return render_template('dbpage.html')
      else:
        return redirect(url_for('fail',name =data.user))

if __name__ == '__main__':
   app.run(debug = True)
