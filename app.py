from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can add code to handle the form data, such as saving it to a database or sending an email
        return f'Thank you for your message, {name}!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
