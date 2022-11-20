from contextlib import contextmanager


class Resource:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f"Resource was opened with arguments {args}")
        self.opened = True

    def close(self):
        print(f"Resource was closed!")
        self.opened = False

    def __del__(self):
        if self.opened:
            print("Memory leak detected! Resource was not closed")

    def action(self):
        print("Do something with resource")


@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource
    except:
        raise
    finally:
        if resource:
            resource.close()


class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()


if __name__ == '__main__':
    # resource = None
    # try:
    #     resource = Resource()
    #     resource.open(1, 2, 3)
    #     resource.action()
    #     raise  ValueError()
    # except:
    #     raise
    # finally:
    #     if resource:
    #         resource.close()

    # with open_resource(1, 2, 3) as res:
    #     res.action()
    #     raise ValueError("Stop")

    with ResourceWorker(1, 2, 3) as res:
        res.action()
        raise ValueError()
