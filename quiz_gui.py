import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"], "answer": "Shakespeare"},
    {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "Which is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": "2"},
    {"question": "What is the boiling point of water?", "options": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"},
    {"question": "Who discovered gravity?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "answer": "Newton"},
    {"question": "Which language is used for web development?", "options": ["Python", "HTML", "C++", "Java"], "answer": "HTML"},
    {"question": "Which continent is India in?", "options": ["Africa", "Asia", "Europe", "Australia"], "answer": "Asia"},
    {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": "12"},
    {"question": "Which animal is known as the King of Jungle?", "options": ["Tiger", "Elephant", "Lion", "Leopard"], "answer": "Lion"},
    {"question": "Which device is used to store data?", "options": ["Monitor", "Keyboard", "Hard Drive", "Mouse"], "answer": "Hard Drive"},
    {"question": "Which is the fastest land animal?", "options": ["Lion", "Tiger", "Cheetah", "Horse"], "answer": "Cheetah"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.q_index = 0
        self.score = 0

        # Question label
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        # Score label
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Option buttons
        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Restart button (hidden initially)
        self.restart_button = tk.Button(root, text="Restart Quiz", command=self.restart_quiz)

        self.load_question()

    def load_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.buttons[i].config(text=option)

    def check_answer(self, i):
        selected = questions[self.q_index]["options"][i]
        correct = questions[self.q_index]["answer"]

        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ That's right!")
        else:
            messagebox.showerror("Wrong!", f"❌ The correct answer was: {correct}")

        # Update score
        self.score_label.config(text=f"Score: {self.score}")

        self.q_index += 1

        if self.q_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Complete", f"🎯 Your score: {self.score}/{len(questions)}")

            # Disable buttons
            for btn in self.buttons:
                btn.config(state="disabled")

            # Show restart button
            self.restart_button.pack(pady=20)

    def restart_quiz(self):
        self.q_index = 0
        self.score = 0
        self.score_label.config(text="Score: 0")

        # Enable buttons again
        for btn in self.buttons:
            btn.config(state="normal")

        # Hide restart button
        self.restart_button.pack_forget()

        self.load_question()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()
