from kivy_soil.kb_system.canvas import FocusBehaviorCanvas
from kivy.uix.modalview import ModalView
from kivy_soil import hover_behavior
from kivy_soil.kb_system import keys
from kivy.uix.popup import Popup
from kivy.lang import Builder


class AppPopup(hover_behavior.HoverBehavior, FocusBehaviorCanvas, Popup):
    '''A special Popup class that integrates with kivy_soil hover_behavior
    and increases hover_behavior.min_hover_height when it is opened'''

    hover_height = 20
    grab_keys = [keys.ESC]

    def __init__(self, **kwargs):
        super(AppPopup, self).__init__(**kwargs)
        self.grab_focus = True

    def open(self):
        hover_behavior.min_hover_height = self.hover_height
        super(AppPopup, self).open()
        self.is_focusable = True

    def dismiss(self):
        hover_behavior.min_hover_height = 0
        super(AppPopup, self).dismiss()
        self.is_focusable = False
