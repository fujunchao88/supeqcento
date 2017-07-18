# -*- coding: utf-8 -*-
import os.path
import site

from argparse import ArgumentParser


def add_scan_path():
    cur_dir = os.path.dirname(__file__)
    site.addsitedir(os.path.abspath(os.path.join(cur_dir, os.pardir)))


def setup_server(args):
    from supeqcento.build import init_supeq
    from sanic import Sanic

    app = Sanic("supeq")
    if args.project == "supeqcento":
        init_supeq(app)

    app.run(host=args.host, port=args.port,
            workers=args.workers, debug=args.debug)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--host', dest='host', type=str, required=True)
    parser.add_argument('--port', dest='port', type=int, required=True)
    help_str = 'multiple processes,by default using only one CPU core'
    parser.add_argument('--workers', dest='workers', type=int,
                        default=1, help=help_str)
    parser.add_argument('--debug', dest='debug', action="store_true")
    choices = ['supeqcento', 'email']
    help_str = 'choose server from (supeqcento|email)'
    parser.add_argument('project', choices=choices, help=help_str)
    ps_args = parser.parse_args()

    add_scan_path()

    setup_server(ps_args)
