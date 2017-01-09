from girder_worker.app import app
import time

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
