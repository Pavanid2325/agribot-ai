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

