from flask import Flask, request, render_template
from rdflib import Graph, URIRef, Namespace
from utils import backward_chaining, get_roles

# Tạo Namespace và tải Ontology
EX = Namespace("http://localhost/ontologies/")
g = Graph()
g.parse("ontology.owl", format="xml")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    roles = get_roles(g, EX)
    courses = None
    error = None
    
    if request.method == 'POST':
        current_position = URIRef(EX[request.form['current_position'].strip().replace(" ", "_")])
        target_position = URIRef(EX[request.form['target_position'].strip().replace(" ", "_")])
        
        courses = backward_chaining(g, current_position, target_position, EX)
        
        if not courses:
            error = "Không tìm thấy lộ trình học tập phù hợp."
    
    return render_template('index.html', roles=roles, courses=courses, error=error)

if __name__ == '__main__':
    app.run(debug=True)
