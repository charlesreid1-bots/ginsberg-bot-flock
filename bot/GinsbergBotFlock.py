import rainbowmindmachine as rmm
import os, glob
import logging

ch = logging.StreamHandler()
logger = logging.getLogger('')
logger.setLevel(logging.INFO)
logger.addHandler(ch)


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATADIR = os.path.join(BASEDIR, 'data')
KEYSDIR = os.path.join(BASEDIR, 'keys')
LOGNAME = 'ginsberg.log'
LOGDIR = BASEDIR
LIVE = True


fh = logging.FileHandler(filename=os.path.join(LOGDIR, LOGNAME))
fh.setLevel(logging.INFO)
logger.addHandler(fh)


def main():
    keys_exists = os.path.isdir(KEYSDIR)
    keys_has_keys = len(glob.glob(os.path.join(KEYSDIR, "*.json"))) > 0
    if( keys_exists and keys_has_keys ):
        print("running bot")
        run()
    else:
        print("setting up bot")
        setup()


def setup():
    k = rmm.TxtKeymaker()
    k.set_apikeys_file(os.path.join(BASEDIR, 'apikeys.json'))
    k.make_keys(DATADIR, KEYSDIR)


def run():
    sh = rmm.TwitterShepherd(
            KEYSDIR, 
            flock_name = 'ginsberg',
            sheep_class = rmm.PoemSheep
    )

    if not LIVE:
        sh.perform_parallel_action(
                'tweet',
                **{
                    'publish' : False,
                    'inner_sleep' : 1,
                    'outer_sleep' : 1,
                    'lines_length' : 4
                }
        )
    else:
        sh.perform_parallel_action(
                'tweet',
                **{
                    'publish' : True,
                    'inner_sleep' : 3*60,
                    'outer_sleep' : 2*3600,
                    'lines_length' : 4
                }
        )


if __name__=="__main__":
    main()
