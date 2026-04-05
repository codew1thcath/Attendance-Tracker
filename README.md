🌸 Attendance Tracker

A lightweight, desktop-based **Attendance Tracking System** built with Python and Tkinter — featuring a pink-themed UI, real-time search, SQLite database storage, and a clean table view.

---

📸 Preview

> A full-window pink-themed desktop app with a live search bar, attendance table, and one-click record management.

---

✨ Features

- ✅ **Mark Attendance** — Enter a name and log attendance with auto-stamped date & time
- 🔍 **Live Search** — Filter records in real-time as you type
- 🗑️ **Delete Records** — Select and remove any attendance entry
- 📊 **Table View** — Clean, alternating-row table with sortable columns
- 💾 **Persistent Storage** — All data saved locally via SQLite (`attendance.db`)
- ⌨️ **Keyboard Shortcut** — Press `Enter` to quickly mark attendance
- 🖥️ **Full Window** — Launches maximized, fully resizable
- 🌸 **Pink Theme** — Custom pink color palette with bold Georgia & Courier New fonts

---

🛠️ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Language    | Python 3.x              |
| GUI         | Tkinter + ttk           |
| Database    | SQLite3 (built-in)      |
| Date/Time   | `datetime` (built-in)   |

> ✅ No external libraries required — runs on any machine with Python 3 installed.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional pip installs needed

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/attendance-tracker.git

# 2. Navigate to the project folder
cd attendance-tracker

# 3. Run the app
python attendance_tracker.py
```

> On first launch, `attendance.db` will be automatically created in the same directory.

---

📁 Project Structure

```
attendance-tracker/
│
├── attendance_tracker.py   # Main application file
├── attendance.db           # SQLite database (auto-generated)
└── README.md               # Project documentation
```

---

🗄️ Database Schema

**Table:** `attendance`

| Column | Type    | Description                  |
|--------|---------|------------------------------|
| `id`   | INTEGER | Auto-incremented primary key |
| `name` | TEXT    | Name of the attendee         |
| `date` | TEXT    | Date in `YYYY-MM-DD` format  |
| `time` | TEXT    | Time in `HH:MM:SS` format    |

---

🎮 How to Use

| Action              | How                                         |
|---------------------|---------------------------------------------|
| Mark attendance     | Type a name → click **✅ Mark Present** or press `Enter` |
| Search records      | Type in the 🔍 Search bar — filters live    |
| Delete a record     | Click a row to select → click **🗑 Delete Selected** |
| Refresh the list    | Automatically refreshes after every action  |

---

🎨 UI Theme

| Element         | Color          |
|-----------------|----------------|
| Background      | `#FFF0F5` — Lavender Blush |
| Primary (Header/Buttons) | `#E91E8C` — Hot Pink |
| Card Background | `#FFD6E7` — Soft Pink |
| Accent          | `#FF1493` — Deep Pink |
| Text            | `#3D0026` — Dark Maroon |
| Fonts           | Georgia (UI), Courier New (data) — both **bold** |

---

🔮 Possible Future Improvements

- [ ] Export attendance records to CSV or Excel
- [ ] Add face recognition check-in (via `deepface` or `mediapipe`)
- [ ] Login system for admin access
- [ ] Filter by date range
- [ ] Print / generate PDF reports
- [ ] Add student/employee ID support

---

📄 License

This project is open source and available under the [MIT License](LICENSE).
