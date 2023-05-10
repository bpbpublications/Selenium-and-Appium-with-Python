FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "--driver=Remote", "--host=selenium-hub", "--port=4444", "-v", "-s", "-n 2", "Test_Selenium.py"]



