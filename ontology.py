from rdflib import Graph, RDF, URIRef, Namespace, OWL

# Tạo Namespace
EX = Namespace("http://localhost/ontologies/")

# Tạo đồ thị RDF
g = Graph()

# Định nghĩa các lớp (classes)
Role = URIRef(EX.Role)
Skill = URIRef(EX.Skill)
Course = URIRef(EX.Course)

g.add((Role, RDF.type, OWL.Class))
g.add((Skill, RDF.type, OWL.Class))
g.add((Course, RDF.type, OWL.Class))

# Định nghĩa các thuộc tính và mối quan hệ (properties and relationships)
requiresSkill = URIRef(EX.requiresSkill)
hasCourse = URIRef(EX.hasCourse)
teachesSkill = URIRef(EX.teachesSkill)

g.add((requiresSkill, RDF.type, RDF.Property))
g.add((hasCourse, RDF.type, RDF.Property))
g.add((teachesSkill, RDF.type, RDF.Property))

# Thêm các cá thể (individuals)
senior_developer = URIRef(EX.SeniorDeveloper)
junior_developer = URIRef(EX.JuniorDeveloper)
python_programming = URIRef(EX.PythonProgramming)
advanced_python = URIRef(EX.AdvancedPython)
software_architecture = URIRef(EX.SoftwareArchitecture)

g.add((senior_developer, RDF.type, Role))
g.add((junior_developer, RDF.type, Role))
g.add((python_programming, RDF.type, Skill))
g.add((advanced_python, RDF.type, Course))
g.add((software_architecture, RDF.type, Course))

# Liên kết các cá thể (associations between individuals)
g.add((senior_developer, requiresSkill, python_programming))
g.add((advanced_python, teachesSkill, python_programming))
g.add((senior_developer, hasCourse, advanced_python))
g.add((senior_developer, hasCourse, software_architecture))

# Lưu ontology vào file
g.serialize("ontology.owl", format="xml")
