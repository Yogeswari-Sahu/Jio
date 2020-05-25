from flask import Flask,render_template, url_for, request, redirect


app= Flask(__name__)
app.config['SECRET_KEY']='91c0e2fcb2a2008481fa07d4e4beb3fa'


@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html', title='Login')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)