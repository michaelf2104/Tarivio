# Dockerfile
FROM python:3.11

# Working directory in container
WORKDIR /app

# copy requirements
COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy src code
COPY ./app /app/app

# port
EXPOSE 8000

# start FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]