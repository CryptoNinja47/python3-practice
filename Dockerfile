# docker build -t python-3 .
# docker run -it --rm --name my-python-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python test.py
FROM python:3
WORKDIR /usr/src/app
