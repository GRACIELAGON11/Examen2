#paquteria de flas
from flask import Flask,render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#la inicializacion del app 
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key='mysecretkey'
MySQL=MySQL(app)
#INSERTAR DATOS 
@app.route('/')
def index():
        cc=MySQL.connection.cursor();
        cc.execute('select * from tbflores')
        #guardar consulta
        conFlores=cc.fetchall();
        print(conFlores)
        return render_template('index.html',listaFlores=conFlores)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        #pasamos a variables el contenido de los input
        Vnombre=request.form['txtNombre']
        Vcantidad=request.form['txtCantidad']
        Vprecio=request.form['txtPrecio']
    
        #conectar y ejecutar el insert
        CS= MySQL.connection.cursor()
        CS. execute('insert into tbflores(nombre,cantidad,precio) values(%s,%s,%s)',(Vnombre,Vcantidad,Vprecio))
        MySQL.connection.commit()
    flash('EL DATO FUE AGREGADO CORRECTAMENTE')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    CursorId= MySQL.connection.cursor()
    CursorId.execute('select * from tbflores where id= %s',(id,))
    consulId= CursorId.fetchone()  
    return render_template('Editar.html', Flores=consulId)

@app.route('/update/<id>', methods=['POST'])
def update(id):
   if request.method == 'POST':
    Vnombre=request.form['txtNombre']
    Vcantidad=request.form['txtCantidad']
    Vprecio=request.form['txtPrecio']
    curAct= MySQL.connection.cursor()
    curAct.execute('update tbflores set nombre= %s, cantidad= %s, precio= %s  where id= %s',(Vnombre,Vcantidad,Vprecio,id))
    MySQL.connection.commit()
    
    
    flash('Se actualizo el nombre de la flor'+Vnombre)    
    return redirect(url_for('index'))
   
   #consultar
@app.route("/Consultar.html")
def consultasFrutas():
    return render_template('Consultar.html')



@app.route("/consultar")
def consulta():
    vnombre = request.form.get('nombre', False)
    cs = MySQL.connection.cursor()
    cs.execute('select * from tbflores where nombre = %s order by nombre', [vnombre])
    data = cs.fetchone()
    print(data)
    return render_template('Consultar.html', Flor = data)




if __name__ == '__main__':
    app.run(port=5000 ,debug= True)