from flask import Flask, render_template
from fluent import sender


app = Flask(__name__)


def send(level):
	logger = sender.FluentSender('app', host='fluentd', port=24224)
	result = logger.emit('flask.' + level, {'level': level, 'from': 'heart', 'to': 'sun'})
	if not result:
		error = logger.last_error
		logger.clear_last_error()
	else:
		error = 'OK'
	logger.close()
	return error

@app.route("/info")
def info():
	return "Info: " + send('info')

@app.route("/debug")
def debug():
	return "Debug: " + send('debug')

@app.route("/warning")
def warning():
	return "Warning: " + send('warn')

@app.route("/error")
def error():
	return "Error: " + send('error')

@app.route("/")
def home():
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
