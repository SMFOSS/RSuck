from monkeylib import rrsync_remote
from path import path
import execnet
import execnet.rsync
import execnet.rsync_remote
import optparse
import sys


class RRSync(execnet.rsync.RSync):
    """
    Remote rsync
    """
    def add_target(self, channel, destdir, finishedcallback=None, **options):
        for name in options:
            assert name in ('delete',)
        def itemcallback(req):
            self._receivequeue.put((channel, req))
        channel.setcallback(itemcallback, endmarker = None)
        channel.send((str(destdir), options))
        self._channels[channel] = finishedcallback

    @staticmethod
    def parse_options(argv=None, usage="usage: %prog [options] remotesrc [localdest]"):
        parser = optparse.OptionParser(usage=usage)

        parser.add_option('-x', '--xspec',
                          help='Connection specification',
                          dest='xspec',
                          #default='ssh=127.0.0.1//id=ssh1/chdir=/tmp/',
                          default="ssh=127.0.0.1//python=/Users/whit/dev/rsuck/bin/python//id=ssh1//chdir=/tmp/" 
                          )

        parser.add_option('-d', '--delete',
                          action="store_true",
                          help='delete files',
                          dest='delete',
                          default=False)
    
        if argv is None:
            argv = sys.argv
        options, args = parser.parse_args(argv)

        howmany = len(args)
        assert howmany  >= 2, "Must at least give a remote src directory as an argument"
        args = [path(x) for x in args]
        if howmany == 3:
            script, localdest, remotesrc = args
        elif howmany == 2:
            script, localdest = path('.')
            remotesrc = args[0]
        return options, localdest, remotesrc


def main(argv=None):
    if not argv:
        argv = sys.argv
    options, remotesrc, localdest = RRSync.parse_options(argv)
    roptions = options.delete and dict(delete=True) or {}
    gw = execnet.makegateway(options.xspec)
    channel = gw.remote_exec(rrsync_remote)
    channel.send((str(remotesrc), str(localdest), roptions))
    execnet.rsync_remote.serve_rsync(channel)
    print "<< Done >>"





