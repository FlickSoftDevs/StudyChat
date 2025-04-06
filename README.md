<div align="center">
  <img width="30%" src="readme/hd.png">
  
  # Discussion Forum  
  *A Django-based collaborative discussion platform*
</div>

---

## 🧠 Overview

**Discussion Forum** is a web-based platform built using Django. It aims to bring people together for sharing knowledge, engaging in educational and social discussions, and building a strong community of learners.

Users can join, create discussion rooms, engage in real-time discussions, and manage their personal profiles.

---

## 🌍 Vision & Strategy

> **Created by [William](https://nyumbachap.com)**  
> 📞 **Contact**: 0629712678

**Vision:**  
The vision for the Discussion Forum is to bring together developers, students, and all Tanzanians to participate in discussions that will elevate their skills in the technology sector.

**Development Strategy:**
- Adding AI Chatbot support for quick question answers.
- Expanding discussions into professional, business, and community sectors.
- Implementing voice/video discussions.
- Enabling discussion collaboration through social media integration.

---

## ✨ Features

- 🔐 **User Authentication** – Secure Sign Up / Login functionality.
- 💬 **Discussion Rooms** – Create or join any discussion room.
- ⏱️ **Real-Time Chat** – Engage in real-time conversations.
- 🙋‍♂️ **User Profiles** – Edit and view user profiles.
- 📱 **Mobile Responsive** – Works seamlessly on all devices.

---

## 🚀 How to Use

1. Visit `http://127.0.0.1:8000/` after starting the server.
2. Register an account or log in if you already have one.
3. Search for or create a discussion room.
4. Share opinions, ask questions, provide help, or respond to existing topics.
5. Visit *User Profiles* to learn more about others.

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.x  
- pip  
- Git  

### Installation Guide

```bash
git clone https://github.com/Barackwilliam/StudyChat.git
cd Discussion-Forum-Django
pip install virtualenv
virtualenv env
# Activate environment
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
