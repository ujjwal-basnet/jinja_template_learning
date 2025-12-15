from flask import Flask , render_template 

app = Flask(__name__)
max_score= 100 
test_name= "english"
students = [
    {"name": "ram",  "score": 100},
    {"name": "hari", "score": 87},
    {"name": "gita", "score": 92},
    {"name": "sita", "score": 40},
    {"name": "rakesh", "score": 75},
]




@app.route("/")
def home():
    return render_template("base.html", title='jinja and flask')


@app.route("/results")
def results():
    context= {
        "title": "Results",
        "students" : students,
        "test_name": test_name,
        "max_score":max_score
    }
    return render_template('results.html', **context)


if __name__ == "__main__":
    app.run(debug= True)