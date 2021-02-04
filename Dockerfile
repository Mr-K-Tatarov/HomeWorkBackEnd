FROM python:3.8

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD sh -c "alembic upgrade head && python main.py"

EXPOSE 8000
