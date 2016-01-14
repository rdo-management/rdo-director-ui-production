from __future__ import unicode_literals

import os
import sys

from flask import Flask, render_template, send_from_directory
from oslo_config import cfg, types
from oslo_log import log


LOG = log.getLogger(__name__)

PortType = types.Integer(1, 65535)

DIST_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..', 'dist')

# App options
cfg.CONF.register_group(cfg.OptGroup(name='service',
                                     title='Service options'))
cfg.CONF.register_opts([cfg.StrOpt('bind_host',
                                   default='0.0.0.0',
                                   help='App host address'),
                        cfg.Opt('bind_port',
                                default=8888,
                                type=PortType,
                                help='App port'),
                        cfg.BoolOpt('debug',
                                    default=False)],
                       group='service')

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def index(path):
    return render_template('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js/', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(app.static_folder + '/img', path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory(app.static_folder + '/fonts', path)


def main(args=sys.argv[1:]):
    cfg.CONF(args)
    app.run(host=cfg.CONF.service.bind_host,
            port=cfg.CONF.service.bind_port,
            debug=cfg.CONF.service.debug)


if __name__ == '__main__':
    main()
