from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")
@app.route('/menu')
def menu():
   return render_template('menu.html')
@app.route('/about')
def about():
   return render_template('about.html')
@app.route('/booking')
def booking():
   return render_template('booking.html')


if __name__ == '__main__':
    app.run(port=3000,debug=True)