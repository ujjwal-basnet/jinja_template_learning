from jinja2 import Environment , FileSystemLoader 
from pathlib import Path


environment= Environment(loader= FileSystemLoader("templates/"))
template= environment.get_template("message_with_cond.txt")

students = [
       {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

for student in students:
    filename = Path(f"output/with_if_else/message_{student['name'].lower()}.txt")
    filename.parent.mkdir(parents=True, exist_ok=True)

    content= template.render(**student)

    with open(filename , mode='w', encoding='utf-8')as message:
        message.write(content)
        print(f"wrote {filename}")
