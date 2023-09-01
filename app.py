from flask import Flask, render_template, request

app = Flask(__name__)

data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        fruit = request.form.get('fruit')
        data.append({'name': name, 'age': age, 'gender': gender, 'fruit': fruit})

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
