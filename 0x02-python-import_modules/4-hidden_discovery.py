#!/usr/bin/python3
if __name__ == "__main__":
    """prints all the names defined by the compiled
    module hidden_4.pyc"""
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] not in ("__"):
            print("{}".format(name))
