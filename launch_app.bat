@echo off
cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Streamlit app...
streamlit run new_app.py

pause
