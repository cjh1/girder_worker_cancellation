from girder_worker.app import app
import time
from celery.task.control import inspect

CANCELLED = 'CANCELLED'

@app.task(bind=True)
def cancellable(task):

    loop = 0
    status = None
    while loop < 10 and status != CANCELLED:
        status = task.backend.get_status(task.request.id)
        time.sleep(1)
        loop += 1

    if status == CANCELLED:
        print('I was cancelled!')

_inspector = None
def _worker_inspector(task):
  global _inspector
  if _inspector is None:
     _inspector = inspect([task.request.hostname])

  return _inspector

def _revoked_tasks(task):
  return _worker_inspector(task).revoked()[task.request.hostname]

def is_revoked(task):
  return task.request.id in _revoked_tasks(task)

@app.task(bind=True)
def revokable(task):
    loop = 0
    while loop < 10 and not is_revoked(task):
        time.sleep(1)
        loop += 1

    if is_revoked(task):
        print('I was revoked!')
