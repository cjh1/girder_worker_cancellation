from girder_worker import GirderWorkerPluginABC
class GWExamplePlugin(GirderWorkerPluginABC):
    def __init__(self, app, *args, **kwargs):
        pass

    def task_imports(self):
        return ['gwcancellation.tasks']
