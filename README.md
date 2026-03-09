# Automated CI/CD Pipeline with Kubernetes Deployment

Every time I push code, the pipeline automatically builds a Docker image, scans it for vulnerabilities, pushes it to Docker Hub, and deploys it to Kubernetes on AWS EC2 — no manual steps needed.

---

## Tech Stack

- **GitHub Actions** — pipeline automation
- **Docker** — containerization
- **Trivy** — security vulnerability scanning
- **Docker Hub** — image registry
- **Kubernetes K3s** — container orchestration
- **AWS EC2** — cloud infrastructure

---

## Pipeline Flow

1. Push code to master
2. Docker image builds automatically
3. Trivy scans for CRITICAL and HIGH vulnerabilities
4. Image pushed to Docker Hub
5. App deployed to K3s on AWS EC2

---

## Project Structure
```
action/
├── app.py
├── Dockerfile
├── requirements.txt
├── k8s/
│   └── deployment.yaml
└── .github/
    └── workflows/
        └── app.yaml
```

---

## Run Locally
```bash
git clone https://github.com/RohitKharait/action.git
cd action
docker build -t myapp .
docker run -d -p 5000:5000 myapp
```

Open: http://localhost:5000

---

## GitHub Secrets Required

| Secret | Description |
|---|---|
| DOCKERHUB_USERNAME | Docker Hub username |
| DOCKERHUB_TOKEN | Docker Hub access token |
| KUBECONFIG | K3s cluster kubeconfig |

---

## Author

Rohit Kharait
GitHub: https://github.com/RohitKharait
LinkedIn: https://linkedin.com/in/rohitkharait
