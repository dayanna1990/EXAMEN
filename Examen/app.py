from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro
        descuento = 0

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25

        total_con_descuento = total_sin_descuento - descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento,
            'total_con_descuento': total_con_descuento
        }
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "juan" and password == "admin":
            mensaje = "Bienvenido administrador juan"
        elif username == "pepe" and password == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
