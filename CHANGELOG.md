The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

ToDo:
 - cursor configuring
 - overwrite winfo methods
 - set icon (self.call("wm", "iconphoto", self._w, tkinter.PhotoImage(file="test_images/CustomTkinter_logo_single.png")))
 - add option to change label position for checkbox, switch, radiobutton #628

### Added
 - Mostly bug fixes
 - Added CTkScrollableFrame
 - Added CTkTextbox with automatic x and y scrollbars, corner_radius, border_width, border_spacing
 - Added CTkSegmentedButton
 - Added CTkTabview
 - Added .cget() method to all widgets and windows
 - Added .bind() and .focus() methods to almost all widgets
 - Added 'anchor' option to CTkButton to position image and text inside the button
 - Added 'anchor' option to CTkOptionMenu and 'justify' option to CTkComboBox
 - Added CTkFont class
 - Added CTkImage class to replace PIL.ImageTk.PhotoImage, supports scaling and two images for appearance mode, supports configuring
 - Added missing configure options for multiple widgets

### Changed
 - Changed value for transparent colors (same as background) from None to 'transparent'
 - Changed 'text_font' attribute to 'font' in all widgets, changed 'dropdown_text_font' to 'dropdown_font'
 - Changed 'dropdown_color' attribute to 'dropdown_fg_color' for combobox, optionmenu
 - Changed 'orient' attribute of CTkProgressBar and CTkSlider to 'orientation'
 - Width and height attributes of CTkCheckBox, CTkRadioButton, CTkSwitch now describe the outer dimensions of the whole widget. The button/switch size is described by separate attributes like checkbox_width, checkbox_height
 - font attribute must be tuple or CTkFont now, all size values are measured in pixel now
 - Changed dictionary key 'window_bg_color' to 'window' in theme files
 - CTkInputDialog attributes completely changed
 - CTkScrollbar attributes scrollbar_color, scrollbar_hover_color changed to button_color, button_hover_color

### Removed
 - Removed setter and getter functions like set_text in CTkButton
 - Removed bg and background attribute from CTk and CTkToplevel, always use fg_color
 - Removed Settings class and moved settings to widget and window classes
 - removed customtkinter.set_spacing_scaling(), now set_widget_scaling() is used for spacing too

### Changed
 - Changed custom dropdown menu to normal tkinter.Menu because of multiple platform specific bugs

### Added 
- CTkProgressBar indeterminate mode, automatic progress loop with .start() and .stop()
 - CTkScrollbar (vertical, horizontal)
 - Added CTkComboBox
 - Small fixes for new dropdown menu
 - CTkOptionMenu with custom dropdown menu
 - Support for clicking on labels of CTkCheckBox, CTkRadioButton, CTkSwitch
 - Configure width and height for frame, button, label, progressbar, slider, entry
 - This changelog file
 - Adopted semantic versioning
 - Added HighDPI scaling to all widgets and geometry managers (place, pack, grid)
 - Restructured CTkSettings and renamed a few manager classes
 - Orientation attribute for slider and progressbar