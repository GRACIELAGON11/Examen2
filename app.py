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

if __name__ == '__main__':
    app.run(port=5000 ,debug= True)