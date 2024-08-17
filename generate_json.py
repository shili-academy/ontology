import json
import random

# Danh sách mở rộng các role (khoảng 20 role)
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
    {
        "role_name": "DevOps Engineer",
        "skills": ["CI/CD", "Automation", "Cloud Computing", "Server Management", "Security"],
        "current_position": "System Administrator",
        "target_position": "DevOps Engineer"
    },
    {
        "role_name": "Mobile App Developer",
        "skills": ["Java", "Kotlin", "Swift", "Android Development", "iOS Development"],
        "current_position": "Junior Mobile Developer",
        "target_position": "Mobile App Developer"
    },
    {
        "role_name": "AI Engineer",
        "skills": ["Machine Learning", "Deep Learning", "Python Programming", "TensorFlow", "Natural Language Processing"],
        "current_position": "AI Researcher",
        "target_position": "AI Engineer"
    },
    {
        "role_name": "Cybersecurity Specialist",
        "skills": ["Network Security", "Cryptography", "Ethical Hacking", "Risk Management", "Incident Response"],
        "current_position": "Security Analyst",
        "target_position": "Cybersecurity Specialist"
    },
    {
        "role_name": "Database Administrator",
        "skills": ["SQL", "Database Design", "Performance Tuning", "Backup and Recovery", "Security"],
        "current_position": "Database Assistant",
        "target_position": "Database Administrator"
    },
    {
        "role_name": "Project Manager",
        "skills": ["Agile Methodologies", "Scrum", "Team Management", "Risk Management", "Project Planning"],
        "current_position": "Assistant Project Manager",
        "target_position": "Project Manager"
    },
    {
        "role_name": "Data Engineer",
        "skills": ["Big Data", "ETL", "Data Warehousing", "Python Programming", "SQL"],
        "current_position": "Junior Data Engineer",
        "target_position": "Data Engineer"
    },
    {
        "role_name": "Cloud Architect",
        "skills": ["Cloud Computing", "AWS", "Azure", "Google Cloud", "DevOps"],
        "current_position": "Cloud Engineer",
        "target_position": "Cloud Architect"
    },
    {
        "role_name": "Blockchain Developer",
        "skills": ["Blockchain", "Smart Contracts", "Solidity", "Cryptography", "Decentralized Applications"],
        "current_position": "Junior Blockchain Developer",
        "target_position": "Blockchain Developer"
    },
    {
        "role_name": "Network Engineer",
        "skills": ["Networking", "Network Security", "Cisco", "Routing", "Switching"],
        "current_position": "Junior Network Engineer",
        "target_position": "Network Engineer"
    },
    {
        "role_name": "IT Support Specialist",
        "skills": ["Technical Support", "Troubleshooting", "Customer Service", "Windows Administration", "Help Desk"],
        "current_position": "IT Assistant",
        "target_position": "IT Support Specialist"
    },
    {
        "role_name": "Business Analyst",
        "skills": ["Data Analysis", "Business Intelligence", "Requirements Gathering", "Process Improvement", "Project Management"],
        "current_position": "Junior Business Analyst",
        "target_position": "Business Analyst"
    },
    {
        "role_name": "Software Architect",
        "skills": ["System Design", "Software Architecture", "Microservices", "API Development", "Security"],
        "current_position": "Senior Developer",
        "target_position": "Software Architect"
    },
    {
        "role_name": "UI/UX Designer",
        "skills": ["User Interface Design", "User Experience Design", "Wireframing", "Prototyping", "Adobe XD"],
        "current_position": "Junior Designer",
        "target_position": "UI/UX Designer"
    },
    {
        "role_name": "Full Stack Developer",
        "skills": ["Frontend Development", "Backend Development", "JavaScript", "Python Programming", "Database Management"],
        "current_position": "Junior Developer",
        "target_position": "Full Stack Developer"
    },
    {
        "role_name": "Quality Assurance Engineer",
        "skills": ["Software Testing", "Automation Testing", "Test Planning", "Bug Tracking", "Performance Testing"],
        "current_position": "QA Assistant",
        "target_position": "Quality Assurance Engineer"
    }
]

# Mở rộng danh sách skill (khoảng 100 skill)
skills = [
    "Python Programming", "Software Design", "Data Science", "Machine Learning", "Artificial Intelligence",
    "Web Development", "JavaScript", "CSS", "React", "HTML", "Server Management", "Database Design",
    "API Development", "Security", "Big Data", "Java", "Kotlin", "Swift", "Android Development", "iOS Development",
    "CI/CD", "Automation", "Cloud Computing", "TensorFlow", "Natural Language Processing", "Network Security",
    "Cryptography", "Ethical Hacking", "Risk Management", "Incident Response", "SQL", "Performance Tuning",
    "Backup and Recovery", "Agile Methodologies", "Scrum", "Team Management", "Project Planning", "Blockchain",
    "DevOps", "Docker", "Kubernetes", "Software Testing", "Continuous Integration", "Continuous Deployment",
    "System Architecture", "Microservices", "RESTful APIs", "GraphQL", "User Interface Design", "User Experience Design",
    "Cross-Platform Development", "Mobile UX/UI", "Responsive Web Design", "Progressive Web Apps", "Serverless Computing",
    "Edge Computing", "Data Visualization", "Business Intelligence", "Predictive Analytics", "Data Mining",
    "Digital Marketing", "SEO", "Content Management Systems", "Social Media Management", "E-Commerce Platforms",
    "IT Support", "Help Desk", "Network Administration", "System Monitoring", "Cloud Security", "Penetration Testing",
    "Mobile Security", "Web Security", "Threat Detection", "Vulnerability Assessment", "Patch Management",
    "IT Governance", "Compliance Management", "IT Auditing", "Data Governance", "Data Privacy", "Disaster Recovery",
    "Incident Management", "Change Management", "Service Management", "Process Automation", "Workflow Automation",
    "Robotic Process Automation (RPA)", "AI Ethics", "Explainable AI", "Data Ethics", "Software Licensing",
    "Software Compliance", "Intellectual Property", "Open Source Software", "Software Development Lifecycle (SDLC)",
    "Customer Relationship Management (CRM)", "Enterprise Resource Planning (ERP)", "Business Process Modeling", 
    "Lean Six Sigma", "Supply Chain Management", "Vendor Management", "Contract Management", "Operations Management"
]

# Mở rộng danh sách hình ảnh và liên kết khóa học (khoảng 100 mỗi loại)
course_images = [
    "https://pluralsight.imgix.net/course-images/django-fundamentals-v1.jpg",
    "https://pluralsight.imgix.net/course-images/introduction-to-kubernetes-v1.jpg",
    "https://pluralsight.imgix.net/course-images/angular-fundamentals-v1.jpg",
    "https://pluralsight.imgix.net/course-images/aws-certified-solutions-architect-v1.jpg",
    "https://pluralsight.imgix.net/course-images/cyber-security-certification-v1.jpg",
    "https://pluralsight.imgix.net/course-images/machine-learning-ai-v1.jpg",
    "https://pluralsight.imgix.net/course-images/python-for-data-science-v1.jpg",
    "https://pluralsight.imgix.net/course-images/devops-fundamentals-v1.jpg",
    "https://pluralsight.imgix.net/course-images/sql-for-beginners-v1.jpg",
    "https://pluralsight.imgix.net/course-images/full-stack-development-v1.jpg",
    "https://pluralsight.imgix.net/course-images/ruby-on-rails-v1.jpg",
    "https://pluralsight.imgix.net/course-images/javascript-advanced-v1.jpg",
    "https://pluralsight.imgix.net/course-images/linux-fundamentals-v1.jpg",
    "https://pluralsight.imgix.net/course-images/blockchain-for-developers-v1.jpg",
    "https://pluralsight.imgix.net/course-images/golang-for-beginners-v1.jpg",
    "https://pluralsight.imgix.net/course-images/cloud-computing-essentials-v1.jpg",
    "https://pluralsight.imgix.net/course-images/networking-fundamentals-v1.jpg",
    "https://pluralsight.imgix.net/course-images/docker-deep-dive-v1.jpg",
    "https://pluralsight.imgix.net/course-images/mobile-app-development-v1.jpg",
    "https://pluralsight.imgix.net/course-images/ethical-hacking-v1.jpg"
]

course_links = [
    "https://www.udemy.com/course/pythonforbeginners/",
    "https://www.udemy.com/course/machinelearning/",
    "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
    "https://www.udemy.com/course/software-architecture-and-design/",
    "https://www.udemy.com/course/deeplearning/",
    "https://www.udemy.com/course/java-programming/",
    "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/",
    "https://www.udemy.com/course/ethical-hacking/",
    "https://www.udemy.com/course/cyber-security-certification/",
    "https://www.udemy.com/course/web-development-bootcamp/",
    "https://www.udemy.com/course/full-stack-web-development-with-react/",
    "https://www.udemy.com/course/introduction-to-devops/",
    "https://www.udemy.com/course/android-app-development/",
    "https://www.udemy.com/course/ios-development-bootcamp/",
    "https://www.udemy.com/course/data-science-and-machine-learning/",
    "https://www.udemy.com/course/cloud-computing-with-aws/",
    "https://www.udemy.com/course/network-security-essentials/",
    "https://www.udemy.com/course/advanced-python-programming/",
    "https://www.udemy.com/course/blockchain-and-cryptocurrency-explained/",
    "https://www.udemy.com/course/artificial-intelligence-az/"
]

courses_example = [
    {"course_name": "Introduction to Python Programming", "course_description": "Learn the basics of Python programming, including variables, data types, and functions."},
    {"course_name": "Advanced Machine Learning Techniques", "course_description": "Master advanced machine learning algorithms and techniques with hands-on projects."},
    {"course_name": "Web Development with JavaScript", "course_description": "Build dynamic and interactive websites using JavaScript, HTML, and CSS."},
    {"course_name": "Data Science Essentials", "course_description": "An introduction to data science concepts including data manipulation, visualization, and basic statistics."},
    {"course_name": "Deep Learning with TensorFlow", "course_description": "Explore deep learning concepts and build neural networks using TensorFlow."},
    {"course_name": "Cybersecurity Fundamentals", "course_description": "Understand the basics of cybersecurity, including threat analysis and risk management."},
    {"course_name": "Full Stack Web Development", "course_description": "Learn both frontend and backend web development with modern technologies like React and Node.js."},
    {"course_name": "Blockchain and Cryptocurrency", "course_description": "Dive into the world of blockchain technology and understand how cryptocurrencies work."},
    {"course_name": "Mobile App Development with React Native", "course_description": "Create cross-platform mobile apps using React Native and JavaScript."},
    {"course_name": "Introduction to Cloud Computing", "course_description": "Gain an understanding of cloud computing fundamentals and major cloud service providers."},
    {"course_name": "DevOps Essentials", "course_description": "Learn the key practices and tools involved in DevOps, including CI/CD pipelines."},
    {"course_name": "Artificial Intelligence for Beginners", "course_description": "A beginner's guide to AI, covering fundamental concepts and applications."},
    {"course_name": "Agile Project Management", "course_description": "Master Agile methodologies and learn how to manage projects effectively."},
    {"course_name": "SQL for Data Analysis", "course_description": "Learn SQL to manage and analyze data in relational databases."},
    {"course_name": "Kubernetes in Practice", "course_description": "Implement container orchestration with Kubernetes and Docker."},
    {"course_name": "Network Security Essentials", "course_description": "Learn about securing network infrastructures and implementing security protocols."},
    {"course_name": "Introduction to Ethical Hacking", "course_description": "Learn the basics of ethical hacking and penetration testing techniques."},
    {"course_name": "Java Programming for Beginners", "course_description": "An introductory course to Java programming, covering core concepts and syntax."},
    {"course_name": "Big Data Analytics with Hadoop", "course_description": "Learn how to process and analyze big data using the Hadoop ecosystem."},
    {"course_name": "Software Design Patterns", "course_description": "Explore common software design patterns and how to implement them."},
    {"course_name": "Introduction to Data Visualization", "course_description": "Learn how to create informative and visually appealing data visualizations."},
    {"course_name": "Cyber Threat Intelligence", "course_description": "Understand cyber threats and how to gather intelligence to prevent attacks."},
    {"course_name": "AWS Certified Solutions Architect", "course_description": "Prepare for the AWS Solutions Architect certification with hands-on labs."},
    {"course_name": "iOS Development with Swift", "course_description": "Learn to develop iOS apps using Swift and Xcode."},
    {"course_name": "Introduction to Artificial Neural Networks", "course_description": "Explore the basics of artificial neural networks and how they are used in AI."},
    {"course_name": "Responsive Web Design", "course_description": "Create responsive and mobile-friendly web designs using modern CSS techniques."},
    {"course_name": "CI/CD with Jenkins", "course_description": "Implement continuous integration and deployment pipelines using Jenkins."},
    {"course_name": "Fundamentals of Data Governance", "course_description": "Learn the principles of data governance and how to manage data assets effectively."},
    {"course_name": "Introduction to Game Development with Unity", "course_description": "Create your first 2D and 3D games using Unity and C#."},
    {"course_name": "Advanced Cybersecurity Practices", "course_description": "Implement advanced cybersecurity measures and incident response strategies."},
    {"course_name": "Introduction to Quantum Computing", "course_description": "Get started with quantum computing and understand its basic principles and applications."}
]


courses = []

for i in range(1000):
    course_example = random.choice(courses_example)
    course = {
        "course_name": course_example.get('course_name'), 
        "skill_taught": random.choice(skills),
        "course_image": random.choice(course_images),
        "course_link": random.choice(course_links),
        "course_description": course_example.get('course_description')
    }
    courses.append(course)

# Tạo tệp JSON
data = {
    "roles": roles,
    "courses": courses
}

# Lưu vào tệp JSON
with open('courses.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Tệp JSON đã được tạo và lưu thành công với khoảng 20 role, 100 skill, và 100 khóa học!")
