import rainbowmindmachine as rmm
import os, glob
import logging

ch = logging.StreamHandler()
logger = logging.getLogger('')
logger.setLevel(logging.INFO)
logger.addHandler(ch)

DATADIR = os.path.join(os.getcwd(), 'poems')
KEYSDIR = os.path.join(os.getcwd(), 'keys')

def setup():
    k = rmm.TxtKeymaker()
    k.set_apikeys_file('apikeys.json')
    k.make_keys(DATADIR, KEYSDIR)

def run():
    sh = rmm.TwitterShepherd(
            json_keys_dir = KEYSDIR, 
            flock_name = 'ginsberg',
            sheep_class = rmm.PoemSheep
    )


    LIVE = False


    if not LIVE:
        sh.perform_parallel_action(
                'tweet',
                **{
                    'publish' : False,
                    'offset' : 15,
                    'inner_sleep' : 3,
                    'outer_sleep' : 3
                }
        )
    else:
        sh.perform_parallel_action(
                'tweet',
                **{
                    'publish' : True,
                    'offset' : 15,
                    'inner_sleep' : 5*60,
                    'outer_sleep' : 4*1800
                }
        )


if __name__=="__main__":

    keys_exists = os.path.isdir(KEYSDIR)
    keys_has_keys = len(glob.glob(os.path.join(KEYSDIR,"*.json"))) > 0
    if( keys_exists and keys_has_keys ):
        print("running bot")
        run()
    else:
        print("setting up bot")
        setup()


