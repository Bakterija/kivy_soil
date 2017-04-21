from kivy.properties import BooleanProperty
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
<AppFocusBehavior>:
    canvas.after:
        Color:
            rgba: (.2, 1.0, 0.2, 1) if self.focus else (0.4, 0.4, 1, 0)
        Line:
            points: self.x, self.y, self.x, self.top, self.right, self.top, self.right, self.y, self.x, self.y
            # width: 2
''')

focusable_widgets = []
current_focus = None

def on_parent(self, parent):
    global focusable_widgets
    if parent:
        focusable_widgets.append(self)
    else:
        focusable_widgets.remove(self)

def focus_next():
    len_focusable_widgets = len(focusable_widgets)
    found = False
    for i, widget in enumerate(focusable_widgets):
        if widget.focus:
            widget.focus = False
            found = True
            if len_focusable_widgets - 1 > i:
                set_focus(focusable_widgets[i+1])
            else:
                set_focus(focusable_widgets[0])
            break

    if not found:
        set_focus(focusable_widgets[0])

def remove_focus():
    global current_focus
    current_focus.focus = False
    current_focus = None

def set_focus(widget):
    global current_focus
    widget.focus = True
    current_focus = widget

class AppFocusBehavior(Widget):
    focus = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(AppFocusBehavior, self).__init__(**kwargs)
        self.bind(parent=on_parent)

