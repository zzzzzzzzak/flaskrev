from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the flask"

@app.route('/calculator',methods = ["GET"])
def math_operation():
    opeartion=request.json["opeartion"]
    numbers1= request.json["number1"]
    numbers2=request.json["number2"]
    
    if opeartion=='add':
        result = numbers1 + numbers2
        
    elif opeartion=='multiply':
        result= numbers1*numbers2
    elif opeartion=='division':
        result=numbers1/numbers2
    else:
        result=numbers1-numbers2
    return result 


if __name__== '__main__':
    app.run()

