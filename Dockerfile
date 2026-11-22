FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "test", "--alluredir=allure_results", "--selenoid-uri=http://selenoid:4444/wd/hub"]
