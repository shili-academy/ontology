def backward_chaining(graph, target_role):
    if (target_role, RDF.type, EX.Role) not in graph:
        return f"No information found for {target_role}"

    learning_path = []
    for skill in graph.objects(target_role, requiresSkill):
        for course in graph.subjects(teachesSkill, skill):
            if course not in learning_path:
                learning_path.append(course)
    
    return learning_path

# Sử dụng bộ suy diễn lùi để tìm khóa học cho Senior Developer
target_role = senior_developer
learning_path = backward_chaining(g, target_role)
print(f"To become a Senior Developer, you need to complete the following courses: {[str(c) for c in learning_path]}")
