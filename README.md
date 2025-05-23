# UniApp - University Enrollment System

| Team Member | Student ID |
|-------------|------------|
| Praveer jain | 25947209 |
| Ruben Easo Thomas | 25598184 |
| Jinkyung Kim | 14657314 |
| Harshit Soni  | 25652177 |

A comprehensive Python-based interactive university enrollment system with both command-line and graphical interfaces:

- *CLIUniApp*: Command-line interface for Student and Admin subsystems handling the entire Uni App
- *GUIUniApp*: Tkinter GUI for student login, enrollment, and subject display for each student

## ✨ Features at a Glance

- *User Authentication*: Secure login/registration with validation
- *Student Management*: 
  - Enrollment in up to 4 subjects (with randomly generated marks)
  - Password management with security validation
  - Subject viewing and removal capabilities
- *Admin Functions*: 
  - Student listing and management
  - Grade-based grouping and analysis
  - Pass/fail partitioning
- *Data Persistence*: JSON-based storage system
- *MGUI*: Interface with Student dashboard 
- *Enhanced CLI*: Enhanced university system through terminal interface

## 📋 Requirements

- Python 3.12.0 (tested on 3.12.0)
- No external packages required beyond the standard library

## 🚀 Installation & Running

1. Clone or unzip the project folder.
2. (Optional) Create and activate a virtual environment:
   
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   
3. Run the application in either mode:
   bash
   # Command-line interface:
   python main_cli.py
   
   # Graphical interface:
   python GUIUniApp/main_gui.py 
   

## 📁 Project Structure


university_app/
├── cli/
│   ├── controllers/
│   │   ├── student_controller.py
│   │   ├── admin_controller.py
│   │   └── university_controller.py
│   ├── views/
│   │   ├── student_view.py
│   │   ├── admin_view.py
│   │   └── university_view.py
│   └── main.py
├── gui/
│   ├── views/
│   │   ├── login_view.py
│   │   ├── enrollment_view.py
│   │   ├── subject_view.py
│   │   └── exception_view.py
│   ├── controllers/
│   │   └── gui_controller.py
│   └── main.py
├── models/
│   ├── student.py
│   ├── subject.py
│   └── database.py
├── utils/
│   ├── validators.py
│   └── id_generator.py
├── data/
│   └── students.data
└── README.md



## 🎯 CLI Usage

From the project root:

bash
# Launch the CLI application:
python main_cli.py


### University System Menu
- *Admin (A)*: Access admin functions
- *Student (S)*: Access student functions
- *Exit (X)*: Exit application

### Student System
- *login (l)*: Enter email and password to authenticate
- *register (r)*: Create new student account (validated)
- *exit (x)*: Return to main menu

### Subject Enrollment System (after login)
- *change password (c)*: Update password with validation
- *enrol (e)*: Add subjects (up to 4, auto-generated)
- *remove (r)*: Remove subject by ID
- *show (s)*: Display enrolled subjects with marks and grades
- *exit (x)*: Logout and save data

### Admin System
- *show (s)*: List all registered students
- *group students (g)*: Group students by grade
- *partition PASS/FAIL (p)*: Divide students by passing status
- *remove student (r)*: Delete student by ID
- *clear database (c)*: Erase all student data
- *exit (x)*: Return to main menu

## 🖥 GUI Usage

bash
# Launch the GUI application:
python main_gui.py 


### Login Window
- Enter registered email and password
- System validates credentials

### Enrollment Window
- *Enrol subject*: Add random subject with mark and grade
- *View subjects*: See list of enrolled subjects
- *Logout*: Save changes and return to login

## ✅ Automated Tests

The project includes comprehensive tests using pytest:

bash
# Run all tests:
pytest

# Run with detailed output:
pytest -v





## 💾 Persistence

All data is stored in JSON format in data/students.data:
- Data is loaded when the application starts
- Changes are saved when students logout or enroll in subjects
- Both CLI and GUI interfaces share the same data file

## 🔐 Validation Rules

- *Email*: Must end with "@university.com"
- *Password*: 
  - Must start with uppercase letter
  - Must contain at least 5 letters
  - Must contain at least 3 digits

## 📌 Technical Notes

- Follows MVC architecture pattern (Models, Views, Controllers)
- GUI implemented with Tkinter with modal dialogs
- Defensive programming with input validation
- Error handling with appropriate user feedback

## Team Contributions

### Ruben Easo Thomas
- *Domain Models*: Implemented Student and Subject classes with proper encapsulation and inheritannce
- *CLI- Login Interface*: Developed the authentication window with validation
- *DataValidations*: Detailed model specifications and validation rules 
- *Data Persistence*: Designed JSON-based database system

### Praveer Jain
- *CLI Interface*: Designed and implemented the command-line interface , Admin model and controller
- *CLI - Enrollment Interface*: Created the Admin enrollment terminal interface
- *User Experience*: Implemented intuitive menu navigation for admin 
- *Documentation*: Detailed model specifications and validation rules

### Jinkyung Kim 
- *GUIControllers*: Developed Student enrollment for GUI interface
- *GUI - Subject Display*: Created the subject visualization window 
- *Modelversion control* : Folder struture design
- *Business Logic*: Implemented core application workflows

### Harshit Soni 
*GUIControllers*: Developed Student enrollment for GUI interface
- *Testing GUIFramework*: Created comprehensive test suite with pytest
- *Utility Functions*: Developed validation and ID generation utilities
- *GUI - Theme System*: Implemented application theming and popup management

## Group Contribution
- *Project Integration*: Ensured consistency across components