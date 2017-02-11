import argh
import logging
from configure import Configuration


@argh.arg('config', type=str, help='location of YAML config file')
@argh.arg('port', type=int, help='port to run at')
def run(config, port):
    """
    Run a web server with UI and API
    """
    logging.getLogger().setLevel(logging.DEBUG)
    config = Configuration.from_file(config).configure()
    config.application.run(port)


def main():
    argh.dispatch_command(run)

if __name__ == '__main__':
    main()
