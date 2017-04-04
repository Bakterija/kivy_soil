from kivy.core.window import Window
from kivy.logger import Logger

keybinds = {}
ctrl_held = False
alt_held = False
shift_held = False
log_keys = False

def add(name, key, state, callback, modifier=None):
    keybinds[name] = {
        'callback': callback,
        'key': int(key),
        'state': state,
        'modifier': modifier
    }

def remove(name):
    del keybinds[name]

def on_key_down(win, key, *args):
    global ctrl_held, alt_held, shift_held
    try:
        modifier = args[2]
    except:
        modifier = []

    if key in (308, 1073741824):
        alt_held = True
    elif key in (305, 306):
        ctrl_held = True
    elif key in (304, 303):
        shift_held = True

    if log_keys:
        Logger.info('KeyBinder: on_key_down: {} - {}'.format(key, modifier))

    for k, v in keybinds.items():
        if v['key'] == key:
            if v['state'] in ('down', 'any', 'all'):
                if not v['modifier'] or v['modifier'] == modifier:
                    v['callback']()

def on_key_up(win, key, *args):
    global ctrl_held, alt_held, shift_held
    if log_keys:
        Logger.info('KeyBinder: on_key___up: {} - {}'.format(key, args))

    if key in (308, 1073741824):
        alt_held = False
    elif key in (305, 306):
        ctrl_held = False
    elif key in (304, 303):
        shift_held = False

    for k, v in keybinds.items():
        if v['key'] == key:
            if v['state'] in ('up', 'any', 'all'):
                v['callback']()


Window.bind(on_key_down=on_key_down)
Window.bind(on_key_up=on_key_up)
Logger.info('key_binder: initialised')
