from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def form_page():

	return render_template('application-form.html')


@app.route('/application', methods=["POST"])
def index_page():
	# Return this as a strange
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salary = request.form.get("salary")
	job_title = request.form.getlist("jobselection")


	return """
      <!DOCTYPE html>
      <html>
        <head>
          <title>Thank you for your application!</title>
        </head>
        <body>
          Thank you, %s %s, for applying to be a %s. Your minimum salary requirement is %s dollars.
        </body>
      </html>
      """ % (firstname, lastname, job_title[0], salary)

	# return render_template("application_submit.html",
	# 						firstname=firstname,
	# 						lastname=lastname,
	# 						salary=salary,
	# 						job_title=job_title)

	# Alternately, we could make this a Jinja template in `templates/`
	# and return that result of rendering this, like:
	#
	# return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)