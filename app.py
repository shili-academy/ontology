from flask import Flask, request, render_template
from rdflib import Graph, URIRef, Namespace
from utils import backward_chaining 

# Tạo Namespace và tải Ontology
EX = Namespace("http://localhost/ontologies/")
g = Graph()
g.parse("ontology.owl", format="xml")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_role = request.form['role']
        target_role_uri = URIRef(EX[target_role])
        learning_path = backward_chaining(g, target_role_uri, EX)
        
        if learning_path is None:
            error_message = "Không tìm thấy kết quả phù hợp cho vai trò này."
            return render_template('index.html', error=error_message)
        
        return render_template('result.html', role=target_role, learning_path=learning_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
