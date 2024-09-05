from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/' , methods = ['POST', 'GET'])

def calculator():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        bmi = weight/((height/100) **2)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.debug = True
    app.run()