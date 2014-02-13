import os
import glob
import argparse

from .helpers import ext, exit


def setup_parser():
    p = argparse.ArgumentParser(
        description='Juju plugin to manage juju plugins!')
    p.add_argument('subcommand', nargs='?',
                   help='subcommand to run')
    p.add_argument('description', action='store_true', default=False,
                   help='print a short description')

    return p


def subcommands():
    subs = []
    for path in os.environ['PATH'].split(os.pathsep):
        path = path.strip('"')
        for cmd in glob.glob(os.path.join(path, 'juju-plugin-*%s' % ext())):
            sub = os.path.basename(cmd)
            sub = sub.split('juju-plugin-')[1].replace(ext(), '')
            subs.append(sub)

    return sorted(set(subs))


def main(args=None):
    """Will parse args, if present, then execute subcommand if exists"""
    cmds = subcommands()
    p = setup_parser()
    args = p.parse_args(args)
    if args.description:
        exit(msg=p.description)
    if args.subcommand not in cmds:
        exit(1, msg='Subcommand not found')
