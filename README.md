# 🧠 Python Quiz App (Tkinter GUI)

A simple object-oriented quiz application built using Python and tkinter. It pulls questions from a list of dictionaries and quizzes the user with a graphical interface.

---

## 📸 Screenshot

![Quiz Screenshot](https://via.placeholder.com/600x300?text=Quiz+App+GUI) <!-- You can add your own screenshot here -->

---

## 🚀 Features

- GUI built with `tkinter`
- Interactive true/false quiz
- Automatic score tracking
- Easy to extend with more questions

---

## 📁 Project Structure
```bash
quiz-app/
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
├── ui.py
├── README.md         ← we'll create this
├── .gitignore         ← optional, but recommended
```
## 🛠 How to Run
### 🔧 Requirements
- Python
-  3.x
### ▶️ Run the App
```bash
python main.py
```
## ✏️ How It Works
1. data.py contains the raw question data.
2. main.py loads data into Question objects.
3. quiz_brain.py controls question flow and scoring.
4. ui.py builds the graphical interface and updates UI dynamically.

## 🧪 Example Question Format
```bash

question_data = [
    {"question": "The sky is blue.", "correct_answer": "True"},
    {"question": "Cats bark.", "correct_answer": "False"},
]
```
## ✅ Step 3: Create `.gitignore`
```bash
Create a file named `.gitignore` and add:

```txt
__pycache__/
*.pyc
*.pyo
*.log
*.env
.venv/
```
## 📄 License
MIT License — free to use, modify, and share!
## 👨‍💻 Author
Sayan Sanki



