# Damn Vulnerable Django Server
<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

⚠️ **WARNING: This is a deliberately vulnerable application. DO NOT deploy on production systems or expose to the internet.**

A deliberately vulnerable Django web application designed to demonstrate command injection vulnerabilities for educational purposes.

## Overview

This application implements an intentionally unsafe command execution interface to help security researchers and developers understand:
- How command injection vulnerabilities work
- Why proper input sanitization is critical
- Common patterns that lead to command injection
- Best practices for secure command execution

## Technical Details

The application exposes a simple web interface with:
- A text input field accepting arbitrary user input
- A submit button that executes the input as system commands
- Direct output display of command execution results

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install django
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Educational Use

This application demonstrates several critical security concepts:

1. Command Injection
   - Direct execution of user input
   - Shell command parsing behavior
   - Command chaining techniques

2. Secure Coding Practices (by negative example)
   - Input validation importance
   - Command sanitization
   - Output encoding

## Security Notice

This application deliberately contains dangerous vulnerabilities:

- Arbitrary command execution
- No input validation
- Direct system access

**Usage Guidelines:**

- Run only in isolated development environments
- Never expose to networks
- Use only for learning and research
- Do not use any code patterns demonstrated here in production

## Legal Disclaimer

This software is provided for educational purposes only. Users are responsible for complying with applicable laws and regulations. The authors are not responsible for any misuse or damage.

## License

MIT License - See LICENSE file for details
