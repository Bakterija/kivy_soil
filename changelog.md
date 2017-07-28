# 2.00
Added changelog
Changed AppRecycleBoxLayout.open_context_menu method to return what is returned by context_menu_function
Added AppRecycleView on_key_down method with default keys for scrolling and selecting with keyboard that integrate with kivy_soil kb_system
Added AppRecycleView warning when default_height and data dict height is not set
Added modified kivy_md menu widgets with kb_system focus behavior compatability
Fixed FocusBehavior grabbing focus when is_focusable is set to False
Added FocusBehavior.focus_previous method
