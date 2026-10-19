# 🚀 Python Zero to Hero: Cloud & DevOps Journey

Welcome to my daily coding tracker! I am documenting my progression from Python fundamentals to AWS Cloud automation and DevOps engineering.

## 👩‍💻 Author
**Benita Oyinkansola Adakeja**  
*Focus: Cloud Engineering, AWS Infrastructure, and DevOps Automation*

## 🛠️ Tech Stack
- **Language:** Python 3
- **Environment:** Linux (Ubuntu/WSL2), Jupyter Notebooks
- **Version Control:** Git & GitHub

---

## 🗺️ Learning Roadmap

- [x] **Phase 1:** Core Python Foundations
- [x] **Phase 2:** External Data, File I/O & APIs
- [x] **Phase 3:** AWS Cloud Automation (Boto3)
- [x] **Phase 4:** DevOps & Containerization

---

## 📅 Daily Log

### ✅ Day 1: Python Fundamentals
- **Topics Mastered:** Variables, Lists, Loops, Conditionals, Dictionaries, Functions, and Error Handling (Try/Except).
- **Project:** Built a local *Cloud Budget Auditor* script to automatically check infrastructure costs against a defined budget.

### ✅ Day 2: External Data & APIs
- **Topics Mastered:** JSON parsing, File Handling (`open()` with read/write/append modes), and HTTP requests.
- **Project:** Used the `requests` library to fetch and parse live JSON data directly from the GitHub API, and built an automated audit logging system.

### ✅ Day 3: AWS Cloud Automation (Boto3)
- **Topics Mastered:** AWS Boto3 SDK, IAM credential resolution, S3 bucket provisioning, cloud object storage, and the Infrastructure as Code (IaC) lifecycle.
- **Project:** Wrote a Python script to automatically provision a globally unique AWS S3 bucket, upload local security audit logs to the cloud, verify the storage state, and safely tear down the infrastructure to prevent billing charges.

### ✅ Day 4: Containerization with Docker

- **Objective:** Package a standalone Python script and its dependencies into a portable, isolated Linux container using Docker.
- **Key Files Created:**
  - `app.py`: Modular Python script fetching user metadata from the GitHub REST API.
  - `requirements.txt`: Explicit dependency declaration file for `requests`.
  - `Dockerfile`: Multi-layer blueprint leveraging `python:3.10-slim`, configuring `WORKDIR /app`, and establishing build/runtime parameters.
- **Core DevOps Takeaways:**
  - **Build-Time vs. Runtime:** Understanding the operational difference between `RUN` (baked into the static image layer during build) and `CMD` (default entrypoint executed on container launch).
  - **Docker Layer Caching:** Ordering Dockerfile instructions (`COPY requirements.txt` before `COPY app.py`) to prevent unnecessary dependency downloads when code changes.
  - **Container Lifecycle:** Building (`docker build -t github-app .`) and running isolated execution environments (`docker run github-app`) in Linux.
