from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.logger import Logger
from kivy.compat import string_types
from kivy.factory import Factory


class DataView(object):

    def refresh_view_attrs(self, rv, index, data):
        '''Attributes are set from data dict keys and values'''
        for k, v in data.iteritems():
            setattr(self, k, v)


class DataBox(BoxLayout):
    data = ListProperty()
    '''The data used by DataBox. This is a list of dicts whose
    keys map to the corresponding property names of the viewclass
    '''

    viewclass = StringProperty()
    '''
    The viewclass that will be generated from each data dict
    '''

    viewclass_class = None

    def __init__(self, **kwargs):
        super(DataBox, self).__init__(**kwargs)

    def on_data(self, instance, value):
        if self.viewclass_class:
            children_count = len(self.children)
            value_count = len(value)
            if children_count != value_count:
                if children_count < value_count:
                    for count in range(0, value_count - children_count):
                        self.add_widget(self.viewclass_class())
                else:
                    for count in range(0, children_count - value_count):
                        self.remove_widget(self.children[-1])

            if self.children:
                for i, widget_dict in enumerate(value):
                    self.children[i].refresh_view_attrs(self, i, widget_dict)

    def on_viewclass(self, instance, value):
        if isinstance(value, string_types):
            self.viewclass_class = getattr(Factory, value)
            self.on_data(None, self.data)
        else:
            Logger.error(
                "{}: on_viewclass: {} is not an instance".format(self, e))

    def refresh_from_data(self, *args):
        self.on_data(None, self.data)
