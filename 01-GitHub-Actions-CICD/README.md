# Project 01: Python CI Pipeline using GitHub Actions

![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue)
![Python](https://img.shields.io/badge/Python-3.9-yellow)
![Testing](https://img.shields.io/badge/Testing-Pytest-green)
![Platform](https://img.shields.io/badge/Platform-RHEL_9.8-red)

## 1. Project Overview

This project demonstrates how to build a Continuous Integration (CI) pipeline using GitHub Actions.

Whenever code is pushed to the `main` branch or a pull request is created against `main`, GitHub Actions automatically:

- Checks out the repository.
- Configures Python 3.9.
- Installs project dependencies.
- Executes automated tests using Pytest.
- Reports pipeline success or failure.

The objective is to understand how automated testing helps maintain software quality in a DevOps environment.

## 2. Project Objectives

- Understand Continuous Integration.
- Learn Git and GitHub version control.
- Build a GitHub Actions workflow.
- Configure a GitHub-hosted runner.
- Automate Python application testing.
- Understand workflow failures and troubleshooting.
- Implement a basic CI pipeline.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| RHEL 9.8 | Development environment |
| Python 3.9 | Application development |
| Git | Version control |
| GitHub | Remote repository |
| GitHub Actions | CI automation |
| YAML | Workflow configuration |
| Pytest | Automated testing |
| Ubuntu 24.04 | GitHub-hosted runner |

## 4. Architecture

Developer → Git Push → GitHub Repository → GitHub Actions Runner → Install Dependencies → Pytest → Pipeline Result.

### CI Workflow

1. Developer writes Python application code.
2. Developer commits and pushes changes.
3. GitHub detects the push event.
4. GitHub Actions starts an Ubuntu 24.04 runner.
5. Repository source code is checked out.
6. Python 3.9 is configured.
7. Dependencies are installed.
8. Pytest executes the automated tests.
9. GitHub Actions reports the result.

## 5. Project Structure

```text
DevOps-Projects/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── 01-GitHub-Actions-CICD/
    ├── app.py
    ├── test_app.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md
```

## 6. Application Features

The Python calculator application supports:

- Addition
- Subtraction
- Multiplication

## 7. Installation and Execution

### Clone the repository

```bash
git clone https://github.com/Arunkrishna02/DevOps-Projects.git
cd DevOps-Projects/01-GitHub-Actions-CICD
```

### Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

### Run automated tests

```bash
pytest -v
```

## 8. GitHub Actions Workflow

Workflow location:

```text
.github/workflows/ci.yml
```

The workflow uses:

- Trigger events: Push and Pull Request.
- Runner: Ubuntu 24.04.
- Python version: 3.9.
- Dependency installation: pip.
- Testing framework: Pytest.

## 9. Failure Detection and Troubleshooting

During implementation, an intentional application bug was introduced.

Incorrect implementation:

```python
def multiply(a, b):
    return a + b
```

Expected result:

```text
10 * 5 = 50
```

Actual result:

```text
10 + 5 = 15
```

Pytest detected the failure:

```text
2 passed, 1 failed
```

GitHub Actions marked the test job as failed because Pytest returned a non-zero exit code.

### Resolution

The multiplication function was corrected:

```python
def multiply(a, b):
    return a * b
```

After correction, all three automated tests passed.

## 10. Testing Results

| Test Scenario | Result |
|---|---|
| Addition | PASSED |
| Subtraction | PASSED |
| Multiplication | PASSED |
| Intentional bug detection | FAILED as expected |
| Corrected application | PASSED |

Final test result:

**3 passed, 0 failed.**

## 11. Key Learnings

- Difference between Git and GitHub.
- Git repository initialization and remote management.
- Git commits, branches and pushes.
- GitHub Actions workflows and events.
- Jobs, steps and runners.
- YAML configuration.
- Python virtual environments.
- Automated testing using Pytest.
- CI failure detection and troubleshooting.
- Runner version compatibility.

## 12. Future Improvements

- Add code quality checks using Flake8.
- Add code coverage reports.
- Introduce Docker image building.
- Add automated deployment.
- Integrate security scanning.

## 13. Repository

GitHub: https://github.com/Arunkrishna02/DevOps-Projects

## 14. Conclusion

Successfully implemented a basic Continuous Integration pipeline using GitHub Actions and Pytest.

This project demonstrates how developers can automate application testing, detect errors early, troubleshoot pipeline failures and maintain a reliable development workflow.
