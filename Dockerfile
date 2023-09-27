# selecting the python version
FROM python:3.8-slim
EXPOSE 9000
COPY docker_requirements.txt .
RUN pip install --no-cache-dir -r docker_requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "9000"]
