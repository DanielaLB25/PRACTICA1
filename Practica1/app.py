from flask import Flask, render_template, request, redirect, url_for

app = Flask(name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/servicios/maquillaje-personalizado')
def maquillaje_personalizado():
    return render_template('maquillaje_personalizado.html')

@app.route('/servicios/clases-de-maquillaje')
def clases_maquillaje():
    return render_template('clases_maquillaje.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Guardar el mensaje en un archivo de texto
        with open('contactos.txt', 'a') as f:
            f.write(f'Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}\n')

        return redirect(url_for('index'))  # Redirige a la página de inicio después de enviar el formulario
    
    return render_template('contacto.html')

if name == 'main':
    app.run(debug=True)
