from gwcancellation.tasks import revokable
import time

if __name__ == '__main__':
    async_result = revokable.delay()
    time.sleep(3)
    async_result.revoke()
     


