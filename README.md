# 🚀 Enterprise Cloud & DevOps Roadmap: Python to AWS IaC/CI-CD

[![CI/CD Pipeline](https://github.com/benitaadakeja/python-zero-to-hero/actions/workflows/ci.yml/badge.svg)](https://github.com/benitaadakeja/python-zero-to-hero/actions/workflows/ci.yml)
![Terraform](https://img.shields.io/badge/IaC-Terraform_v1.5+-623CE4?logo=terraform&logoColor=white)
![AWS ECR](https://img.shields.io/badge/Cloud-AWS_ECR-FF9900?logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker_24+-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python_3.10-3776AB?logo=python&logoColor=white)
![Security Scanned](https://img.shields.io/badge/Security-ECR_Scan_On_Push-success?logo=guardsquare&logoColor=white)

An end-to-end, production-ready DevOps portfolio project demonstrating modular application development, containerization, Infrastructure as Code (IaC) with HashiCorp Terraform, automated CI/CD with GitHub Actions, and cloud registry publishing on Amazon Web Services (AWS).

---

## 🏗️ System Architecture & Wrkflow
```
┌─────────────────────────────────────────────────────────────────────┐
│                   1. LOCAL WORKSPACE (WSL2 / Linux)                 │
│  ┌──────────────┐     ┌────────────────┐     ┌───────────────────┐  │
│  │ Python 3 App │ ──> │ Docker Build   │ ──> │ Terraform HCL Code│  │
│  └──────────────┘     └────────────────┘     └───────────────────┘  │
└──────────────────────────────────┬──────────────────────────────────┘
                                   │ git push origin main
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   2. GITHUB ACTIONS CI/CD ENGINE                    │
│  ┌──────────────────┐     ┌──────────────────┐     ┌─────────────┐  │
│  │ Checkout & Setup │ ──> │ Authenticate AWS │ ──> │ Build Image │  │
│  └──────────────────┘     └──────────────────┘     ───────┬──────┘  │
└───────────────────────────────────────────────────────────┼─────────┘
                                   HTTPS / TLS 1.3          │ docker push
                                                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   3. AMAZON WEB SERVICES (AWS CLOUD)                │
│  AWS ECR Registry: github-app-repo                                  │
│   ├── Security Scanning : scan_on_push = true                       │
│   ├── Traceable Tag     : :<commit-sha>                             │
│   └── Production Pointer: :latest                                   │
└─────────────────────────────────────────────────────────────────────┘
```
## 🛠️ Technology Stack & Specifications

* **Application Core:** Python 3.10 (`requests`, `json`, modular error handling)
* **Containerization:** Docker Engine, Dockerfile multi-layer optimization, `python:3.10-slim` base image
* **Infrastructure as Code (IaC):** Terraform CLI (v1.5+), HashiCorp AWS Provider (`~> 5.0`), HCL2 syntax
* **CI/CD Orchestration:** GitHub Actions workflows (`ubuntu-latest` runners, `aws-actions` suite)
* **Cloud Infrastructure:** Amazon Web Services (AWS IAM, ECR, S3, STS)
* **Local Operating Environment:** Linux / WSL2 (Ubuntu 22.04 LTS), Bash, Git, AWS CLI v2

---

## 📋 Detailed 8-Day Roadmap & Implementation Logs

### Day 1: Python Core Foundations & Script Automation
* **Key Competencies:** Control structures, custom error handling (`try/except`), environment variable parsing, clean code practices.
* **Deliverable:** Engineered a local *Cloud Audit CLI* script (`budget_auditor.py`) to parse infrastructure expenses against dynamic threshold limits.

### Day 2: File I/O, REST APIs & Telemetry Logs
* **Key Competencies:** HTTP REST API interactions (`requests`), JSON serialization/deserialization, audit trail file logging (`open()` append mode).
* **Deliverable:** Built an automated GitHub API scraper (`app.py`) that extracts profile metadata, repositories, and activity metrics, generating timestamped audit log files.

### Day 3: Cloud Storage Automation via AWS SDK (Boto3)
* **Key Competencies:** AWS SDK initialization, programmatic IAM credential resolution, S3 bucket lifecycle operations, cloud error handling (`botocore.exceptions.ClientError`).
* **Deliverable:** Created an automated Python utility (`s3_sync.py`) to provision globally unique S3 buckets, upload encrypted audit logs, verify cloud object integrity, and perform clean teardowns.

### Day 4: Docker Containerization & Image Optimization
* **Key Competencies:** Microservices containerization, lightweight base image selection (`python:3.10-slim`), non-root security principles, build layer caching, `.dockerignore` optimization.
* **Deliverable:** Authored an optimized `Dockerfile` encapsulating the Python application, reducing container image footprint to under 150 MB.

### Day 5: CI/CD Pipeline Automation with GitHub Actions
* **Key Competencies:** Event-driven pipeline execution (`on: push`), YAML workflow syntax, workflow job dependency trees, automated testing environment setup, repository status badging.
* **Deliverable:** Implemented `.github/workflows/ci.yml` to automatically trigger virtual machine runners, install dependencies, and test container builds on every commit.

### Day 6: Infrastructure as Code (IaC) via Terraform
* **Key Competencies:** Declarative infrastructure definition, HCL syntax (`provider`, `resource`, `variable`, `output`), state file tracking (`terraform.tfstate`), binary execution plan generation (`terraform plan -out`).
* **Deliverable:** Declaratively provisioned an AWS Elastic Container Registry (`github-app-repo`) in `us-east-1` with server-side AES256 encryption and automated CVE vulnerability scanning (`scanOnPush = true`).

### Day 7: Automated Cloud Registry Publishing (ECR Integration)
* **Key Competencies:** Encrypted GitHub Actions secrets, zero-trust credential pass-through (`aws-actions/configure-aws-credentials`), ECR authentication tokens, dual-tagging strategy (`github.sha` + `latest`).
* **Deliverable:** Expanded the CI/CD pipeline to automatically log into AWS, build the Docker container image, attach traceable Git SHA tags, and publish artifacts directly to AWS ECR upon `main` branch push.

### Day 8: Production Hardening, Security Matrix & Capstone Wrap-Up
* **Key Competencies:** Least-privilege access control, vulnerability assessment, state file isolation, deployment audit verification, infrastructure lifecycle teardown (`terraform destroy`).
* **Deliverable:** Complete architecture audit, security hardening documentation, execution verification logs, and repository portfolio polish.

---

## 🔒 Security & Production Hardening Matrix

| Security Domain | Risk Addressed | Implementation Mechanism |
| :--- | :--- | :--- |
| **Credential Protection** | Plaintext secret exposure in Git history | AWS API keys secured in **GitHub Encrypted Secrets**; zero secrets in codebase. |
| **Container Security** | Vulnerable base image OS packages | AWS ECR **Scan on Push** automatically scans image layers for known CVE vulnerabilities. |
| **Deployment Auditing** | Inability to map cloud image to source code | Docker images are dual-tagged with the **40-character Git commit SHA** for 1:1 traceability. |
| **State File Safety** | Infrastructure metadata & token leakage | `.gitignore` explicitly blocks `.tfstate`, `tfplan`, and `.terraform/` binary caches. |
| **Deterministic Execution**| Configuration drift and mid-flight changes | Automated deployments enforce binary plan output files (`terraform plan -out=tfplan`). |

---

## ⚙️ Local Setup & Deployment Guide

### Prerequisites
* **WSL2 / Linux Terminal** with Git and Curl installed.
* **Docker Engine** (or Docker Desktop configured for WSL2).
* **AWS CLI v2** configured via `aws configure`.
* **Terraform CLI** (v1.5.0 or newer).

### 1. Clone & Test Application Locally
```bash
git clone [https://github.com/benitaadakeja/python-zero-to-hero.git](https://github.com/benitaadakeja/python-zero-to-hero.git)
cd python-zero-to-hero

# Build Docker Image
docker build -t github-app .

# Run Container Locally
docker run --rm github-app

### 2. Provision AWS Infrastructure via Terraform
```bash
cd terraform

# Initialize Provider Plugins
terraform init

# Generate Execution Plan
terraform plan -out=tfplan

# Apply Configuration to AWS
terraform apply tfplan
```

### 3. Verify Deployment via AWS CLI
```bash
aws ecr describe-repositories --repository-names github-app-repo
aws ecr list-images --repository-name github-app-repo
```

### 4. Clean Up Cloud Resources
```bash
cd terraform
terraform destroy -auto-approve
```

---

## 🔑 Required GitHub Repository Secrets

Configure the following key-value pairs in **Settings ➔ Secrets and variables ➔ Actions**:

| Secret Name | Description | Example Value |
| :--- | :--- | :--- |
| `AWS_ACCESS_KEY_ID` | IAM User Programmatic Access Key | `AKIAXXXXXXXXXXXXXXXX` |
| `AWS_SECRET_ACCESS_KEY` | IAM User Secret Signing Key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_REGION` | Target AWS Cloud Region | `us-east-1` |

---

## 👤 Author & Acknowledgments

* **Author:** Benita Oyinkansola Adakeja
* **Role:** Computer Science Undergraduate & AWS Certified Cloud Practitioner
* **Repository:** [github.com/benitaadakeja/python-zero-to-hero](https://github.com/benitaadakeja/python-zero-to-hero)
