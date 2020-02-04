from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import createtimetable 

app = Flask(__name__,template_folder='')
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'timetableschedular'

mysql = MySQL(app)

@app.route('/hod')
def hod():
    return render_template('hod.html')

@app.route('/')
def logout():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/hodlogin', methods = ['POST'])
def hodlogin():
    
    if request.method == "POST":
        email = request.form['email']
        passwd = request.form['password']
        
        print("Content-type: text/html \r\n\r\n")
        mydb = mysql.connection.cursor()
        loadname= "select email from users where email=%s and passwd = %s"
        mydb.execute(loadname,(email,passwd,))
        c=mydb.fetchall()
        #print(len(c))
        #print(c[0]);

        if len(c)==1:
            return render_template('hod.html')
        
        else:
            return render_template('index.html')
        
def faclogin():
    
    if request.method == "POST":
        email = request.form['email']
        passwd = request.form['password']
        
        print("Content-type: text/html \r\n\r\n")
        mydb = mysql.connection.cursor()
        loadname= "select email from users where email=%s and passwd = %s"
        mydb.execute(loadname,(email,passwd,))
        c=mydb.fetchall()
        #print(len(c))
        #print(c[0]);

        if len(c)==1:
            return render_template('faculty.html')
        
        else:
            return render_template('index.html')
            

@app.route('/hodsignup', methods = ['POST'])
def hodsignup():
    
    if request.method == "POST":
        fname = request.form['fullname']
        email  = request.form['email']
        mobno = request.form['mobile']
        deptt = request.form['dropdown']
        passwd = request.form['password']
        mydb = mysql.connection.cursor()
        mydb.execute("INSERT INTO users(fname,email,mobno,deptt,passwd,ishod) VALUES (%s, %s, %s, %s, %s, %s)",(fname,email,mobno,deptt,passwd,'1'))
        mysql.connection.commit()
        mydb.close()
        
    return render_template('index.html')
        

@app.route('/facsignup', methods = ['POST'])
def facsignup():
    
    if request.method == "POST":
        fname = request.form['fullname']
        email  = request.form['email']
        mobno = request.form['mobile']
        deptt = request.form['dropdown']
        passwd = request.form['password']
        mydb = mysql.connection.cursor()
        mydb.execute("INSERT INTO users(fname,email,mobno,deptt,passwd,ishod) VALUES (%s, %s, %s, %s, %s, %s)",(fname,email,mobno,deptt,passwd,'0'))
        mysql.connection.commit()
        mydb.close()
        
    return render_template('index.html')
    
@app.route('/sub')
def Index():
    mydb = mysql.connection.cursor()
    mydb.execute("SELECT  * FROM subinfo")
    data = mydb.fetchall()
    mydb.close()

    return render_template('sub.html', subjects=data)


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    mydb = mysql.connection.cursor()
    mydb.execute("DELETE FROM subinfo WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        subtype = request.form['subtdropdown']
        subCode = request.form['subjectcode']
        subName = request.form['subjectname']
        sem = request.form['semdropdown']
        dept = request.form['deptdropdown']
        mydb = mysql.connection.cursor()
        mydb.execute("INSERT INTO subinfo (subtype, subCode, subName, sem, dept) VALUES (%s, %s, %s, %s, %s)", (subtype, subCode, subName, sem, dept))
        mysql.connection.commit()
        mydb.close()
    return redirect(url_for('Index'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        subtype = request.form['subtdropdown']
        subCode = request.form['subjectcode']
        subName = request.form['subjectname']
        sem = request.form['semdropdown']
        dept = request.form['deptdropdown']
        mydb = mysql.connection.cursor()
        mydb.execute("""
               UPDATE subinfo
               SET subtype=%s, subCode=%s, subName=%s, sem=%s, dept=%s 
               WHERE id=%s
            """, (subtype, subCode, subName, sem, dept, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/createtimetab')
def subjectinfo():
    mydb = mysql.connection.cursor()
    print("Content-type: text/html \r\n\r\n")
    mydb.execute("SELECT subCode, subName FROM subinfo")
    subdata = mydb.fetchall()

    mydb.execute("SELECT id,fname FROM users")
    facdata = mydb.fetchall()
    mydb.close()
    
    return render_template('createtimetab.html', sub0=subdata ,lensub=len(subdata), fac0=facdata,lenfac=len(facdata))

@app.route('/generatetime',methods=['POST','GET'])
def generator():
    print("Content-type: text/html \r\n\r\n")
    subject=[]
    num_sub = len(request.form)//3
    for i in range(0,num_sub):
        subcode = request.form['sub'+str(i)]
        faccode = request.form['fac'+str(i)]
        subcount = request.form['subcount'+str(i)]
        subject.append(createtimetable.sub(subcode,faccode,subcount))
    subject = createtimetable.sortsub(subject)
    timetable = generateTimeTable(subject)
    printtimetable(timetable)
    return subjectinfo()

def generateTimeTable(subject):
    timet = {}
    timet[6] = [[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0]]
    timet[8] = [[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0]]
    
    
    for subsem in subject:
        
        subsem = subject[subsem]
        filledsem = []
        for sub in subsem:
            i=0
            j=0
            sem = timet[sub.sem]
            while sub.issubcount():
                if(sem[i][j]==0):
                    if(len(filledsem)>0):
                        ansem = timet[filledsem[0]]
                        if(ansem[i][j]!=0):
                            if(ansem[i][j].faccode==sub.faccode):
                                j+=1
                                if j>7:
                                    i+=1
                                    j=0
                                    if(i>4):
                                        i=0
                                continue
                    sem[i][j]=sub
                    sub.subcount-=1
                    i+=1
                    j+=1
                    if j>7:
                        j=0
                    if(i>4):
                        i=0
                else:
                    j+=1
                    if j>7:
                        i+=1
                        j=0
                        if(i>4):
                            i=0
        filledsem.append(subsem[0].sem)
    return timet
def printtimetable(timetable):
    print()
    print()
    tt = [timetable[6],timetable[8]]
    #print(tt[1])
    for t in tt:
        for i in range(0,5):
            for j in range(0,8):
                if(t[i][j]!=1 and t[i][j]!=0):
                   print(t[i][j].subcode,end="\t\t")
                else:
                    print(t[i][j],end="\t\t")
            print()
        print()
        print()
        print()
                    
                    
                    
            
    


if __name__ == "__main__":
    app.run(port=5000,debug=True)
