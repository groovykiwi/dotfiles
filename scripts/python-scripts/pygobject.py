#!/usr/bin/env python


import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class myWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Wraith Prism RGB")
        self.set_border_width(10)


        #Grid 
        grid = Gtk.Grid()
        grid.set_row_spacing(20)
        self.add(grid)

        #Stack
        component = Gtk.Stack()
        component.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        component.set_transition_duration(500)



        ########LOGO########
        logo_grid = Gtk.Grid()
        logo_grid.set_row_spacing(20)
        logo_grid.set_column_spacing(20)
        component.add_titled(logo_grid, "logo_grid", "Logo")

        #Mode Select
        logo_label  = Gtk.Label(label="Mode: ")
        logo_grid.attach(logo_label, 0,0,1,1)

        modes = Gtk.ListStore(str)
        modes.append(["Static"])
        modes.append(["Breathing"])

        logo_mode = Gtk.ComboBox().new_with_model(modes)
        logo_mode.set_active(0)
        renderer_text = Gtk.CellRendererText()
        logo_mode.pack_start(renderer_text, True)
        logo_mode.add_attribute(renderer_text, "text", 0)
        logo_grid.attach(logo_mode, 1,0,1,1)
        
        #Color Picker
        logo_clabel = Gtk.Label(label="Color: ")
        logo_grid.attach(logo_clabel, 0,1,1,1)
        logo_color = Gtk.ColorButton()
        logo_grid.attach(logo_color, 1,1,1,1)


        #Brightness

        logo_blabel = Gtk.Label(label="Brightness: ")
        logo_grid.attach(logo_blabel, 0,2,1,1)

        bright_value = Gtk.Adjustment(0, 0, 5, 1, 1, 0)
        logo_bright = Gtk.SpinButton()
        logo_bright.set_adjustment(bright_value)
        logo_grid.attach(logo_bright, 1,2,1,1)

        #Speed
        global logo_speed
        global logo_slabel

        logo_speed = Gtk.SpinButton()

        def updatespeed(x):

            if logo_mode.get_active() == 1:
                global logo_slabel
                logo_slabel = Gtk.Label(label="Speed: ")
                logo_grid.attach(logo_slabel, 0,3,1,1)

                global logo_speed
                speed_value = Gtk.Adjustment(0, 0, 5, 1, 1, 0)
                logo_speed = Gtk.SpinButton()
                logo_speed.set_adjustment(speed_value)
                logo_grid.attach(logo_speed, 1,3,1,1)

                logo_slabel.show()
                logo_speed.show()

            else:
                logo_speed.hide()
                logo_slabel.hide()


        logo_mode.connect("changed", updatespeed)
        



        ########FAN########

        fan_grid = Gtk.Grid()
        fan_grid.set_row_spacing(20)
        fan_grid.set_column_spacing(20)
        component.add_titled(fan_grid, "fan_grid", "Fan")

        #Mode Select
        fan_label  = Gtk.Label(label="Mode: ")
        fan_grid.attach(fan_label, 0,0,1,1)

        modes = Gtk.ListStore(str)
        modes.append(["Static"])
        modes.append(["Breathing"])

        fan_mode = Gtk.ComboBox().new_with_model(modes)
        fan_mode.set_active(0)
        renderer_text = Gtk.CellRendererText()
        fan_mode.pack_start(renderer_text, True)
        fan_mode.add_attribute(renderer_text, "text", 0)
        fan_grid.attach(fan_mode, 1,0,1,1)
        
        #Color Picker
        fan_clabel = Gtk.Label(label="Color: ")
        fan_grid.attach(fan_clabel, 0,1,1,1)
        fan_color = Gtk.ColorButton()
        fan_grid.attach(fan_color, 1,1,1,1)


        #Brightness

        fan_blabel = Gtk.Label(label="Brightness: ")
        fan_grid.attach(fan_blabel, 0,2,1,1)

        bright_value = Gtk.Adjustment(0, 0, 5, 1, 1, 0)
        fan_bright = Gtk.SpinButton()
        fan_bright.set_adjustment(bright_value)
        fan_grid.attach(fan_bright, 1,2,1,1)

        #Speed
        global fan_speed
        global fan_slabel

        fan_speed = Gtk.SpinButton()

        def updatespeed(x):

            if fan_mode.get_active() == 1:
                global fan_slabel
                fan_slabel = Gtk.Label(label="Speed: ")
                fan_grid.attach(fan_slabel, 0,3,1,1)

                global fan_speed
                speed_value = Gtk.Adjustment(0, 0, 5, 1, 1, 0)
                fan_speed = Gtk.SpinButton()
                fan_speed.set_adjustment(speed_value)
                fan_grid.attach(fan_speed, 1,3,1,1)

                fan_slabel.show()
                fan_speed.show()

            else:
                fan_speed.hide()
                fan_slabel.hide()


        fan_mode.connect("changed", updatespeed)
    




        ########RING########
        ring_grid = Gtk.Grid()
        ring_grid.set_row_spacing(20)
        ring_grid.set_column_spacing(20)
        component.add_titled(ring_grid, "ring_grid", "Ring")

        #Mode Select
        ring_label  = Gtk.Label(label="Mode: ")
        ring_grid.attach(ring_label, 0,0,1,1)

        modes = Gtk.ListStore(str)
        modes.append(["Static"])
        modes.append(["Breathing"])

        ring_mode = Gtk.ComboBox().new_with_model(modes)
        ring_mode.set_active(0)
        renderer_text = Gtk.CellRendererText()
        ring_mode.pack_start(renderer_text, True)
        ring_mode.add_attribute(renderer_text, "text", 0)
        ring_grid.attach(ring_mode, 1,0,1,1)

        #Color Picker
        ring_clabel = Gtk.Label(label="Color: ")
        ring_grid.attach(ring_clabel, 0,1,1,1)
        ring_color = Gtk.ColorButton()
        ring_grid.attach(ring_color, 1,1,1,1)


        #Brightness

        ring_blabel = Gtk.Label(label="Brightness: ")
        ring_grid.attach(ring_blabel, 0,2,1,1)

        bright_value = Gtk.Adjustment(0, 0, 5, 1, 1, 0)
        ring_bright = Gtk.SpinButton()
        ring_bright.set_adjustment(bright_value)
        ring_grid.attach(ring_bright, 1,2,1,1)

        #Speed
        global ring_speed
        global ring_slabel

        ring_speed = Gtk.SpinButton()

        def updatespeed(x):

            if ring_mode.get_active() == 1:
                global ring_slabel
                ring_slabel = Gtk.Label(label="Speed: ")
                ring_grid.attach(ring_slabel, 0,3,1,1)

                global ring_speed
                speed_value = Gtk.Adjustment(0, 0, 5, 1, 1, 0)
                ring_speed = Gtk.SpinButton()
                ring_speed.set_adjustment(speed_value)
                ring_grid.attach(ring_speed, 1,3,1,1)

                ring_slabel.show()
                ring_speed.show()

            else:
                ring_speed.hide()
                ring_slabel.hide()


        ring_mode.connect("changed", updatespeed)
        


        #StackSwitcher
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(component)
        grid.attach(stack_switcher,0,0,1,1)
        grid.attach(component, 0,1,1,1)

        #####BUTTONS#######
        def apply_clicked(self):

            #Logo Values
            print("\n==============\n")
            if logo_mode.get_active() == 0:
                final_logo_mode = "static"
            elif logo_mode.get_active() == 1:
                final_logo_mode = "breathe"
            else:
                print("ERROR: No mode set for logo")

            final_logo_brightness = str(logo_bright.get_value_as_int())
            final_logo_speed = str(logo_speed.get_value_as_int())

            def rgb_to_hex(rgb):

                red = int(rgb.red * 255)
                green = int(rgb.green * 255)
                blue = int(rgb.blue * 255)
                return '#%02x%02x%02x' % (red,green,blue)

            final_logo_color = str(rgb_to_hex(logo_color.get_rgba()))

            print("Logo:",final_logo_mode,final_logo_brightness,final_logo_speed,final_logo_color)

            #Fan Values
            print("\n==============\n")
            if fan_mode.get_active() == 0:
                final_fan_mode = "static"
            elif fan_mode.get_active() == 1:
                final_fan_mode = "breathe"
            else:
                print("ERROR: No mode set for fan")

            final_fan_brightness = str(fan_bright.get_value_as_int())    
            final_fan_speed = str(fan_speed.get_value_as_int())

            def rgb_to_hex(rgb):

                red = int(rgb.red * 255)
                green = int(rgb.green * 255)
                blue = int(rgb.blue * 255)
                return '#%02x%02x%02x' % (red,green,blue)

            final_fan_color = str(rgb_to_hex(fan_color.get_rgba()))

            print("Fan:",final_fan_mode,final_fan_brightness,final_fan_speed,final_fan_color)

            #Ring Values
            print("\n==============\n")
            if ring_mode.get_active() == 0:
                final_ring_mode = "static"
            elif ring_mode.get_active() == 1:
                final_ring_mode = "breathe"
            else:
                print("ERROR: No mode set for ring")

            final_ring_brightness = str(ring_bright.get_value_as_int())    
            final_ring_speed = str(ring_speed.get_value_as_int())

            def rgb_to_hex(rgb):

                red = int(rgb.red * 255)
                green = int(rgb.green * 255)
                blue = int(rgb.blue * 255)
                return '#%02x%02x%02x' % (red,green,blue)

            final_ring_color = str(rgb_to_hex(ring_color.get_rgba()))

            print("Ring:",final_ring_mode,final_ring_brightness,final_ring_speed,final_ring_color)


            #Final Command
            final_command = "cm-rgb-cli set logo --mode=" + final_logo_mode + " --color=" + final_logo_color + " --brightness=" + final_logo_brightness + " --speed=" + final_logo_speed + " fan --mode=" + final_fan_mode + " --color=" + final_fan_color + " --brightness=" + final_fan_brightness + " --speed=" + final_fan_speed + " ring --mode=" + final_ring_mode + " --color=" + final_ring_color + " --brightness=" + final_ring_brightness + " --speed=" + final_ring_speed
            print(final_command)
            os.system(final_command)

        def disable_clicked(self):
            print("Disabling all RGB")
            os.system("cm-rgb-cli set logo --mode=off save")


        btn_apply = Gtk.Button(label="Apply")
        btn_apply.connect("clicked", apply_clicked)
        grid.attach(btn_apply, 0,3,1,1)

        btn_disable = Gtk.Button(label="Disable all RGB")
        btn_disable.connect("clicked", disable_clicked)
        grid.attach(btn_disable, 0,2,1,1)



win = myWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
