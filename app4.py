from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
	return jsonify(
{"about": "Hello there! it's a Calculator.py that use flask framework and REST API with Json"},
{"functions": "there is 4 functionswhich you can use: Addition (add), Subtraction (sub), Multiplication (Mul), Division (div)"},

{"Addiiton": "If you want use this function you should add in the link /add/{num1}/{num2}, where is {num1} - first aurgument, {num2} - second aurgument"},

{"Subtraction": "If you want use this function you should add in the link /sub/{num1}/{num2}, where is {num1} - first aurgument, {num2} - second aurgument"},

{"Multiplication": "If you want use this function you should add in the link /mul/{num1}/{num2}, where is {num1} - first aurgument, {num2} - second aurgument"},

{"Division": "If you want use this function you should add in the link /div/{num1}/{num2}, where is {num1} - first aurgument, {num2} - second aurgument"}
)

@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def get_add(num1, num2):
	return jsonify({'result': num1+num2})

@app.route('/sub/<int:num1>/<int:num2>', methods=['GET'])
def get_sub(num1, num2):
        return jsonify({'result': num1-num2})

@app.route('/mul/<int:num1>/<int:num2>', methods=['GET'])
def get_mul(num1, num2):
        return jsonify({'result': num1*num2})

@app.route('/div/<int:num1>/<int:num2>', methods=['GET'])
def get_div(num1, num2):
        return jsonify({'result': num1/num2})


if __name__ == '__main__':
	app.run(debug=True)
