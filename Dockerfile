from python: 3.10-slim

workdir /app

copy . /app

run pip install --no-cache-dir -r requirementes.txt

expose 5000

cmd ["python", "app.py"]
