# 🧠 Marg - Career Recommendation System

**Marg** is a career recommendation web application designed for recent SEE graduates. It allows users to take a short quiz and receive their top 3 career recommendations using a trained **Random Forest Classifier**. The platform also features **career-related blogs**, a **chatbot** for assistance, **comment sections** for interaction, and a **clean, user-friendly UI** built using **HTML, CSS, and JavaScript**, with a **Django + Scikit-learn** backend.

![Marg Banner](https://github.com/user-attachments/assets/581601a6-0e7e-4f65-ac4d-e0f0deee9f4d)

---

## 💻 Tech Stack

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge\&logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge\&logo=javascript\&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge\&logo=django\&logoColor=white)
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge\&logo=python\&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge\&logo=github\&logoColor=white)

---

## 🔍 Table of Contents

* [🚀 Demo](#-demo)
* [✨ Features](#-features)
* [📂 Folder Structure](#-folder-structure)
* [⚙️ Installation](#-installation)
* [🔐 Environment Variables](#-environment-variables)
* [🖼️ Screenshots](#-screenshots)
* [📜 License](#-license)
* [👩‍💻 Author](#-author)

---

## 🚀 Demo

📽️ **Video Demo:**
[Watch on Google Drive](https://drive.google.com/file/d/1LWudR6H7c1o_CBUbyT9MjaoWPcVVr85w/view?usp=drive_link) 

---

## ✨ Features

✅ Career Quiz for recent SEE graduates </br>
✅ Top 3 career recommendations based on quiz answers </br>
✅ Machine Learning (Random Forest Classifier) backend </br>
✅ Blog section with educational content </br>
✅ User Dashboard to Create, Read, Update, and Delete (CRUD) blog posts </br>
✅ Chatbot for user guidance </br>
✅ Comment system on blogs for interaction </br>
✅ Contact Us and About Us pages </br>
✅ Clean, intuitive, mobile-friendly UI </br>

---

## 📂 Folder Structure

```
marg/
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
├── backend/
│   ├── marg/
│   │   └── settings.py
│   ├── recommender/
│   │   └── model.py
│   └── manage.py
├── media/
├── static/
├── templates/
└── requirements.txt
```

---

## ⚙️ Installation

### 🔹 Frontend Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/marg.git
cd marg/frontend

# 2. Open index.html in your browser or serve with live server
```

---

### 🔹 Backend Setup (Django + ML)

```bash
# 1. Navigate to the backend folder
cd marg/backend

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate for Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Run server
python manage.py runserver
```

---

## 🔐 Environment Variables

Create a `.env` file in the Django backend root:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
```

---

## 🖼️ Screenshots

### 🔹 Login And Register Page

![Register](https://github.com/user-attachments/assets/e207a8e6-07db-48ed-93ed-1c1ff9f5669b)
![Login](https://github.com/user-attachments/assets/87e1cb1c-5071-45ac-a2a4-c778778fe018)

### 🔹 Home Page with Chatbot

![Home](https://github.com/user-attachments/assets/7f439a9b-fde8-4691-8468-c27e3c13e4a2)

### 🔹 Quiz Starting Interface

![Quiz](https://github.com/user-attachments/assets/23098a0d-127b-49be-9552-c7cea0ddbe24)

### 🔹 Quiz Interface

![Quiz](https://github.com/user-attachments/assets/5514beaa-f8a1-4354-826a-ed711a0b5081)

### 🔹 Career Results

![Results](https://github.com/user-attachments/assets/df7aa95d-b0fb-4481-ac55-396df263c37c)

### 🔹 Blog Page

![Blog](https://github.com/user-attachments/assets/c798828a-5657-4ee6-b401-8cd594998b8d)

### 🔹Create Blog 

![Blog](https://github.com/user-attachments/assets/5b9fd9df-2026-4436-b5e6-9f76c08a2a6e)

### 🔹 About Us Page

![Contact](https://github.com/user-attachments/assets/66c87d40-6102-46a5-85e1-633d9a7d744f)

### 🔹 Contact Page

![Contact](https://github.com/user-attachments/assets/05a20515-9f17-485d-92f5-cb6fa84eadfc)

### 🔹 Dashboard Page

![Contact](https://github.com/user-attachments/assets/7f7e814a-ad5e-4af1-a6bc-0e22b121c349)

---

## 🧠 Machine Learning Model

* 🎯 **Algorithm:** Random Forest Classifier
* 📚 **Library Used:** Scikit-learn
* 🔢 **Input:** Quiz responses
* 🧾 **Output:** Top 3 career predictions
* 🧠 The model is trained on a preprocessed career dataset and integrated into Django views for dynamic predictions.

---

## 📜 License

This project is open for educational and personal use. Please give proper credits if reused.
I’m not responsible for any damages, bugs, or crashes caused by modifications or misuses.

---

## 👩‍💻 Author

Created with 💙 by **Roxks**
🔗 [GitHub](https://github.com/rakxya111) • [LinkedIn](https://linkedin.com/in/rakshya-bhuju13)

---

> 🌱 *Feel free to fork, clone, and contribute. Pull requests are welcome!*

