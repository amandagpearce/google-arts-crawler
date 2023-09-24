# selecting the python version
FROM python:3.8-slim
# exposing the port where the app will run
EXPOSE 9000

COPY requirements.txt .
# install requirements
RUN pip install -r docker_requirements.txt
# copy everything (first .) to the directory we are at (second .)
COPY . .
# say what commands will run the container
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "9000"]

## flask run --host 0.0.0.0 --port 9000
