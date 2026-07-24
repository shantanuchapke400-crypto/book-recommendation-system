# 📚 Book Recommendation System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?logo=scikitlearn)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

A production-style **Machine Learning Book Recommendation System** that recommends books similar to the user's selection using **Collaborative Filtering with K-Nearest Neighbors (KNN)**.

The application provides an interactive **Streamlit** web interface, displays book cover images, and is fully containerized using **Docker** for cloud deployment on **Render**.

---

# 🌐 Live Demo

### 🚀 Try the application

**https://book-recommendation-system-hc8l.onrender.com/**

> **Note**
>
> The application is hosted on the Render Free Plan.
> If the application has been inactive, the first request may take around **30–60 seconds** while the server starts.

---

# ✨ Features

- 📚 Recommend similar books using Machine Learning
- 🧠 Collaborative Filtering with K-Nearest Neighbors (KNN)
- 🖼️ Displays book cover images
- 🎯 Interactive Streamlit web interface
- 📦 Modular project architecture
- 🐳 Dockerized application
- ☁️ Cloud deployment on Render
- ⚙️ Configuration-driven project structure

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Streamlit |
| Model Serialization | Pickle |
| Containerization | Docker |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
book-recommendation-system/
│
├── Books_recommendor/
│   ├── components/
│   ├── config/
│   ├── constants/
│   ├── entity/
│   ├── exception/
│   ├── logger/
│   ├── pipeline/
│   └── utils/
│
├── artifacts/
│   ├── serialized_objects/
│   └── trained_model/
│
├── config/
├── notebook/
├── templates/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🧠 How It Works

1. The user selects a book from the Streamlit interface.
2. The trained K-Nearest Neighbors model is loaded.
3. The selected book is converted into its feature representation.
4. The recommendation engine finds the nearest similar books.
5. Book cover URLs are retrieved.
6. Recommended books and their cover images are displayed.

---

# 📊 Dataset

This project is built using the **Book-Crossing Dataset**.

The dataset contains:

- 📚 Book Information
- ⭐ User Ratings
- 👤 User Details

The recommendation model is trained using collaborative filtering based on user rating patterns.

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/shantanuchapke400-crypto/book-recommendation-system.git

cd book-recommendation-system
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

### Activate

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t book-recommendation-system .
```

## Run Container

```bash
docker run -p 8501:8501 book-recommendation-system
```

---

# ☁️ Deployment

The application is deployed on **Render** using Docker.

Deployment workflow:

```
GitHub
      │
      ▼
Docker Image
      │
      ▼
Render
      │
      ▼
Live Web Application
```

---

# 📸 Screenshots

## Home Page

> Add your application home page screenshot here.

```
screenshots/home-page.png
```

---

## Recommendation Results

> Add recommendation output screenshot here.

```
screenshots/recommendation-results.png
```

---

# 📚 What I Learned

Building this project helped me gain practical experience in:

- Machine Learning Recommendation Systems
- Collaborative Filtering
- K-Nearest Neighbors
- Model Serialization
- Streamlit Application Development
- Docker Containerization
- Cloud Deployment using Render
- Project Structure & Configuration Management
- Debugging Production Deployment Issues

---

# 🔮 Future Improvements

- User Authentication
- Personalized User Profiles
- Hybrid Recommendation System
- Content-Based Recommendation
- REST API using FastAPI
- Database Integration
- Recommendation History
- CI/CD Pipeline
- Kubernetes Deployment

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

# 👨‍💻 Author

**Shantanu Chapke**

📧 Email:
shantanuchapke400@gmail.com

🐙 GitHub:
https://github.com/shantanuchapke400-crypto

💼 LinkedIn:
https://www.linkedin.com/in/shantanu-chapke-38038a375

---

# 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project helpful, consider giving it a **Star ⭐** on GitHub.

It helps support the project and motivates future development.