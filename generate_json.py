import json
import random

# Danh sách các role và skill mẫu
roles = [
    {
        "role_name": "Senior Developer",
        "skills": ["Python Programming", "Software Design", "Data Science", "Artificial Intelligence", "Web Development"],
        "current_position": "Junior Developer",
        "target_position": "Senior Developer"
    },
    {
        "role_name": "Data Scientist",
        "skills": ["Data Science", "Machine Learning", "Statistics", "Python Programming", "Big Data"],
        "current_position": "Data Analyst",
        "target_position": "Data Scientist"
    },
    {
        "role_name": "Frontend Developer",
        "skills": ["Web Development", "JavaScript", "CSS", "React", "HTML"],
        "current_position": "Junior Developer",
        "target_position": "Frontend Developer"
    },
    {
        "role_name": "Backend Developer",
        "skills": ["Server Management", "Python Programming", "Database Design", "API Development", "Security"],
        "current_position": "Junior Developer",
        "target_position": "Backend Developer"
    },
    # Thêm nhiều role hơn, ít nhất 20 role
]

# Danh sách các skill mẫu
skills = [
    "Python Programming",
    "Software Design",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence",
    "Web Development",
    "JavaScript",
    "CSS",
    "React",
    "HTML",
    "Server Management",
    "Database Design",
    "API Development",
    "Security",
    "Big Data"
]

# Danh sách các hình ảnh và liên kết mẫu (lấy từ Udemy)
course_images = [
    "https://img-c.udemycdn.com/course/480x270/1542112_1b60_4.jpg",
    "https://img-c.udemycdn.com/course/480x270/950390_270f_3.jpg",
    "https://img-c.udemycdn.com/course/480x270/1362070_b9a1_2.jpg",
    "https://img-c.udemycdn.com/course/480x270/903744_8eb2.jpg",
    "https://img-c.udemycdn.com/course/480x270/2196488_8fc7.jpg"
]

course_links = [
    "https://www.udemy.com/course/pythonforbeginners/",
    "https://www.udemy.com/course/machinelearning/",
    "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
    "https://www.udemy.com/course/software-architecture-and-design/",
    "https://www.udemy.com/course/deeplearning/"
]

# Tạo danh sách khóa học
courses = []

for i in range(1000):
    course = {
        "course_name": f"Course {i+1}",
        "skill_taught": random.choice(skills),
        "course_image": random.choice(course_images),
        "course_link": random.choice(course_links),
        "course_description": f"This is a description for Course {i+1}."
    }
    courses.append(course)

# Tạo danh sách các role (ít nhất 20 role)
role_list = roles * (20 // len(roles))  # Nhân bản danh sách role để đạt ít nhất 20 role

# Tạo tệp JSON
data = {
    "roles": role_list,
    "courses": courses
}

# Lưu vào tệp JSON
with open('courses_and_roles.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Tệp JSON đã được tạo và lưu thành công!")

