# 🔐 DevSecOps Demo Project

This project is **intentionally vulnerable** for demonstration purposes.
Used to show how DevSecOps tools automatically detect security issues.

---

## 🚨 Vulnerabilities Inside (for demo)

| # | Type | Location | Severity |
|---|------|----------|----------|
| 1 | Hardcoded Credentials | `app.py` line 8–10 | 🔴 Critical |
| 2 | SQL Injection | `app.py` line 20 | 🔴 Critical |
| 3 | Command Injection | `app.py` line 28 | 🔴 Critical |
| 4 | Weak Hashing (MD5) | `app.py` line 34 | 🟠 High |
| 5 | Path Traversal | `app.py` line 41 | 🔴 Critical |
| 6 | Debug Mode in Production | `app.py` line 45 | 🟡 Medium |

**Outdated dependencies with known CVEs** are also listed in `requirements.txt`.

---

## 🔍 How to scan with SonarCloud

1. Go to [sonarcloud.io](https://sonarcloud.io)
2. Sign in with GitHub
3. Click **"Analyze new project"**
4. Select this repository
5. Watch the vulnerabilities appear automatically ✅

## 📦 How to scan with Snyk

1. Go to [snyk.io](https://snyk.io)
2. Sign in with GitHub
3. Import this repository
4. Snyk will flag all CVEs in `requirements.txt` instantly ✅

---

> ⚠️ **DO NOT deploy this app.** It is for educational demonstration only.
