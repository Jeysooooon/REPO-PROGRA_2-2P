from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

bpProductos = Blueprint('Clientes', __name__, url_prefix='/Clientes')

@bpProductos.route("/")
def productos_index():
    conn = get_connection
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos")
    datos = cur.fetchall()
    cur.close()
    return render_template('productos/index.html', lista_productos=datos)



@app.route("/agregar", methods=["GET", "POST"])
def productos_agregar_datos():
    if request.method == 'POST':
        conn = get_connection
        cursor = conn.cursor()
        nombre= request.form['ProNombre']
        descripcion = request.form['ProDescripcion']
        precio = request.form['ProPrecio']
        costo = request.form['ProCosto']
        stock=request.form['ProStock']
        cursor.execute("insert into productos(ProNombre, ProDescripcion, ProPrecio, ProCosto, ProStock) values(%s, %s, %s, %s, %s)", (nombre, descripcion, precio, costo, stock))
        conn.commit()
        return redirect(url_for('productos_index'))
    elif request.method=='GET':
         return render_template('/productos/agregar.html')


@app.route("/editar/<string:codigo>", methods=["GET", "POST"])
def productos_editar_datos(codigo):
    if request.method == 'GET':
        conn = get_connection
        cur = conn.cursor()
        cur.execute("SELECT * FROM productos where ProCodigo=%s", (codigo,))
        producto = cur.fetchone()
        return render_template('/productos/editar.html', producto=producto)
    elif request.method=='POST':
        cursor = conn.cursor()
        nombre= request.form['ProNombre']
        descripcion = request.form['ProDescripcion']
        precio = request.form['ProPrecio']
        costo = request.form['ProCosto']
        stock=request.form['ProStock']
        cursor.execute("update productos set ProNombre=%s, ProDescripcion=%s, ProPrecio=%s, ProCosto=%s, ProStock=%s where ProCodigo=%s", (nombre, descripcion, precio, costo, stock, codigo))
        conn.commit()
        return redirect(url_for('productos_index'))

    
@app.route("/eliminar/<string:codigo>", methods=["GET", "POST"])
def productos_eliminar_datos(codigo):
    if request.method == 'GET':
        conn = get_connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE ProCodigo = %s", (codigo,))
        producto = cursor.fetchone()
        return render_template('/productos/eliminar.html', producto=producto)
        
    elif request.method == 'POST':
        conn = get_connection
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE ProCodigo = %s", (codigo,))
        conn.commit()
        return redirect(url_for('productos_index'))
