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

COURSE_LESSONS = {
    "Lesson 1 - Home Row": ["a s d f j k l ;", "f j d k s l ; a"],
    "Lesson 2 - Home Row Practice": ["a s d f j k l ;", "s d f j k l ; a"],
    "Lesson 3 - Top Row": ["q w e r t y u i o p", "e r t y u i o p q w"],
    "Lesson 4 - Top Row Practice": ["q w e r t y u i o p", "r t y u i o p q w e"],
    "Lesson 5 - Bottom Row": ["z x c v b n m , . /", "x c v b n m , . z"],
    "Lesson 6 - Bottom Row Practice": ["z x c v b n m , . /", "c v b n m , . z x"],
    "Lesson 7 - Numbers 1": ["1 2 3 4 5 6 7 8 9 0", "2 3 4 5 6 7 8 9 0 1"],
    "Lesson 8 - Numbers 2": ["1 2 3 4 5 6 7 8 9 0 - =", "2 3 4 5 6 7 8 9 0 - 1"],
    "Lesson 9 - Simple Words 1": ["cat dog sun pen car", "pen sun dog cat car"],
    "Lesson 10 - Simple Words 2": ["ball cup tree book star", "cup tree ball star book"],
    "Lesson 11 - Longer Words 1": ["apple orange mango banana", "mango banana apple orange"],
    "Lesson 12 - Longer Words 2": ["kiwi lemon grape peach", "grape peach kiwi lemon"],
    "Lesson 13 - Short Sentences 1": ["Typing is fun", "Fun typing is"],
    "Lesson 14 - Short Sentences 2": ["I like to play", "To play I like"],
    "Lesson 15 - Short Sentences 3": ["We love coding", "Coding we love"],
    "Lesson 16 - Simple Story 1": ["The cat runs fast", "Fast runs the cat"],
    "Lesson 17 - Simple Story 2": ["The dog jumps high", "Jumps the dog high"],
    "Lesson 18 - Fun Sentences 1": ["Sun is bright today", "Today sun is bright"],
    "Lesson 19 - Fun Sentences 2": ["I eat apple and banana", "Banana and apple I eat"],
    "Lesson 20 - Mixed Practice": ["Typing helps kids learn fast", "Kids learn fast typing helps"]
}


class TypingTutor:
    def __init__(self, root):
        self.root = root
        root.title("Usmaniya Typing Classes")
        root.geometry("1300x750")
        root.configure(bg="#1e1e2e")

        self.lesson_names = list(COURSE_LESSONS.keys())
        self.lesson_index = 0
        self.lesson_name = self.lesson_names[self.lesson_index]
        self.lesson_text = ""
        self.start_time = None
        self.typed_chars = 0
        self.correct_chars = 0

        self.create_home_page()

    # --- Home Page ---
    def create_home_page(self):
        self.clear_root()
        tk.Label(self.root, text="🖥️ Usmaniya Typing Classes", font=("Comic Sans MS", 28, "bold"),
                 fg="#ff79c6", bg="#1e1e2e").pack(pady=20)

        tk.Label(self.root, text="Select a Lesson to Start Typing", font=("Arial", 20), fg="#f1fa8c", bg="#1e1e2e").pack(pady=10)

        self.lesson_var = tk.StringVar(value=self.lesson_name)
        self.lesson_menu = tk.OptionMenu(self.root, self.lesson_var, *self.lesson_names)
        self.lesson_menu.config(font=("Arial", 16), bg="#44475a", fg="white", width=30)
        self.lesson_menu.pack(pady=20)

        tk.Button(self.root, text="Start Lesson", font=("Arial", 16), bg="#50fa7b", fg="black", command=self.start_typing_interface).pack(pady=30)

    # --- Clear root ---
    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- Start typing interface ---
    def start_typing_interface(self):
        self.lesson_index = self.lesson_names.index(self.lesson_var.get())
        self.lesson_name = self.lesson_names[self.lesson_index]
        self.clear_root()
        self.build_typing_ui()
        self.start_lesson()

    # --- Build typing UI ---
    def build_typing_ui(self):
        # Title
        tk.Label(self.root, text="🖥️ Usmaniya Typing Classes", font=("Comic Sans MS", 28, "bold"),
                 fg="#ff79c6", bg="#1e1e2e").pack(pady=10)

        # Current lesson
        self.current_lesson_var = tk.StringVar(value=self.lesson_name)
        self.lesson_menu = tk.OptionMenu(self.root, self.current_lesson_var, *self.lesson_names, command=self.select_lesson)
        self.lesson_menu.config(font=("Arial", 16), bg="#44475a", fg="white", width=25)
        self.lesson_menu.pack(pady=5)

        # Instruction
        tk.Label(self.root, text="Press ENTER to start typing. Focus on highlighted keys.",
                 font=("Arial", 14), fg="#f1fa8c", bg="#1e1e2e").pack(pady=5)

        # Lesson text
        self.word_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.word_frame.pack(pady=20)

        # Typing entry
        self.entry = tk.Entry(self.root, font=("Arial", 18), justify="center", width=50)
        self.entry.pack(ipady=8)
        self.entry.bind("<Return>", self.start_lesson)
        self.entry.bind("<KeyRelease>", self.key_release)

        # Stats
        self.stats_label = tk.Label(self.root, text="WPM: 0 | Accuracy: 0%", font=("Arial", 16), fg="#f1fa8c", bg="#1e1e2e")
        self.stats_label.pack(pady=10)

        # Keyboard
        self.keyboard_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.keyboard_frame.pack(pady=20)
        self.key_buttons = {}
        self.build_keyboard()

        # Hand/finger guide
        self.hand_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.hand_frame.pack(pady=10)
        self.hand_labels = {}
        for finger, color in FINGER_COLORS.items():
            lbl = tk.Label(self.hand_frame, text=finger.replace("_"," ").title(), bg=color, fg="white", width=12, height=2)
            lbl.pack(side="left", padx=3)
            self.hand_labels[finger] = lbl

    # --- Build keyboard ---
    def build_keyboard(self):
        for row in KEYBOARD_ROWS:
            row_frame = tk.Frame(self.keyboard_frame, bg="#1e1e2e")
            row_frame.pack()
            for key in row:
                key_lower = key.lower()
                width = 40 if key_lower=="space" else 5
                color = "#ff6b6b" if key_lower in ["a","s","d","f","j","k","l",";"] else "#44475a"
                btn = tk.Label(row_frame, text=key.upper(), width=width, height=2, bg=color, fg="white", bd=2, relief="raised")
                btn.pack(side="left", padx=2, pady=2)
                self.key_buttons[key_lower] = btn

    # --- Select lesson manually ---
    def select_lesson(self, lesson_name):
        self.lesson_index = self.lesson_names.index(lesson_name)
        self.start_lesson()

    # --- Start lesson ---
    def start_lesson(self, event=None):
        self.lesson_name = self.lesson_names[self.lesson_index]
        self.current_lesson_var.set(self.lesson_name)
        self.lesson_text = random.choice(COURSE_LESSONS[self.lesson_name])
        self.display_lesson_text()
        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.typed_chars = 0
        self.correct_chars = 0
        self.highlight_next_key()

    # --- Display lesson text ---
    def display_lesson_text(self):
        for widget in self.word_frame.winfo_children():
            widget.destroy()
        words = self.lesson_text.split(" ")
        for word in words:
            lbl = tk.Label(self.word_frame, text=word, font=("Arial", 28, "bold"), fg="white", bg="#1e1e2e")
            lbl.pack(side="left", padx=10)

    # --- Highlight next key dynamically ---
    def highlight_next_key(self):
        for k,b in self.key_buttons.items():
            if k in ["a","s","d","f","j","k","l",";"]:
                b.config(bg="#ff6b6b")
            elif k=="space":
                b.config(bg="#44475a")
            else:
                b.config(bg="#44475a")
        for lbl in self.hand_labels.values():
            lbl.config(relief="flat")

        typed_len = len(self.entry.get())
        if typed_len < len(self.lesson_text):
            next_char = self.lesson_text[typed_len].lower()
            if next_char==" ":
                next_char="space"
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

        # Highlight correct/incorrect words
        typed_len = len(typed)
        char_count = 0
        for lbl in self.word_frame.winfo_children():
            word_len = len(lbl.cget("text"))
            word_text = lbl.cget("text")
            correct_in_word = True
            for i in range(word_len):
                if char_count < typed_len:
                    if typed[char_count] != word_text[i]:
                        correct_in_word = False
                    char_count +=1
            lbl.config(fg="green" if correct_in_word and char_count<=typed_len else "white")

        # Lesson completed
        if typed == self.lesson_text:
            messagebox.showinfo("🎉 Well Done!", f"{self.lesson_name} Completed!")
            self.lesson_index = (self.lesson_index+1) % len(self.lesson_names)
            self.start_lesson()


if __name__=="__main__":
    root = tk.Tk()
    app = TypingTutor(root)
    root.mainloop()
