# Password Checker 🔐

This is my first beginner project as I start getting into cybersecurity and Python.  
The goal of this project was to build a simple password checker that teaches the basics of secure password practices **and** introduces a cyber concept: checking passwords against a leaked breach list.

It's a small project, but it's a realistic way to understand how weak passwords and leaked credentials put users at risk.

---

## What This Project Does

### ✔ Password Strength Checker
The program checks if a password contains:
- At least **8 characters**
- **Uppercase** and **lowercase** letters
- At least one **digit**
- At least one **special character** (`@$!%*?&#`)
- No **repeating consecutive characters**

It gives clear feedback to help users build a stronger password.

### Breach List Checker
The project also checks the password against a local file called `passwords.txt` which contains a list of leaked passwords.  
This teaches a real cybersecurity concept:  
➡ Attackers often use breached passwords in large “credential stuffing” attacks.

---

## Why I Built This
I'm learning cybersecurity and wanted a small but realistic project.  
This combines:
- Python programming  
- Regex  
- Basic security concepts  
- Checking for leaked passwords (similar idea to HaveIBeenPwned)

This project is a foundation I plan to build on as I keep learning.

---
