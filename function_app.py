import azure.functions as func

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>DevSecOps & DevOps Courses</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f9f9f9; }
        h1 { color: #0078d7; }
        .course { margin-bottom: 15px; }
        a { color: #2b5797; text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>🚀 DevOps & DevSecOps Learning Resources</h1>

    <div class="course">🚀 <a href="https://www.tutorialspoint.com/course/fundamentals-of-devsecops-handson-included/index.asp" target="_blank">DevSecOps Fundamentals</a> – A beginner's guide to DevSecOps.</div>
    <div class="course">🚀 <a href="https://www.udemy.com/course/sonarqube-master-sonarqube-within-a-few-hours-2020/?referralCode=992044CBD2B0CAA48856" target="_blank">SonarQube Mastery</a> – Improve code quality and security.</div>
    <div class="course">🚀 <a href="https://www.udemy.com/course/google-cloud-serverless/?referralCode=9C79C2F2F87F1045C902" target="_blank">Serverless Architecture</a> – Build scalable apps with ease.</div>
    <div class="course">🚀 <a href="https://www.udemy.com/course/docker-devops/?referralCode=ECEDBD3CEC6B99717566" target="_blank">Docker Essentials</a> – Learn containers and Kubernetes.</div>
    <div class="course">🚀 <a href="https://www.udemy.com/course/jenkins-zero-to-pro/?referralCode=" target="_blank">CI/CD with Jenkins</a> – Automate your pipelines.</div>
    <div class="course">🚀 <a href="https://www.udemy.com/course/introduction-to-linux-crash-course/" target="_blank">Free Linux Crash Course</a> – Get started with Linux.</div>
    <div class="course">🚀 <a href="https://www.udemy.com/course/aws-devops-practice-test-dop-c01-2023/?referralCode=D8209AD57D310A001C78" target="_blank">AWS DevOps Certification</a> – Practice for DOP-C01 exam.</div>

    <p><strong>👉 Watch this space for more updates. Happy learning!</strong></p>
</body>
</html>
"""

# Function to handle HTTP requests
app = func.FunctionApp()

@app.function_name(name="DevSecOpsHttp")
@app.route(route="courses", auth_level=func.AuthLevel.ANONYMOUS)  # Route without /api
def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        html_content,
        mimetype="text/html",
        status_code=200
    )
