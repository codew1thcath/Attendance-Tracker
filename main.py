import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# ── Database Setup ─────────────────────────────────────────
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    time TEXT
)
""")
conn.commit()

# ── Color & Font Theme ──────────────────────────────────────
BG         = "#FFF0F5"       # Lavender blush background
PRIMARY    = "#E91E8C"       # Hot pink
SECONDARY  = "#FF69B4"       # Light pink
ACCENT     = "#FF1493"       # Deep pink
TEXT_DARK  = "#3D0026"       # Dark maroon text
TEXT_LIGHT = "#FFFFFF"
CARD_BG    = "#FFD6E7"       # Soft pink card
ROW_ODD    = "#FFE4F0"
ROW_EVEN   = "#FFF0F8"

FONT_TITLE  = ("Georgia", 22, "bold")
FONT_LABEL  = ("Georgia", 12, "bold")
FONT_ENTRY  = ("Courier New", 12, "bold")
FONT_BTN    = ("Georgia", 11, "bold")
FONT_TABLE  = ("Courier New", 10, "bold")

# ── Functions ───────────────────────────────────────────────
def mark_attendance():
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning("Oops!", "Please enter a name! 💕")
        return

    now  = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    cursor.execute(
        "INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)",
        (name, date, time)
    )
    conn.commit()
    messagebox.showinfo("Success! 🌸", f"{name} marked present!")
    entry_name.delete(0, tk.END)
    view_attendance()

def view_attendance():
    # Clear existing rows
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM attendance ORDER BY id DESC")
    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        tag = "odd" if i % 2 == 0 else "even"
        tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]), tags=(tag,))

    lbl_count.config(text=f"Total Records: {len(rows)}")

def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Oops!", "Please select a record to delete! 💕")
        return

    confirm = messagebox.askyesno("Delete?", "Delete selected record?")
    if confirm:
        item = tree.item(selected[0])
        record_id = item["values"][0]
        cursor.execute("DELETE FROM attendance WHERE id = ?", (record_id,))
        conn.commit()
        view_attendance()

def search_attendance(event=None):
    keyword = entry_search.get().strip().lower()
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM attendance ORDER BY id DESC")
    rows = cursor.fetchall()

    filtered = [r for r in rows if keyword in r[1].lower()] if keyword else rows

    for i, row in enumerate(filtered):
        tag = "odd" if i % 2 == 0 else "even"
        tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]), tags=(tag,))

    lbl_count.config(text=f"Total Records: {len(filtered)}")

# ── Main Window ──────────────────────────────────────────────
root = tk.Tk()
root.title("🌸 Attendance Tracker")
root.configure(bg=BG)
root.state("zoomed")          # Full window on launch
root.minsize(700, 500)        # Minimum resizable size

# ── Title Bar ────────────────────────────────────────────────
frame_title = tk.Frame(root, bg=PRIMARY, pady=18)
frame_title.pack(fill="x")

tk.Label(
    frame_title, text="🌸  Attendance Tracker  🌸",
    font=FONT_TITLE, bg=PRIMARY, fg=TEXT_LIGHT
).pack()

# ── Input Card ───────────────────────────────────────────────
frame_card = tk.Frame(root, bg=CARD_BG, padx=30, pady=20,
                      relief="flat", bd=0)
frame_card.pack(fill="x", padx=40, pady=(20, 10))

# Row 1: Name input
row1 = tk.Frame(frame_card, bg=CARD_BG)
row1.pack(fill="x", pady=5)

tk.Label(row1, text="👤  Name:", font=FONT_LABEL,
         bg=CARD_BG, fg=TEXT_DARK, width=12, anchor="w").pack(side="left")

entry_name = tk.Entry(row1, font=FONT_ENTRY, bg=TEXT_LIGHT,
                      fg=TEXT_DARK, relief="flat", bd=2,
                      insertbackground=PRIMARY)
entry_name.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 10))
entry_name.bind("<Return>", lambda e: mark_attendance())

btn_mark = tk.Button(
    row1, text="✅  Mark Present",
    font=FONT_BTN, bg=PRIMARY, fg=TEXT_LIGHT,
    relief="flat", padx=16, pady=6, cursor="hand2",
    activebackground=ACCENT, activeforeground=TEXT_LIGHT,
    command=mark_attendance
)
btn_mark.pack(side="left")

# Row 2: Search input
row2 = tk.Frame(frame_card, bg=CARD_BG)
row2.pack(fill="x", pady=5)

tk.Label(row2, text="🔍  Search:", font=FONT_LABEL,
         bg=CARD_BG, fg=TEXT_DARK, width=12, anchor="w").pack(side="left")

entry_search = tk.Entry(row2, font=FONT_ENTRY, bg=TEXT_LIGHT,
                        fg=TEXT_DARK, relief="flat", bd=2,
                        insertbackground=PRIMARY)
entry_search.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 10))
entry_search.bind("<KeyRelease>", search_attendance)

btn_del = tk.Button(
    row2, text="🗑  Delete Selected",
    font=FONT_BTN, bg=SECONDARY, fg=TEXT_DARK,
    relief="flat", padx=16, pady=6, cursor="hand2",
    activebackground=ACCENT, activeforeground=TEXT_LIGHT,
    command=delete_selected
)
btn_del.pack(side="left")

# ── Table ────────────────────────────────────────────────────
frame_table = tk.Frame(root, bg=BG, padx=40)
frame_table.pack(fill="both", expand=True, pady=(0, 10))

# Treeview style
style = ttk.Style()
style.theme_use("clam")

style.configure("Pink.Treeview",
    background=ROW_ODD, foreground=TEXT_DARK,
    fieldbackground=ROW_ODD, font=FONT_TABLE, rowheight=30)

style.configure("Pink.Treeview.Heading",
    background=PRIMARY, foreground=TEXT_LIGHT,
    font=("Georgia", 11, "bold"), relief="flat")

style.map("Pink.Treeview",
    background=[("selected", ACCENT)],
    foreground=[("selected", TEXT_LIGHT)])

cols = ("ID", "Name", "Date", "Time")
tree = ttk.Treeview(frame_table, columns=cols, show="headings",
                    style="Pink.Treeview")

for col in cols:
    tree.heading(col, text=col)

tree.column("ID",   width=60,  anchor="center")
tree.column("Name", width=250, anchor="w")
tree.column("Date", width=150, anchor="center")
tree.column("Time", width=120, anchor="center")

tree.tag_configure("odd",  background=ROW_ODD)
tree.tag_configure("even", background=ROW_EVEN)

# Scrollbar
scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ── Footer ───────────────────────────────────────────────────
frame_footer = tk.Frame(root, bg=PRIMARY, pady=8)
frame_footer.pack(fill="x", side="bottom")

lbl_count = tk.Label(frame_footer, text="Total Records: 0",
                     font=("Georgia", 10, "bold"),
                     bg=PRIMARY, fg=TEXT_LIGHT)
lbl_count.pack(side="left", padx=20)

tk.Label(frame_footer, text="🌸 Attendance Tracker © 2025",
         font=("Georgia", 10, "bold"),
         bg=PRIMARY, fg=TEXT_LIGHT).pack(side="right", padx=20)

# ── Initial Load ─────────────────────────────────────────────
view_attendance()
root.mainloop()