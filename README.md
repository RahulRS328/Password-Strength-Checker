# 🔐 Advanced Password Strength Checker

A modern **Flask-based web app** that helps you test, analyze, and improve your passwords.  
It gives you a **strength score**, **security analysis**, and **suggestions** to make your password stronger — all in a clean web interface.

---

## 🚀 Features

✅ Password strength analysis  
✅ Password breach check (using HaveIBeenPwned API - optional)  
✅ Suggestions for stronger passwords  
✅ Login / Welcome screen  
✅ Responsive web interface (works on any browser)  

---

## 🛠️ Installation & Setup

Follow these simple steps to run it locally 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RahulRS328/Password-Strength-Checker.git
cd Password-Strength-Checker

### 2️⃣ Create a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate     # On Linux / macOS
# OR
venv\Scripts\activate        # On Windows

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Run the Application

python app.py

Then open your browser and visit 👉
http://127.0.0.1:5000/

### 🧠 Usage

Run the Flask app.

Enter your password on the main page.

Click “Analyze Password” to view:

Strength score (0–4)

Feedback message

Suggestions for improvement

Optional breach check

### 📂 Project Structure

Password-Strength-Checker/
│
├── app.py                  # Main Flask app
├── analysis.py             # Password analysis logic
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── base.html
│   ├── login.html
│   └── index.html
├── static/
│   └── style.css           # Frontend styling
└── README.md               # Project documentation

### 🤝 Contributing
Pull requests are welcome!
If you’d like to improve this project, fork it and submit a PR.

🧑‍💻 Author

Rahul R S
📘 [GitHub Profile](https://github.com/RahulRS328)

