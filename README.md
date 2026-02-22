# ☁️ Cloud Web App – AWS EC2 Deployment with Nginx & Flask

A cloud-hosted Python Flask web application deployed on **AWS EC2**, served through **Nginx reverse proxy**, and secured using **AWS Security Groups**.

This project demonstrates real-world cloud deployment, Linux server management, and basic production-style web hosting.

---

## 🚀 Tech Stack
- **Cloud:** AWS EC2 (Ubuntu)
- **Web Server:** Nginx
- **Backend:** Python (Flask)
- **OS:** Linux (Ubuntu 24.04)
- **Networking & Security:** AWS Security Groups, SSH
- **Tools:** Git, GitHub

---

## 🧠 What This Project Demonstrates
- Launching and managing an EC2 instance on AWS
- Configuring inbound security group rules (SSH & HTTP)
- Installing and running Nginx on a Linux server
- Deploying a Flask application on EC2
- Using Nginx as a reverse proxy for Flask
- Exposing a live web application using a public IP

---

## 🏗️ Architecture

```text
User Browser
     ↓
Internet
     ↓
AWS EC2 (Public IP)
     ↓
Nginx (Port 80)
     ↓
Flask App (Port 5000)
