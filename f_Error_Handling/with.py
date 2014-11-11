class Repository(object):

    def __init__(self):
        print("  creating repository ...")

    def __enter__(self):
        print("  entering cleanup block ...")
        return self # return object with __exit__

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  leaving cleanup block ...")

def cleanup_method():
    with Repository() as repository:
        print("work with repository")
        raise TypeError("test")

cleanup_method()