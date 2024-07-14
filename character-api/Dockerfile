FROM python:3.12.4

RUN pip3 install pipenv

WORKDIR /usr/src/app

ENV PROJECT_DIR /app

COPY . /${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy 

EXPOSE 5000

CMD ["gunicorn", "--graceful-timeout", "5", "--chdir", ".", "app:create_app()",  "-w", "1", "-b", "0.0.0.0:5000"]