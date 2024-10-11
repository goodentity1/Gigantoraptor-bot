# Only run this once when you have downloaded the python repo
py -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


# Entire the environment
& ".\.venv\Scripts\Activate.ps1"

# Change directory to the server-scanner dir
# Set-Location -Path ".\server-scanner"

# Start a new instance of PowerShell and run the Python script
Start-Process powershell -ArgumentList "-NoExit -Command py '.\main.py'"