from rdflib import RDF

def backward_chaining(graph, target_role, EX):
    if (target_role, RDF.type, EX.Role) not in graph:
        return None

    learning_path = []
    for skill in graph.objects(target_role, EX.requiresSkill):
        for course in graph.subjects(EX.teachesSkill, skill):
            if course not in learning_path:
                image = graph.value(course, EX.courseImage)
                link = graph.value(course, EX.courseLink)
                description = graph.value(course, EX.courseDescription)
                learning_path.append({
                    "course": course,
                    "image": image,
                    "link": link,
                    "description": description
                })
    
    if not learning_path:
        return None

    return learning_path
