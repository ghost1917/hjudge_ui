import argh
import logging
from utils import load_config


@argh.arg('config', type=load_config, help='location of YAML config file')
@argh.arg('port', type=int, help='port to run at')
def run(config, port):
    """
    Run a web server with UI and API
    """
    logging.getLogger().setLevel(logging.DEBUG)

    app = config.application.create()
    app.run('0.0.0.0', port, False, threaded=True)


@argh.arg('--config', type=str, help='location of YAML config file')
def check_config(config="files/config.yml"):
    conf = load_config(config)
    print "==============================="
    print "Config was loaded successfully:"
    for k,v in conf.items():
        print "    {}: {}".format(k, str(v))


def main():
    argh.dispatch_commands([run, check_config])

if __name__ == '__main__':
    main()
