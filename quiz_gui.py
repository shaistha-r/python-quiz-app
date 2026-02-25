import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

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
        self.q_index += 1
        if self.q_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Complete", f"🎯 Your score: {self.score}/{len(questions)}")
            self.root.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
