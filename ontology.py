from rdflib import Graph, RDF, URIRef, Namespace, OWL, Literal

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
courseImage = URIRef(EX.courseImage)
courseLink = URIRef(EX.courseLink)
courseDescription = URIRef(EX.courseDescription)  # Thêm thuộc tính mô tả

g.add((requiresSkill, RDF.type, RDF.Property))
g.add((hasCourse, RDF.type, RDF.Property))
g.add((teachesSkill, RDF.type, RDF.Property))
g.add((courseImage, RDF.type, RDF.Property))
g.add((courseLink, RDF.type, RDF.Property))
g.add((courseDescription, RDF.type, RDF.Property))

# Thêm các cá thể (individuals)
senior_developer = URIRef(EX.SeniorDeveloper)
junior_developer = URIRef(EX.JuniorDeveloper)
data_scientist = URIRef(EX.DataScientist)
frontend_developer = URIRef(EX.FrontendDeveloper)

python_programming = URIRef(EX.PythonProgramming)
advanced_python = URIRef(EX.AdvancedPython)
software_architecture = URIRef(EX.SoftwareArchitecture)
machine_learning = URIRef(EX.MachineLearning)
deep_learning = URIRef(EX.DeepLearning)
react_development = URIRef(EX.ReactDevelopment)
html_css_js = URIRef(EX.HtmlCssJs)

g.add((senior_developer, RDF.type, Role))
g.add((junior_developer, RDF.type, Role))
g.add((data_scientist, RDF.type, Role))
g.add((frontend_developer, RDF.type, Role))

g.add((python_programming, RDF.type, Skill))
g.add((advanced_python, RDF.type, Course))
g.add((software_architecture, RDF.type, Course))
g.add((machine_learning, RDF.type, Course))
g.add((deep_learning, RDF.type, Course))
g.add((react_development, RDF.type, Course))
g.add((html_css_js, RDF.type, Course))

# Liên kết các cá thể (associations between individuals)
g.add((senior_developer, requiresSkill, python_programming))
g.add((junior_developer, requiresSkill, python_programming))
g.add((data_scientist, requiresSkill, machine_learning))
g.add((frontend_developer, requiresSkill, html_css_js))

g.add((advanced_python, teachesSkill, python_programming))
g.add((machine_learning, teachesSkill, python_programming))
g.add((deep_learning, teachesSkill, python_programming))
g.add((react_development, teachesSkill, html_css_js))

g.add((senior_developer, hasCourse, advanced_python))
g.add((senior_developer, hasCourse, software_architecture))
g.add((data_scientist, hasCourse, machine_learning))
g.add((data_scientist, hasCourse, deep_learning))
g.add((frontend_developer, hasCourse, react_development))
g.add((frontend_developer, hasCourse, html_css_js))

# Thêm thông tin hình ảnh, liên kết và mô tả cho các khóa học
g.add((advanced_python, courseImage, Literal("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS68XRM9pZTYOrjS9WvI4Kusz38p7qYu4EHMg&s")))
g.add((advanced_python, courseLink, Literal("https://www.udemy.com/course/advanced-python-programming")))
g.add((advanced_python, courseDescription, Literal("This course covers advanced topics in Python programming.")))

g.add((software_architecture, courseImage, Literal("https://www.questpond.com/qp-img/76/pic_76.jpg")))
g.add((software_architecture, courseLink, Literal("https://www.udemy.com/courses/search/?src=ukw&q=software-architecture")))
g.add((software_architecture, courseDescription, Literal("Learn the principles of software architecture and design patterns.")))

g.add((machine_learning, courseImage, Literal("https://example.com/images/machine_learning.jpg")))
g.add((machine_learning, courseLink, Literal("https://example.com/courses/machine-learning")))
g.add((machine_learning, courseDescription, Literal("An introduction to machine learning concepts and techniques.")))

g.add((deep_learning, courseImage, Literal("https://example.com/images/deep_learning.jpg")))
g.add((deep_learning, courseLink, Literal("https://example.com/courses/deep-learning")))
g.add((deep_learning, courseDescription, Literal("Explore deep learning techniques and neural networks.")))

g.add((react_development, courseImage, Literal("https://example.com/images/react_development.jpg")))
g.add((react_development, courseLink, Literal("https://example.com/courses/react-development")))
g.add((react_development, courseDescription, Literal("Learn how to build dynamic web applications with React.")))

g.add((html_css_js, courseImage, Literal("https://example.com/images/html_css_js.jpg")))
g.add((html_css_js, courseLink, Literal("https://example.com/courses/html-css-js")))
g.add((html_css_js, courseDescription, Literal("Master the basics of web development with HTML, CSS, and JavaScript.")))

# Lưu ontology vào file
g.serialize("ontology.owl", format="xml")

print("Ontology saved to ontology.owl")
