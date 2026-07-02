import tkinter as tk
from tkinter import messagebox
import random
import time

# --- Keyboard layout ---
KEYBOARD_ROWS = [
    ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace"],
    ["Tab","Q","W","E","R","T","Y","U","I","O","P","[","]","\\"],
    ["Caps","A","S","D","F","G","H","J","K","L",";","'","Enter"],
    ["Shift","Z","X","C","V","B","N","M",",",".","/","Shift"],
    ["Space"]
]

# --- Finger mapping ---
FINGER_KEYS = {
    "left_pinky":["`","1","q","a","z","tab","caps","shift"],
    "left_ring":["2","w","s","x"],
    "left_middle":["3","e","d","c"],
    "left_index":["4","5","r","t","f","g","v","b"],
    "right_index":["6","7","y","u","h","j","n","m"],
    "right_middle":["8","i","k",","],
    "right_ring":["9","o","l","."],
    "right_pinky":["0","-","=","p","[","]","\\",";","'","enter","backspace","shift"],
    "thumb":["space"]
}

FINGER_COLORS = {
    "left_pinky":"#ff6b6b", "left_ring":"#feca57", "left_middle":"#48dbfb", "left_index":"#1dd1a1",
    "right_index":"#ff9ff3", "right_middle":"#576574", "right_ring":"#341f97", "right_pinky":"#ee5253", "thumb":"#f368e0"
}

# --- Full course lessons ---
COURSE_LESSONS = {
    "Lesson 1 - Home Row": ["a s d f j k l ;", "f j d k s l a ;"],
    "Lesson 2 - Top Row": ["q w e r t y u i o p", "e r t y u i o p q w"],
    "Lesson 3 - Bottom Row": ["z x c v b n m , . /", "x c v b n m , . z"],
    "Lesson 4 - Numbers": ["1 2 3 4 5 6 7 8 9 0 - =", "2 3 4 5 6 7 8 9 0 - 1"],
    "Lesson 5 - Words": ["cat dog ball sun car pen cup tree", "apple orange mango banana kiwi lemon"],
    "Lesson 6 - Sentences": ["Typing is fun for kids", "Practice daily to improve speed"]
}

class UsmaniyaTypingTutor:
    def __init__(self, root):
        self.root = root
        root.title("Usmaniya Typing Classes")
        root.geometry("1300x750")
        root.configure(bg="#1e1e2e")

        self.lesson_name = "Lesson 1 - Home Row"
        self.lesson_text = ""
        self.start_time = None
        self.typed_chars = 0
        self.correct_chars = 0

        # --- Title ---
        self.title = tk.Label(root, text="🖥️ Usmaniya Typing Classes", font=("Comic Sans MS", 28, "bold"),
                              fg="#ff79c6", bg="#1e1e2e")
        self.title.pack(pady=10)

        # --- Lesson selector ---
        self.lesson_var = tk.StringVar(value=self.lesson_name)
        self.lesson_menu = tk.OptionMenu(root, self.lesson_var, *COURSE_LESSONS.keys(), command=self.select_lesson)
        self.lesson_menu.config(font=("Arial", 14), bg="#44475a", fg="white")
        self.lesson_menu.pack(pady=5)

        # --- Instruction ---
        self.instruction = tk.Label(root, text="Press ENTER to start typing. Focus on highlighted keys.",
                                    font=("Arial", 14), fg="#f1fa8c", bg="#1e1e2e")
        self.instruction.pack(pady=5)

        # --- Lesson text ---
        self.word_label = tk.Label(root, text="", font=("Arial", 24, "bold"), fg="#50fa7b", bg="#1e1e2e")
        self.word_label.pack(pady=20)

        # --- Typing entry ---
        self.entry = tk.Entry(root, font=("Arial", 18), justify="center")
        self.entry.pack(ipady=8)
        self.entry.bind("<Return>", self.start_lesson)
        self.entry.bind("<KeyRelease>", self.key_release)

        # --- Stats ---
        self.stats_label = tk.Label(root, text="WPM: 0 | Accuracy: 0%", font=("Arial", 16), fg="#f1fa8c", bg="#1e1e2e")
        self.stats_label.pack(pady=10)

        # --- Keyboard ---
        self.keyboard_frame = tk.Frame(root, bg="#1e1e2e")
        self.keyboard_frame.pack(pady=20)
        self.key_buttons = {}
        self.build_keyboard()

        # --- Hand/finger guide ---
        self.hand_frame = tk.Frame(root, bg="#1e1e2e")
        self.hand_frame.pack(pady=10)
        self.hand_labels = {}
        for finger, color in FINGER_COLORS.items():
            lbl = tk.Label(self.hand_frame, text=finger.replace("_"," ").title(), bg=color, fg="white", width=12, height=2)
            lbl.pack(side="left", padx=3)
            self.hand_labels[finger] = lbl

    # --- Build keyboard buttons ---
    def build_keyboard(self):
        for row in KEYBOARD_ROWS:
            row_frame = tk.Frame(self.keyboard_frame, bg="#1e1e2e")
            row_frame.pack()
            for key in row:
                key_lower = key.lower()
                color = "#ff6b6b" if key_lower in ["a","s","d","f","j","k","l",";"] else "#44475a"
                btn = tk.Label(row_frame, text=key.upper(), width=5, height=2, bg=color, fg="white", bd=2, relief="raised")
                btn.pack(side="left", padx=2, pady=2)
                self.key_buttons[key_lower] = btn

    # --- Select lesson ---
    def select_lesson(self, lesson_name):
        self.lesson_name = lesson_name
        self.start_lesson()

    # --- Start lesson ---
    def start_lesson(self, event=None):
        self.lesson_text = random.choice(COURSE_LESSONS[self.lesson_name])
        self.word_label.config(text=self.lesson_text)
        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.typed_chars = 0
        self.correct_chars = 0
        self.highlight_next_key()

    # --- Highlight next key and finger ---
    def highlight_next_key(self):
        # Reset keyboard colors
        for k,b in self.key_buttons.items():
            if k in ["a","s","d","f","j","k","l",";"]:
                b.config(bg="#ff6b6b")
            else:
                b.config(bg="#44475a")
        # Reset fingers
        for lbl in self.hand_labels.values():
            lbl.config(relief="flat")
        # Highlight next char
        typed_len = len(self.entry.get())
        if typed_len < len(self.lesson_text):
            next_char = self.lesson_text[typed_len].lower()
            if next_char == " ":
                next_char = "space"
            if next_char in self.key_buttons:
                self.key_buttons[next_char].config(bg="#50fa7b")
                for finger, keys in FINGER_KEYS.items():
                    if next_char in keys:
                        self.hand_labels[finger].config(relief="raised")

    # --- Key release ---
    def key_release(self, event=None):
        typed = self.entry.get()
        self.typed_chars = len(typed)
        self.correct_chars = sum(1 for i,c in enumerate(typed) if i<len(self.lesson_text) and c==self.lesson_text[i])
        elapsed = max(time.time()-self.start_time,1)
        wpm = (self.correct_chars/5)/(elapsed/60)
        accuracy = (self.correct_chars/self.typed_chars)*100 if self.typed_chars>0 else 0
        self.stats_label.config(text=f"WPM: {wpm:.1f} | Accuracy: {accuracy:.1f}%")
        self.highlight_next_key()
        if typed == self.lesson_text:
            messagebox.showinfo("🎉 Well Done!", "Lesson Completed! Press ENTER for next.")
            self.start_lesson()

# --- Run the tutor ---
if __name__=="__main__":
    root = tk.Tk()
    app = UsmaniyaTypingTutor(root)
    root.mainloop()
