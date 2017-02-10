from configure import Configuration


def load_config(path):
    return Configuration.from_file(path).configure()
