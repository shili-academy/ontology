from rdflib import RDF

def get_roles(graph, EX):
    roles = []
    for role in graph.subjects(RDF.type, EX.Role):
        role_name = role.split('/')[-1].replace("_", " ")
        roles.append(role_name)
    return roles

def backward_chaining(graph, current_role, target_role, EX):
    # Lấy các kỹ năng cần thiết từ vị trí mục tiêu
    target_skills = list(graph.objects(target_role, EX.requiresSkill))
    
    # Lấy các kỹ năng đã có từ vị trí hiện tại
    current_skills = set(graph.objects(current_role, EX.requiresSkill))
    
    # Lộ trình học tập cho các kỹ năng chưa có
    learning_path = []
    
    for skill in target_skills:
        if skill not in current_skills:
            for course in graph.subjects(EX.teachesSkill, skill):
                course_name = graph.value(course, EX.courseName)
                image = graph.value(course, EX.courseImage)
                link = graph.value(course, EX.courseLink)
                description = graph.value(course, EX.courseDescription)
                learning_path.append({
                    "course_name": course_name,
                    "course": course,
                    "image": image,
                    "link": link,
                    "description": description
                })
    
    if not learning_path:
        return None

    return learning_path
