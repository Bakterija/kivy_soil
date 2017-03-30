from kivy.core.window import Window
from kivy.logger import Logger


keybinds = {}
log_keys = False


def add(name, key, state, callback, modifier=None):
    keybinds[name] = {
        'callback': callback,
        'key': key,
        'state': state,
        'modifier': modifier
    }

def remove(name):
    del keybinds[name]

def on_key_down(win, key, *args):
    try:
        modifier = args[2]
    except:
        modifier = []

    if log_keys:
        Logger.info('KeyBinder: on_key_down: {} - {}'.format(key, modifier))

    for k, v in keybinds.items():
        if v['key'] == str(key):
            if v['state'] in ('down', 'any', 'all'):
                if not v['modifier'] or v['modifier'] == modifier:
                    v['callback']()

def on_key_up(win, key, *args):
    if log_keys:
        Logger.info('KeyBinder: on_key___up: {} - {}'.format(key, args))

    for k, v in keybinds.items():
        if v['key'] == str(key):
            if v['state'] in ('up', 'any', 'all'):
                v['callback']()


Window.bind(on_key_down=on_key_down)
Window.bind(on_key_up=on_key_up)
Logger.info('key_binder: initialised')
