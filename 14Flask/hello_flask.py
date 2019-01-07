import flask


# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def helloWorld():
    return "Hello World From Flask Web Framework"


if __name__ == '__main__':
    APP.debug=True
    APP.run()
