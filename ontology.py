import json
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
courseDescription = URIRef(EX.courseDescription)
courseName = URIRef(EX.courseName)
currentPosition = URIRef(EX.currentPosition)
targetPosition = URIRef(EX.targetPosition)

g.add((requiresSkill, RDF.type, RDF.Property))
g.add((hasCourse, RDF.type, RDF.Property))
g.add((teachesSkill, RDF.type, RDF.Property))
g.add((courseImage, RDF.type, RDF.Property))
g.add((courseLink, RDF.type, RDF.Property))
g.add((courseDescription, RDF.type, RDF.Property))
g.add((courseName, RDF.type, RDF.Property))
g.add((currentPosition, RDF.type, RDF.Property))
g.add((targetPosition, RDF.type, RDF.Property))

# Đọc dữ liệu từ tệp JSON
with open('courses.json', 'r') as f:
    data = json.load(f)

# Thêm vai trò và kỹ năng
for role in data['roles']:
    role_uri = URIRef(EX[role['role_name'].replace(" ", "_")])
    g.add((role_uri, RDF.type, Role))
    
    # Thêm thông tin về vị trí hiện tại và mục tiêu
    current_position_uri = URIRef(EX[role['current_position'].replace(" ", "_")])
    target_position_uri = URIRef(EX[role['target_position'].replace(" ", "_")])
    
    g.add((role_uri, currentPosition, current_position_uri))
    g.add((role_uri, targetPosition, target_position_uri))
    
    for skill in role['skills']:
        skill_uri = URIRef(EX[skill.replace(" ", "_")])
        g.add((skill_uri, RDF.type, Skill))
        g.add((role_uri, requiresSkill, skill_uri))

# Thêm các khóa học
for course in data['courses']:
    course_uri = URIRef(EX[course['course_name'].replace(" ", "_")])
    skill_uri = URIRef(EX[course['skill_taught'].replace(" ", "_")])
    
    # Thêm khóa học và kỹ năng liên quan
    g.add((course_uri, RDF.type, Course))
    g.add((skill_uri, RDF.type, Skill))
    g.add((course_uri, teachesSkill, skill_uri))
    
    # Thêm thông tin khóa học
    g.add((course_uri, courseImage, Literal(course['course_image'])))
    g.add((course_uri, courseLink, Literal(course['course_link'])))
    g.add((course_uri, courseDescription, Literal(course['course_description'])))
    g.add((course_uri, courseName, Literal(course['course_name'])))

# Lưu ontology vào file
g.serialize("ontology.owl", format="xml")

print("Ontology saved to ontology.owl")

