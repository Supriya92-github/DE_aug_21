from flask import Flask

#wsgi server
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Praxis "



@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to praxis {your_name}"

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=3400)