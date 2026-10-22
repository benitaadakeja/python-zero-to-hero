# 🚀 Python Zero to Hero: Cloud & DevOps Journey

Welcome to my daily coding tracker! I am documenting my progression from Python fundamentals to AWS Cloud automation and DevOps engineering.

## 👩‍💻 Author
**Benita Oyinkansola Adakeja**  
*Focus: Cloud Engineering, AWS Infrastructure, and DevOps Automation*

## 🛠️ Tech Stack
- **Languages & SDKs:** Python 3, Boto3 (AWS SDK), Requests
- **DevOps & Cloud:** Docker, GitHub Actions (CI/CD), AWS (S3, IAM)
- **Environment:** Linux (Ubuntu/WSL2), Jupyter Notebooks, Terminal
- **Version Control:** Git & GitHub

---

## 🗺️ Learning Roadmap

- [x] **Phase 1:** Core Python Foundations
- [x] **Phase 2:** External Data, File I/O & APIs
- [x] **Phase 3:** AWS Cloud Automation (Boto3)
- [x] **Phase 4:** DevOps & Containerization (Docker)
- [x] **Phase 5:** CI/CD & Automated Workflows (GitHub Actions)
- [ ] **Phase 6:** Infrastructure as Code & Cloud Deployment

---

## 📅 Daily Log

### ✅ Day 1: Python Fundamentals
- **Topics Mastered:** Variables, Lists, Loops, Conditionals, Dictionaries, Functions, and Error Handling (`try/except`).
- **Project:** Built a local *Cloud Budget Auditor* script to automatically check infrastructure costs against a defined budget.

### ✅ Day 2: External Data & APIs
- **Topics Mastered:** JSON parsing, File Handling (`open()` with read/write/append modes), and HTTP requests.
- **Project:** Used the `requests` library to fetch and parse live JSON data directly from the GitHub API, and built an automated audit logging system.

### ✅ Day 3: AWS Cloud Automation (Boto3)
- **Topics Mastered:** AWS Boto3 SDK, IAM credential resolution, S3 bucket provisioning, cloud object storage, and the Infrastructure as Code (IaC) lifecycle.
- **Project:** Wrote a Python script to automatically provision a globally unique AWS S3 bucket, upload local security audit logs to the cloud, verify the storage state, and safely tear down the infrastructure to prevent billing charges.

### ✅ Day 4: Containerization with Docker
- **Topics Mastered:** Docker architecture (`Dockerfile`, Images, Containers), Linux base images (`python:3.10-slim`), dependency isolation (`requirements.txt`), Docker layer caching, and build-time (`RUN`) vs. runtime (`CMD`) execution parameters.
- **Project:** Containerized a Python GitHub API profile metadata fetcher (`app.py`) into a lightweight Docker image (`github-app`) and executed it inside an isolated Linux container.

### ✅ Day 5: CI/CD Pipelines with GitHub Actions
- **Topics Mastered:** Continuous Integration (CI) fundamentals, YAML syntax rules (indentation, structure), event triggers (`on: push`), GitHub managed runners (`ubuntu-latest`), workflow jobs/steps, reusable actions (`checkout`, `setup-python`), and automated container image validation.
- **Project:** Engineered an automated CI workflow (`.github/workflows/ci.yml`) that triggers on every push to `main`, provisions a cloud VM, installs dependencies, and automatically executes `docker build` to ensure image integrity.
