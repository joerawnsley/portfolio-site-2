FROM python:3.14.1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3","./portfolio_site_2/portfolio_site_2.py"]

EXPOSE 8080