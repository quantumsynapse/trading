pip install virtualenv
virtualenv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

git init
echo "venv" > .gitignore
echo "*.pyc" >> .gitignore

pip install ccxt flask
