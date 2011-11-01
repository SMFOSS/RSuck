def done():
    print "DONE"

if __name__ == '__channelexec__':
    from monkeylib import rrsync
    localdir, destdir, options = channel.receive()
    job = rrsync.RRSync(localdir, callback=None)
    job.add_target(channel,
                   destdir,
                   done, **options)
    job.send()
