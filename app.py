from flask import Flask, request, render_template
from rdflib import URIRef

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_role = request.form['role']
        target_role_uri = URIRef(EX[target_role])
        learning_path = backward_chaining(g, target_role_uri)
        return render_template('result.html', role=target_role, learning_path=learning_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
