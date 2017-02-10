import logging
from utils import load_config


@argh.arg('config', type=load_config, help='location of YAML config file')
@argh.arg('port', type=int, help='port to run at')
def run_server(config, port):
    """
    Run a web server with UI and API
    """
    logging.getLogger().setLevel(logging.DEBUG)

    app = create_app(config)
    app.run('0.0.0.0', port, True, threaded=True)
