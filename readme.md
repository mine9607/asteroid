# Setup

1) Create a virtual environment using: `python -m venv venv`
    - '-m' flag ensures using the correct Python interpreter version for the virtual env
    - venv uses the 'venv' module to create a virtual environment
    - venv creates a folder 'venv' where the virtual env will be created

2) Activate the virtual environment: `source venv/bin/activate`

3) Create a requirements.txt file: `nvim requirements.txt`
    - Add pygame dependency: `pygame==2.6.1`

4) Install the requirements: `pip install -r requirements.txt`

