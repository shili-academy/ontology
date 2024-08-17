from rdflib import RDF, URIRef

def backward_chaining(graph, target_role, EX):
    if (target_role, RDF.type, EX.Role) not in graph:
        return None

    learning_path = []
    for skill in graph.objects(target_role, EX.requiresSkill):
        for course in graph.subjects(EX.teachesSkill, skill):
            if course not in learning_path:
                learning_path.append(course)
    
    if not learning_path: 
        return None

    return learning_path
