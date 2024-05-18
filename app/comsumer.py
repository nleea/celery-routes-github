from celery import Celery

app = Celery("scheduler", broker="redis://broker:6379/0")


@app.task(name="add")
def add(x, y):
    return x + y


@app.task(name="sub")
def sub(x, y):
    return x - y
