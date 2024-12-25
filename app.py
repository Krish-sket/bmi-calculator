from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def calculate():
    bmi=''
    if request.method == 'POST' and 'mass' in request.form and 'height' in request.form:
        mass=float(request.form.get('mass'))
        height=float(request.form.get('height'))
        bmi=round(mass/((height/100)**2),2)
    return render_template("index.html",bmi=bmi)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)