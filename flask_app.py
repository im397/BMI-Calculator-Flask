
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from processing import do_calculation
from calculator import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def bmi_page():
    errors = ""
    if request.method == "POST":
        feet = None
        inches = None
        pounds = None
        try:
            feet = float(request.form["feet"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["feet"])
        try:
            inches = float(request.form["inches"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["inches"])
        try:
            pounds = float(request.form["pounds"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["pounds"])

        if feet is not None and inches is not None and pounds is not None:

            inches = (feet * 12) + inches
            meters = in2m(inches)
            kilos = lb2kg(pounds)

            bmi = calcBMI(meters, kilos)
            category = bmiCategory(bmi)

            return '''
                <html>
                    <body>
                        <p>Your BMI is: {bmi}</p>
                        <p>You are {category}</p>
                        <p><a href="/">Click here to calculate again</a>.
                    </body>
                </html>
            '''.format(bmi=bmi,category=category)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your height and weight:</p>
                <form method="post" action=".">
                    <p>
                        <label for="feet">Feet:</label>
                        <input name="feet" />
                    </p>
                    <p>
                        <label for="inches">Inches:</label>
                        <input name="inches" />
                    </p>
                    <p>
                        <label for="pounds">Pounds:</label>
                        <input name="pounds" />
                    </p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

#def hello_world():
#    return 'Hello from Martini!'

