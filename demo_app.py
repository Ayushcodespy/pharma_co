from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # getting input with name = fname in HTML form
        first_name = request.form['name']
        # getting input with name = lname in HTML form
        last_name = request.form['password']

        if first_name == 'admin' and last_name =='admin123':

            return render_template('index.html', first_name=first_name, last_name=last_name)
        else:
            return 'welcome'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)