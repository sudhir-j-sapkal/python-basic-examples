from flask import Flask, jsonify


# Create the application.
APP = Flask(__name__)

@APP.route('/')
def myHome():
	return "My Home";

@APP.route('/api/employees', methods=['GET'])
def getEmployees():
    employees = [{"emp_id":"1","name":"Sudhir"},{"emp_id":"11","name":"Sudhir1"},{"emp_id":"133","name":"Sudhir23"}]
    return jsonify({"message":"success", "data":employees})

@APP.route('/api/employee/<emp_id>', methods=['GET'])
def getEmployee(emp_id):
    emps = [{"emp_id":"1","name":"Sudhir"},{"emp_id":"11","name":"Sudhir1"},{"emp_id":"133","name":"Sudhir23"}]
    for employee in emps:
        return employee.name
        return jsonify({"message":"success","data":employee}) 

if __name__ == '__main__':
    APP.debug=True
    APP.run()

