from configure import Configuration


def load_config(path):
    print "Loads config from {}".format(path)
    return Configuration.from_file(path).configure()
