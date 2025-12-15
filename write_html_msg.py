from condition_message import student
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

results_filename = Path("outputs/html/students_results.html")
results_filename.parent.mkdir(parents=True, exist_ok=True)

environment= Environment(loader= FileSystemLoader("templates/"))
results_template= environment.get_template("results.html")

students = [
    {"name": "ram",  "score": 100},
    {"name": "hari", "score": 87},
    {"name": "gita", "score": 92},
    {"name": "sita", "score": 40},
    {"name": "rakesh", "score": 75},
]

test_name= "english"
max_score= 100

context= { ####### this is the actual msgg that will be send
    'students': students,
    'test_name': test_name,
    'max_score': max_score
} 

with open(results_filename, mode="w", encoding= 'utf-8') as results:
    results.write(results_template.render(**context))
    print(f" wrote {results_filename}")