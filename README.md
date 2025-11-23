# AI Voice Assistant - How to Run

This guide explains how to run the AI Voice Assistant project locally.

## **1. Clone or Download the Project**

Clone the GitHub repository or download the project folder.

git clone <your-repo-url>

cd ai-voice-assistant

2. Navigate to Backend Folder
cd backend

3. Create a Python Virtual Environment:
py -3.13 -m venv venv

4. Activate the Virtual Environment:
Windows PowerShell:

powershell:
.\venv\Scripts\Activate.ps1
Linux / Mac:

source venv/bin/activate

5. Install Dependencies:
pip install -r requirements.txt

6. Run the Backend Server:
uvicorn main:app --reload --port 8000

Backend will run at: http://127.0.0.1:8000

API docs (Swagger UI): http://127.0.0.1:8000/docs

7. Open Frontend
Open frontend/index.html in a browser.

Click the Check Balance button to see the balance for account 1001.

Other API endpoints (transactions, transfer) can be tested via Swagger UI or by adding buttons in the frontend.



