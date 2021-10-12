# portfolio

## How to run it?
First of all, you need to collect all your staticfiles in the root directory:
```
python3 manage.py collectstatic
```
You can run it outside and in a Docker container. To run with no Docker, type `python3 manage.py runserver`. And if you want to run it in Docker, type:
```
docker build -t <containername> .
```
```
docker run --rm --name portfolio -e "PORT=8765" -p 8765:8007 containername
```