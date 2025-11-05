🌾 Agribot-AI: An Intelligent Agricultural Assistant

This repository contains the complete project for Agribot-AI, a web-based chatbot built with Python and Flask. The application provides farmers with advice on fertilizers, pests, and weather, and includes secure user authentication and a multilingual interface.

The project is structured as a series of tasks, with each folder representing a progressive stage of development, from a basic login system to a final, integrated chatbot.

✨ Task 04

Core Features

🔐 Secure Dual-Role Authentication: Separate, secure portals for Users (farmers) and Admins.

🔑 Admin Dashboard: A special view for admins to see all registered users in the database.

💬 Intelligent Chatbot: Answers common farming questions about pests, fertilizers, and weather.

🌐 Multilingual Support: The chatbot can detect and respond in multiple languages (e.g., Tamil, English).

🔒 Password Hashing: Uses Flask-Bcrypt to ensure no plain-text passwords are ever stored.

🧰 Technology Stack

Backend: Python, Flask

Database: SQLite (managed with Flask-SQLAlchemy)

Security: Flask-Bcrypt (for password hashing)

Frontend: HTML, CSS, JavaScript

📂 Repository Structure

This repository is organized by task. We recommend running Task04_Agribot as it is the complete, final version.

agribot-ai/

├── Task01_agribot_login_page/

The foundational user authentication system.

Features: User Registration, User Login, Admin Login, and Admin Dashboard.

├── Task02_Simple_Agribot/

A simple, keyword-based chatbot integrated with the Task 01 login system.

├── Task03_multiLanguage/

An evolution of the chatbot, adding multilingual support to handle and respond in different languages.

├── Task04_Agribot/

The final, polished application. This folder contains the complete, integrated, and styled version of the Agribot with all features combined.

🚀 How to Run the Final Application (Task 04)

These instructions are for running the final, complete project.

1. Clone the repository:

git clone [https://github.com/Pavanid2325/agribot-ai.git](https://github.com/Pavanid2325/agribot-ai.git)
cd agribot-ai


2. Navigate to the final project folder:
Based on your project structure, the main file is inside a subfolder.

cd Task04_Agribot/agribot


3. Create a virtual environment & activate it:

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate


4. Install the required dependencies:

pip install Flask Flask-SQLAlchemy Flask-Bcrypt
# (You may need to install other libraries like 'deep_translator' if you used one for Task 3)


5. Run the application:
This will start the web server and create the database.db file if it doesn't exist.

python app.py


6. Open in your browser:
Navigate to: http://127.0.0.1:5000

Default Admin Login

A default admin account is created automatically on the first run:

Username: admin

Password: admin123