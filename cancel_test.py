from gwcancellation.tasks import cancellable, CANCELLED
import time

if __name__ == '__main__':
    async_result = cancellable.delay()
    time.sleep(3)
    async_result.backend.store_result(async_result.id, None, CANCELLED)


