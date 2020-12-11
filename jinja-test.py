from json import load
from jinja2 import Environment, FileSystemLoader, select_autoescape

file = open("RxGovResponse.json", "r")
output = open("output.json", "w")
d = load(file)

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('Bundle')
output.write(template.render(rxGovResponse=d))