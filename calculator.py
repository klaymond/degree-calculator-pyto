# Created with Pyto

import pyto_ui as ui


# Function that will run when converting from Fahrenheit to Celsius
def fahrenheit_to_celsius(sender):
    field_view = sender.superview.subview_with_name("input")
    label_view = sender.superview.subview_with_name("label")
    f = float(field_view.text)
    c = (f - 32) / 1.8
    label_view.text = str(c) + " C"
    
# Function that will run when converting from Celsius to Fahrenheit
def celsius_to_fahrenheit(sender):
    field_view = sender.superview.subview_with_name("input")
    label_view = sender.superview.subview_with_name("label")
    c = float(field_view.text)
    f = c * 1.8 + 32
    label_view.text = str(f) + " F"
    

# Main view where all other components are placed
view = ui.View()
view.background_color = ui.COLOR_SYSTEM_BACKGROUND

# Text input
text = ui.TextField()
text.size = (250, 50)
text.center = (view.width/2, view.height/2-250)
text.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
text.name = "input"
view.add_subview(text)

# Button to convert Celsius to Farenheit
button_ctof = ui.Button(title="Convert C to F")
button_ctof.size = (100, 50)
button_ctof.center = (view.width/2, view.height/2-150)
button_ctof.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
button_ctof.action = celsius_to_fahrenheit
view.add_subview(button_ctof)

# Button to convert Farenheit to Celsius
button_ftoc = ui.Button(title="Convert F to C")
button_ftoc.size = (100, 50)
button_ftoc.center = (view.width/2, view.height/2-100)
button_ftoc.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
button_ftoc.action = fahrenheit_to_celsius
view.add_subview(button_ftoc)

# Label where result will be displayed
label = ui.Label()
label.text = "Waiting for input..."
label.size = (250, 50)
label.center = (view.width/2, view.height/2-50)
label.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
label.name = "label"
view.add_subview(label)



ui.show_view(view, ui.PRESENTATION_MODE_SHEET)
print("Thanks for using my app :)")
