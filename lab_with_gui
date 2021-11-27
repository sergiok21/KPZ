import time

from kivy import args
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty, partial
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.chip import MDChip
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.snackbar import Snackbar
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp, sp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem, MDList, OneLineIconListItem, IconLeftWidget, TwoLineListItem
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivymd.uix.toolbar import MDToolbar

from kivy.config import Config

Window.size = (800, 800)
Config.set('graphics', 'resizable', '0')
Config.write()

var = []
val = []

condition_eq = []
condition_min = []
condition_start = []

var_condition = []
val_condition = []
array_print_condition = []

array_prints = []

condition = False
end = False


class Interpretator(MDScreen):
    check_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.bind(on_key_down=self._on_keyboard_down)

        self.triggerNavigation = NavigationLayout()
        self.navigation = MDNavigationDrawer()
        self.toolbar = MDToolbar()
        self.sm = ScreenManager()
        self.screen = MDScreen()
        self.sv = ScrollView()
        self.list = MDList()

        self.rl = RelativeLayout()
        self.bl = MDBoxLayout()

        self.text_input = MDTextField()

        self.run = OneLineListItem(text='Run code')

        self.label = MDLabel(text='')

        self.str_edit = str()
        self.tab1 = "           "
        self.pos_right = 0.11
        self.condition = False

        self.label_rw = MDLabel(text='Write')
        self.label_edit = MDLabel(text='Edit')
        self.label_remove = MDLabel(text='Remove')

        Clock.schedule_once(self.config_widget)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 66:
            self.read.active = True
        elif keycode == 67:
            self.edit.active = True
        # elif len(modifiers) > 0 and modifiers[0] == "shift" and keycode == 40: # New line in text input
        #     print("Shift + enter")
        elif keycode == 68:
            self.remove.active = True
        elif keycode == 41:
            Clock.schedule_once(self.back)
        elif keycode == 40:
            if "if" in self.text_input.text:
                self.condition = True
                condition_start.append(int(len(self.bl.children)))
                # print(condition_start)
                # print(len(self.bl.children))

            elif "end" == self.text_input.text:
                self.condition = False
                self.pos_right = 0.11
                condition_start.append(int(len(self.bl.children)) + 1)
                # print(condition_start)

            if self.condition is True:
                if self.text_input.text != "" and self.text_input.text != " ":
                    if self.edit.active is True:
                        Clock.unschedule(self.change_text)
                        self.text_input.focus = False
                        self.text_input.text = ''
                    else:
                        if len(self.text_input.text) >= 100:
                            for i in range(len(self.text_input.text)):
                                if i == int(len(self.text_input.text) / 2):
                                    self.str_edit += '\n'
                                self.str_edit += self.text_input.text[i]
                            self.text_input.text = self.str_edit
                            if len(self.bl.children) > 0:
                                self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab1), str("|"))))
                            self.bl.add_widget(MDRaisedButton(text=self.text_input.text,
                                                              pos_hint={"right": self.pos_right}, size=[18, 20],
                                                              on_release=self.change_conf))
                        else:
                            tab = ""
                            if len(self.bl.children) > 0:
                                for i in range(len(self.text_input.text) + 5):
                                    tab += " "
                                self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab1), str("|"))))
                            self.bl.add_widget(MDRaisedButton(text=self.text_input.text,
                                                              pos_hint={"right": self.pos_right},
                                                              on_release=self.change_conf))
                        self.text_input.text = ''
                        if len(self.bl.children) == 15:
                            self.sv.scroll_y = 0
                        self.pos_right = 0.15
                        Clock.schedule_once(self.auto_focus)
            else:
                if self.text_input.text != "" and self.text_input.text != " ":
                    if self.edit.active is True:
                        Clock.unschedule(self.change_text)
                        self.text_input.focus = False
                        self.text_input.text = ''
                    else:
                        if len(self.text_input.text) >= 100:
                            for i in range(len(self.text_input.text)):
                                if i == int(len(self.text_input.text) / 2):
                                    self.str_edit += '\n'
                                self.str_edit += self.text_input.text[i]
                            self.text_input.text = self.str_edit
                            if len(self.bl.children) > 0:
                                self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab1), str("|"))))
                            self.bl.add_widget(MDRaisedButton(text=self.text_input.text,
                                                              pos_hint={"left": 1}, size=[18, 20],
                                                              on_release=self.change_conf))
                            # self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str("|"))))
                        else:
                            tab = ""
                            if len(self.bl.children) > 0:
                                for i in range(len(self.text_input.text) + 5):
                                    tab += " "
                                self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab1), str("|"))))
                            self.bl.add_widget(MDRaisedButton(text=self.text_input.text,
                                                              pos_hint={"left": 1}, on_release=self.change_conf))
                        self.text_input.text = ''
                        if len(self.bl.children) == 15:
                            self.sv.scroll_y = 0
                        # print(len(self.bl.children))
                        Clock.schedule_once(self.auto_focus)

        elif keycode == 62:
            Clock.schedule_once(self.deploy)

    def auto_focus(self, dt):
        self.text_input.focus = True

    def config_widget(self, dt):
        self.add_widget(self.triggerNavigation)
        self.triggerNavigation.add_widget(self.sm)
        self.sm.add_widget(self.screen)
        self.screen.add_widget(self.rl)

        self.sv.size_hint_y = .8
        self.sv.pos_hint = {"top": 0.9}
        self.sv.scroll_distance = 0.1

        self.bl.adaptive_height = True
        self.bl.spacing = 5
        self.bl.orientation = 'vertical'

        self.toolbar.pos_hint = {"center_x": .5, "top": 1}
        self.toolbar.left_action_items = [["menu", lambda x: self.navigation.set_state("open")]]

        self.list.spacing = 10
        self.navigation.add_widget(self.list)

        self.list.pos_hint = {"top": 0.7}

        self.triggerNavigation.add_widget(self.navigation)

        self.list.add_widget(self.run)
        self.run.bind(on_release=self.deploy)

        self.rl.add_widget(self.toolbar)
        self.rl.add_widget(self.label)
        self.rl.add_widget(self.sv)

        self.sv.add_widget(self.bl)

        self.text_input.required = False
        self.text_input.multiline = False
        self.text_input.pos_hint = {"top": 0.1, "right": 0.9}
        self.text_input.hint_text = "Enter code"
        self.text_input.mode = "rectangle"
        self.text_input.size_hint_x = 0.8
        self.rl.add_widget(self.text_input)

        self.label_rw.pos_hint = {"top": 1.46, "right": 1.25}
        self.label_rw.theme_text_color = "Custom"
        self.rl.add_widget(self.label_rw)

        self.label_edit.pos_hint = {"top": 1.46, "right": 1.49}
        self.label_edit.theme_text_color = "Custom"
        self.rl.add_widget(self.label_edit)

        self.label_remove.pos_hint = {"top": 1.46, "right": 1.73}
        self.label_remove.theme_text_color = "Custom"
        self.rl.add_widget(self.label_remove)

        self.layout_for_checkbox1 = RelativeLayout()
        # with self.layout_for_checkbox1.canvas.before:
        #     Rectangle(pos=self.pos, size=[20, 40])
        #     Color(1, 0, 0, 1)
        self.layout_for_checkbox1.size_hint = (0.03, 0.03)
        self.layout_for_checkbox1.pos_hint = {"top": 0.96, "right": 0.36}

        self.layout_for_checkbox2 = RelativeLayout()
        self.layout_for_checkbox2.size_hint = (0.03, 0.03)
        self.layout_for_checkbox2.pos_hint = {"top": 0.96, "right": 0.59}

        self.layout_for_checkbox3 = RelativeLayout()
        self.layout_for_checkbox3.size_hint = (0.03, 0.03)
        self.layout_for_checkbox3.pos_hint = {"top": 0.96, "right": 0.86}

        self.read = CheckBox()
        self.read.pos_hint = {"top": 1.46, "right": 0.85}
        self.read.group = 'group'
        self.read.color = (0, 1, 0, 1)
        self.read.active = True

        self.edit = CheckBox()
        self.edit.pos_hint = {"top": 1.46, "right": 0.85}
        self.edit.color = (0, 1, 0, 1)
        self.edit.group = 'group'

        self.remove = CheckBox()
        self.remove.pos_hint = {"top": 1.46, "right": 0.85}
        self.remove.group = 'group'
        self.remove.color = (0, 1, 0, 1)

        self.rl.add_widget(self.layout_for_checkbox1)
        self.layout_for_checkbox1.add_widget(self.read)

        self.rl.add_widget(self.layout_for_checkbox2)
        self.layout_for_checkbox2.add_widget(self.edit)

        self.rl.add_widget(self.layout_for_checkbox3)
        self.layout_for_checkbox3.add_widget(self.remove)

        Clock.schedule_interval(self.check_switch, 0.1)

    def check_switch(self, dt):
        if self.read.active is True:
            Clock.schedule_once(partial(self.read_mode, self.text_input), 0)

        elif self.edit.active is True:
            Clock.schedule_once(self.edit_mode)

        elif self.remove.active is True:
            Clock.schedule_once(self.remove_mode)

        elif self.read.active is False & self.edit.active is False & self.remove.active is False:
            self.label_rw.text_color = (0, 0, 0, 1)
            self.label_edit.text_color = (0, 0, 0, 1)
            self.label_remove.text_color = (0, 0, 0, 1)

    def read_mode(self, instance, dt):
        if self.text_input not in self.rl.children:
            self.rl.add_widget(self.text_input)
            self.text_input.focus = True

        # if self.text_input.text != "" and self.text_input.text != " ":
        #     if self.text_input.text[len(self.text_input.text) - 1] == "'":
        #         if self.text_input.text[len(self.text_input.text) - 2] != "'":
        #             self.text_input.text += "'"
        #             instance.cursor = (len(instance.text) - 1, 0)

        self.label_rw.text_color = (0, 1, 0, 1)
        self.label_edit.text_color = (0, 0, 0, 1)
        self.label_remove.text_color = (0, 0, 0, 1)

        Clock.unschedule(self.change_text)

    def edit_mode(self, dt):
        if self.text_input not in self.rl.children:
            self.rl.add_widget(self.text_input)

        self.label_edit.text_color = (0, 1, 0, 1)
        self.label_rw.text_color = (0, 0, 0, 1)
        self.label_remove.text_color = (0, 0, 0, 1)

    def remove_mode(self, dt):
        self.label_remove.text_color = (0, 1, 0, 1)
        self.label_edit.text_color = (0, 0, 0, 1)
        self.label_rw.text_color = (0, 0, 0, 1)

        self.rl.remove_widget(self.text_input)

        Clock.unschedule(self.change_text)

    def change_conf(self, instance):
        if self.edit.active is True:
            self.text_input.text = instance.text
            self.widget = instance
            self.text_input.focus = True
            Clock.schedule_interval(self.change_text, 0.1)

        elif self.remove.active is True:
            for i in range(len(self.bl.children)):
                if self.bl.children[i] == instance:
                    print(self.bl.children)
                    print(i)
                    if len(self.bl.children) - 1 == i:
                        if len(self.bl.children) == 1:
                            self.bl.remove_widget(self.bl.children[i])
                            break
                        else:
                            self.bl.remove_widget(self.bl.children[i])
                            self.bl.remove_widget(self.bl.children[i - 1])
                            break
                    else:
                        self.bl.remove_widget(self.bl.children[i])
                        self.bl.remove_widget(self.bl.children[i])
                        break

    def change_text(self, dt):
        self.widget.text = self.text_input.text
        Clock.schedule_once(self.check_empty)

    def check_empty(self, dt):
        if self.widget.text == "":
            if self.text_input.focus is False:
                self.bl.remove_widget(self.widget)

    def deploy(self, dt):
        self.add_to_condition = False
        self.start = False
        self.transit = []
        check = len(condition_start) - 2
        # print("test text = ", self.bl.children[condition_start[check + 2] + 3].text)
        try:
            for i in range(1, len(self.bl.children) + 1):
                # print(self.bl.children[len(self.bl.children) - i].text)
                if self.bl.children[len(self.bl.children) - i].text == self.bl.children[condition_start[check] + 3].text:
                    # print("text = ", self.bl.children[condition_start[check] + 3].text)
                    check -= 2
        except:
            pass
        try:
            var.clear()
            val.clear()
            var_condition.clear()
            val_condition.clear()
            array_prints.clear()
            condition_eq.clear()
            condition_min.clear()
            array_print_condition.clear()
        except:
            pass

        # try:
        # if self.add_to_condition is True:
        #     for i in range(1, len(self.bl.children) + 1):
        #         if "=" in self.bl.children[len(self.bl.children) - i].text:
        #             if "if" not in self.bl.children[len(self.bl.children) - i].text:
        #                 for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
        #                     if self.bl.children[len(self.bl.children) - i].text[j] == "=":
        #                         if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
        #                             var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
        #                         else:
        #                             var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
        # for i in range(1, len(self.bl.children) + 1):
        #     if "=" in self.bl.children[len(self.bl.children) - i].text:
        #         if self.add_to_condition is True:
        #             for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
        #                 if self.bl.children[len(self.bl.children) - i].text[j] == "=":
        #                     if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
        #                         var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
        #                     else:
        #                         var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
        #         if "if" not in self.bl.children[len(self.bl.children) - i].text:
        #             if self.add_to_condition is False:
        #                 for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
        #                     if self.bl.children[len(self.bl.children) - i].text[j] == "=":
        #                         if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
        #                             var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
        #                         else:
        #                             var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
        #         else:
        #             self.add_to_condition = True
        #     elif "<" in self.bl.children[len(self.bl.children) - i].text:
        #         self.add_to_condition = True
        #     elif "end" == self.bl.children[len(self.bl.children) - i].text:
        #         self.add_to_condition = False
            # elif "print" in self.bl.children[len(self.bl.children) - i].text:
            #     if self.add_to_condition is False:
            #         check_num = []
            #         for m in range(len(var)):
            #             if self.bl.children[len(self.bl.children) - i].text[
            #                          6:len(self.bl.children[len(self.bl.children) - i].text) - 1] == var[m]:
            #                 check_num.append(m)
            #         print(check_num)
            #         array_prints.append(check_num[len(check_num) - 1])
        for i in range(1, len(self.bl.children) + 1):
            if "=" in self.bl.children[len(self.bl.children) - i].text:
                if self.add_to_condition is True:
                    for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
                        if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                            if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=":  # val
                                if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                    var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                else:
                                    var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                    self.bl.children[len(self.bl.children) - i].text)])
                                break
                        else:  # (without space)
                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=":  # =
                                if self.bl.children[len(self.bl.children) - i].text[j + 2] != " ":  # =_ (with space)
                                    if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                    else:
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                    val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                        self.bl.children[len(self.bl.children) - i].text)])
                                    break
                                else:  # = (without space)
                                    if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                    else:
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                    val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                        self.bl.children[len(self.bl.children) - i].text)])
                                    break
                        # if self.bl.children[len(self.bl.children) - i].text[j] == "=": # for var cond with space
                        #     if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                        #         var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                        #     else:
                        #         var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                        # if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ": # for val cond with space
                        #     if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=":
                        #         val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                        #             self.bl.children[len(self.bl.children) - i].text)])
                        #         break
                        # else:
                        #     if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=":
                        #         if self.bl.children[len(self.bl.children) - i].text[j + 2] != " ":
                        #             # for n in range(len(var)):
                        #             if self.bl.children[len(self.bl.children) - i].text[j] != " ":
                        #                 var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                        #             else:
                        #                 var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                        #             val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                        #                 self.bl.children[len(self.bl.children) - i].text)])
                        #             break
                        #             # break
                        #         else:
                        #             val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                        #                     self.bl.children[len(self.bl.children) - i].text)])
                        #             break
                elif self.bl.children[len(self.bl.children) - i].text[0:2] != "if" and "print" not in self.bl.children[
                    len(self.bl.children) - i].text:
                    if self.add_to_condition is True:
                        for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
                            # print(self.bl.children[len(self.bl.children) - i].text[j])
                            # if self.bl.children[len(self.bl.children) - i].text[j] == "=":
                            #     print(self.bl.children[len(self.bl.children) - i].text)
                            #     if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                            #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                            #     else:
                            #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j])

                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                                if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=": # val
                                    if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                        var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                    else:
                                        var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                    val.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                        self.bl.children[len(self.bl.children) - i].text)])
                                    break
                            else: # (without space)
                                # if self.bl.children[len(self.bl.children) - i].text[j] == "=":
                                #     if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                #     else:
                                #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                # else:
                                #     pass
                                if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=": # =
                                    if self.bl.children[len(self.bl.children) - i].text[j + 2] != " ": # = (with space)
                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                        else:
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                        val.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                        break
                                    else: # = (without space)
                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                        else:
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                        val.append(self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                        break
                    else:
                        for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
                            # print(self.bl.children[len(self.bl.children) - i].text[j])
                            # if self.bl.children[len(self.bl.children) - i].text[j] == "=":
                            #     print(self.bl.children[len(self.bl.children) - i].text)
                            #     if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                            #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                            #     else:
                            #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j])

                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                                if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=":  # val
                                    if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                        var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                    else:
                                        var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                    val.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                        self.bl.children[len(self.bl.children) - i].text)])
                                    break
                            else:  # (without space)
                                # if self.bl.children[len(self.bl.children) - i].text[j] == "=":
                                #     if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                #     else:
                                #         var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                # else:
                                #     pass

                                if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=":  # =
                                    if self.bl.children[len(self.bl.children) - i].text[
                                        j + 2] != " ":  # = (with space)
                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                        else:
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                        val.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                        break
                                    else:  # = (without space)
                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                        else:
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                        val.append(self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                        break
                    # if len(var_condition) > len(val_condition):
                    #     for b in range(len(val_condition), len(var_condition)):
                    #         var_condition.pop(b)
                    #         val.pop(len(val) - 1)
                    # print(val, "test")
                    # print(var_condition, "test")
                else:
                    pass
            elif "<" in self.bl.children[len(self.bl.children) - i].text: # condition <
                check = 3
                stop = 0
                for k in range(3, len(self.bl.children[len(self.bl.children) - i].text)):
                    if stop > 0:
                        print("Break!")
                        print(stop)
                        break
                    if self.bl.children[len(self.bl.children) - i].text[k] == " ":
                        for b in range(len(var)):
                            if self.bl.children[len(self.bl.children) - i].text[check:k] == var[b]:
                                if self.bl.children[len(self.bl.children) - i].text[k + 1] == "<":  # var <
                                    if self.bl.children[len(self.bl.children) - i].text[k + 3] == " ":  # var < var2
                                        if self.bl.children[len(self.bl.children) - i].text[
                                           k + 4:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
                                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                             check:k])] < val[var.index(self.bl.children[len(
                                                    self.bl.children) - i].text[k + 4:len(self.bl.children[len(
                                                    self.bl.children) - i].text) - 1])]:
                                                condition_min.append(True)
                                                stop += 1
                                                self.add_to_condition = True
                                                # self.start = True
                                            else:
                                                condition_min.append(False)
                                                stop += 1
                                                self.add_to_condition = False
                                                # self.start = False
                                    else:  # var <var2
                                        if self.bl.children[len(self.bl.children) - i].text[
                                           k + 3:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
                                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                             check:k
                                                             ])] < val[
                                                var.index(self.bl.children[len(self.bl.children) - i].text[
                                                          k + 3:len(self.bl.children[
                                                                        len(self.bl.children) - i].text) - 1])]:
                                                condition_min.append(True)
                                                stop += 1
                                                self.add_to_condition = True
                                                # self.start = True
                                            else:
                                                condition_min.append(False)
                                                stop += 1
                                                self.add_to_condition = False
                                                # self.start = False

                    elif self.bl.children[len(self.bl.children) - i].text[k] == "<":  # var<
                        if self.bl.children[len(self.bl.children) - i].text[k + 2] == " ":  # var< var2
                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[check:k])] < val[
                                var.index(self.bl.children[len(self.bl.children) - i].text[k + 3:len(
                                    self.bl.children[len(self.bl.children) - i].text) - 1])]:
                                condition_min.append(True)
                                stop += 1
                                self.add_to_condition = True
                            else:
                                condition_min.append(False)
                                stop += 1
                                self.add_to_condition = False
                        else:  # var<var2
                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                             check:k
                                             ])] < val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                                  k + 2:len(self.bl.children[len(
                                                                      self.bl.children) - i].text) - 1])]:
                                condition_min.append(True)
                                stop += 1
                                self.add_to_condition = True
                            else:
                                condition_min.append(False)
                                stop += 1
                                self.add_to_condition = False
            elif "==" in self.bl.children[len(self.bl.children) - i].text:
                check = 3
                stop = 0
                for k in range(3, len(self.bl.children[len(self.bl.children) - i].text)):
                    if stop > 0:
                        print("Break for equal!")
                        break
                    if self.bl.children[len(self.bl.children) - i].text[k] == " ":
                        for b in range(len(var)):
                            if self.bl.children[len(self.bl.children) - i].text[check:k] == var[b]:
                                if self.bl.children[len(self.bl.children) - i].text[k + 1] == "=":  # var ==
                                    if self.bl.children[len(self.bl.children) - i].text[k + 3] == " ":  # var == var2
                                        if self.bl.children[len(self.bl.children) - i].text[
                                           k + 4:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
                                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                             check:k])] == val[var.index(self.bl.children[len(
                                                    self.bl.children) - i].text[k + 4:len(self.bl.children[len(
                                                    self.bl.children) - i].text) - 1])]:
                                                condition_eq.append(True)
                                                stop += 1
                                                self.add_to_condition = True
                                            else:
                                                condition_eq.append(False)
                                                stop += 1
                                                self.add_to_condition = False
                                    else:  # var ==var2
                                        if self.bl.children[len(self.bl.children) - i].text[
                                           k + 3:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
                                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                             check:k
                                                             ])] == val[
                                                var.index(self.bl.children[len(self.bl.children) - i].text[
                                                          k + 3:len(self.bl.children[
                                                                        len(self.bl.children) - i].text) - 1])]:
                                                condition_eq.append(True)
                                                stop += 1
                                                self.add_to_condition = True
                                            else:
                                                condition_eq.append(False)
                                                stop += 1
                                                self.add_to_condition = False

                    elif self.bl.children[len(self.bl.children) - i].text[k] == "=":  # var==
                        if self.bl.children[len(self.bl.children) - i].text[k + 2] == " ":  # var== var2
                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[check:k])] == val[
                                var.index(self.bl.children[len(self.bl.children) - i].text[k + 3:len(
                                    self.bl.children[len(self.bl.children) - i].text) - 1])]:
                                condition_eq.append(True)
                                stop += 1
                                self.add_to_condition = True
                            else:
                                condition_eq.append(False)
                                stop += 1
                                self.add_to_condition = False
                        else:  # var==var2
                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                             check:k
                                             ])] == val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                                  k + 2:len(self.bl.children[
                                                                                len(self.bl.children) - i].text) - 1
                                                                  ])]:
                                condition_eq.append(True)
                                stop += 1
                                self.add_to_condition = True
                            else:
                                condition_eq.append(False)
                                stop += 1
                                self.add_to_condition = False
            elif "print" in self.bl.children[len(self.bl.children) - i].text:
                if self.add_to_condition is True:
                    index = -1
                    for m in range(len(var_condition)):
                        if var_condition[m] == self.bl.children[len(self.bl.children) - i].text[
                                               6:len(self.bl.children[len(self.bl.children) - i].text) - 1]:
                            index = m
                    if index != -1:
                        array_print_condition.append(index)
                else:
                    index = -1
                    for m in range(len(var)):
                        if var[m] == self.bl.children[len(self.bl.children) - i].text[
                                    6:len(self.bl.children[len(self.bl.children) - i].text) - 1]:
                            index = m
                    if index != -1:
                        array_prints.append(index)

            elif "end" == self.bl.children[len(self.bl.children) - i].text:
                self.add_to_condition = False

        # for n in range(len(val)):
        #     iteration = n
        #     for m in range(iteration, len(var)):
        #         if var[n] == val[m]:
        #             val[m] = val[n]
        # index = 0
        # for i in range(1, len(self.bl.children) + 1):
        #     if "print" in self.bl.children[len(self.bl.children) - i].text:
        #         for m in range(len(var)):
        #             if var[m] == self.bl.children[len(self.bl.children) - i].text[
        #                          6:len(self.bl.children[len(self.bl.children) - i].text) - 1]:
        #                 index = m
        #         array_prints.append(index)
        # try:
        #     for n in range(len(val)):
        #         for m in range(len(var)):
        #             if var[n] == val[m]:
        #                 val[m] = val[n]
                    # elif var[i] == var[j]:
                    #     var.pop(i)
                    #     val.pop(i)
                        # break
        # except:
        #     pass
        # for i in range(1, len(self.bl.children) + 1):
        #     if "if" in self.bl.children[len(self.bl.children) - i].text:
        #         if "==" in self.bl.children[len(self.bl.children) - i].text:
        #             check = 3
        #             stop = 0
        #             for k in range(3, len(self.bl.children[len(self.bl.children) - i].text)):
        #                 if stop > 0:
        #                     break
        #                 if self.bl.children[len(self.bl.children) - i].text[k] == " ":
        #                     for b in range(len(var)):
        #                         if self.bl.children[len(self.bl.children) - i].text[check:k] == var[b]:
        #                             if self.bl.children[len(self.bl.children) - i].text[k + 1] == "=": # var ==
        #                                 if self.bl.children[len(self.bl.children) - i].text[k + 3] == " ": # var == var2
        #                                     if self.bl.children[len(self.bl.children) - i].text[
        #                                        k + 4:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
        #                                         if val[var.index(self.bl.children[len(self.bl.children) - i].text[
        #                                                           check:k
        #                                                           ])] == val[var.index(self.bl.children[len(self.bl.children) - i].text[
        #                                                           k + 4:len(self.bl.children[
        #                                                                         len(self.bl.children) - i].text) - 1])]:
        #                                             condition_eq.append(True)
        #                                             stop += 1
        #                                         else:
        #                                             condition_eq.append(False)
        #                                             stop += 1
        #                                 else: # var ==var2
        #                                     if self.bl.children[len(self.bl.children) - i].text[
        #                                        k + 3:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
        #                                         if val[var.index(self.bl.children[len(self.bl.children) - i].text[
        #                                                         check:k
        #                                                         ])] == val[var.index(self.bl.children[len(self.bl.children) - i].text[
        #                                        k + 3:len(self.bl.children[len(self.bl.children) - i].text) - 1])]:
        #                                             condition_eq.append(True)
        #                                             stop += 1
        #                                         else:
        #                                             condition_eq.append(False)
        #                                             stop += 1
        #
        #                 elif self.bl.children[len(self.bl.children) - i].text[k] == "=": # var==
        #                     if self.bl.children[len(self.bl.children) - i].text[k + 2] == " ": # var== var2
        #                         if val[var.index(self.bl.children[len(self.bl.children) - i].text[check:k])] == val[
        #                             var.index(self.bl.children[len(self.bl.children) - i].text[k + 3:len(
        #                                 self.bl.children[len(self.bl.children) - i].text) - 1])]:
        #                             condition_eq.append(True)
        #                             stop += 1
        #                         else:
        #                             condition_eq.append(False)
        #                             stop += 1
        #                     else: # var==var2
        #                         if val[var.index(self.bl.children[len(self.bl.children) - i].text[
        #                               check:k
        #                               ])] == val[var.index(self.bl.children[len(self.bl.children) - i].text[
        #                             k + 2:len(self.bl.children[len(self.bl.children) - i].text) - 1
        #                                         ])]:
        #                             condition_eq.append(True)
        #                             stop += 1
        #                         else:
        #                             condition_eq.append(False)
        #                             stop += 1
                # elif "<" in self.bl.children[len(self.bl.children) - i].text:
                #     check = 3
                #     stop = 0
                #     for k in range(3, len(self.bl.children[len(self.bl.children) - i].text)):
                #         if stop > 0:
                #             break
                #         if self.bl.children[len(self.bl.children) - i].text[k] == " ":
                #             for b in range(len(var)):
                #                 if self.bl.children[len(self.bl.children) - i].text[check:k] == var[b]:
                #                     if self.bl.children[len(self.bl.children) - i].text[k + 1] == "<":  # var <
                #                         if self.bl.children[len(self.bl.children) - i].text[k + 3] == " ":  # var < var2
                #                             if self.bl.children[len(self.bl.children) - i].text[
                #                                k + 4:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
                #                                 if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                #                                                  check:k
                #                                                  ])] < val[
                #                                     var.index(self.bl.children[len(self.bl.children) - i].text[
                #                                               k + 4:len(self.bl.children[
                #                                                             len(self.bl.children) - i].text) - 1])]:
                #                                     condition_min.append(True)
                #                                     stop += 1
                #                                 else:
                #                                     condition_min.append(False)
                #                                     stop += 1
                #                         else:  # var ==var2
                #                             if self.bl.children[len(self.bl.children) - i].text[
                #                                k + 3:len(self.bl.children[len(self.bl.children) - i].text) - 1] in var:
                #                                 if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                #                                                  check:k
                #                                                  ])] < val[
                #                                     var.index(self.bl.children[len(self.bl.children) - i].text[
                #                                               k + 3:len(self.bl.children[
                #                                                             len(self.bl.children) - i].text) - 1])]:
                #                                     condition_min.append(True)
                #                                     stop += 1
                #                                 else:
                #                                     condition_min.append(False)
                #                                     stop += 1
                #
                #         elif self.bl.children[len(self.bl.children) - i].text[k] == "<":  # var<
                #             if self.bl.children[len(self.bl.children) - i].text[k + 2] == " ":  # var< var2
                #                 if val[var.index(self.bl.children[len(self.bl.children) - i].text[check:k])] < val[
                #                     var.index(self.bl.children[len(self.bl.children) - i].text[k + 3:len(
                #                         self.bl.children[len(self.bl.children) - i].text) - 1])]:
                #                     condition_min.append(True)
                #                     stop += 1
                #                 else:
                #                     condition_min.append(False)
                #                     stop += 1
                #             else:  # var<var2
                #                 if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                #                                  check:k
                #                                  ])] < val[var.index(self.bl.children[len(self.bl.children) - i].text[
                #                                                       k + 2:len(self.bl.children[
                #                                                                     len(self.bl.children) - i].text) - 1
                #                                                       ])]:
                #                     condition_min.append(True)
                #                     stop += 1
                #                 else:
                #                     condition_min.append(False)
                #                     stop += 1

        # print("var", var)
        # print("val", val)
        # print("array_pr", array_prints)
        # print(string_for_condition)
        # print("var", var)
        # print("var_cond", var_condition)
        print("cond", var_condition, val_condition)
        print("var", var, val)
        print("cond_min", condition_min)

        self.navigation.set_state("close")
        Clock.schedule_once(self.new_screen)

    def new_screen(self, dt):
        self.rl2 = RelativeLayout()

        self.toolbar2 = MDToolbar()

        self.sv2 = ScrollView()
        self.bl2 = MDBoxLayout()

        self.text_input2 = MDTextField()

        Clock.schedule_once(self.config)

    def config(self, dt):
        self.remove_widget(self.triggerNavigation)
        self.remove_widget(self.rl)
        # self.remove_widget(self.sv)

        self.rl2 = RelativeLayout()

        self.toolbar2 = MDToolbar()

        self.sv2 = ScrollView()
        self.bl2 = MDBoxLayout()

        self.text_input2 = MDTextField()

        self.add_widget(self.rl2)

        self.toolbar2.pos_hint = {"center_x": .5, "top": 1}
        self.toolbar2.left_action_items = [["arrow-left", lambda x: self.back(x)]]
        self.rl2.add_widget(self.toolbar2)

        self.sv2.size_hint_y = .8
        self.sv2.pos_hint = {"top": 0.9}
        self.sv2.scroll_distance = 0.1
        self.rl2.add_widget(self.sv2)

        self.bl2.adaptive_height = True
        self.bl2.spacing = 25
        self.bl2.orientation = 'vertical'
        self.sv2.add_widget(self.bl2)

        self.text_input2.required = False
        self.text_input2.multiline = False
        self.text_input2.pos_hint = {"top": 0.1, "right": 0.9}
        self.text_input2.hint_text = "Enter code"
        self.text_input2.mode = "rectangle"
        self.text_input2.size_hint_x = 0.8
        self.rl2.add_widget(self.text_input2)

        Clock.schedule_once(self.view_interpreter)

    def view_interpreter(self, dt):
        self.tab = "    "
        self.bl2.add_widget(MDLabel(text=""))
        self.iter_for_print = 0
        self.iter_for_val = 0
        self.check_true_for_eq = 0
        self.check_true_for_min = 0
        self.iter_for_condition_eq = 0
        self.iter_for_condition_min = 0
        self.condition_bool_true = False
        self.condition_bool_min = False
        self.bool_condition = False
        print("eq", condition_eq)
        print("print cond", array_print_condition)
        print("just print", array_prints)
        # try:
        for i in range(1, len(self.bl.children) + 1):
            if "end" == self.bl.children[len(self.bl.children) - i].text:
                self.bool_condition = False
                self.condition_bool_true = False
                self.condition_bool_min = False
            elif "print" in self.bl.children[len(self.bl.children) - i].text:
                if self.bool_condition is False:
                    if self.condition_bool_min is False:
                        if self.condition_bool_true is False:
                            try:
                                print(array_prints, val)
                                self.bl2.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str(
                                    val[array_prints[self.iter_for_print]]))))
                                # val.pop(self.iter_for_print)
                                # var.pop(self.iter_for_print)
                                self.iter_for_print += 1
                            except:
                                pass
                else:
                    print("True~")
                    # if condition_eq[self.iter_for_condition_eq] is True: # if condition is true for ==
                    #     try:
                    #         self.bl2.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str(
                    #             val_condition[array_print_condition[self.iter_for_val]]))))
                    #         self.iter_for_val += 1
                    #         self.iter_for_condition_eq += 1
                    #     except:
                    #         pass
                    #             # if self.bl.children[len(self.bl.children) - i].text[6:len(
                    #             #     self.bl.children[len(self.bl.children) - i].text
                    #             # ) - 1] in var:
                    #             #     self.bl2.add_widget(MDLabel(
                    #             #         text=("%s%s") % (str(self.tab), str(val[array_prints[iter_for_print]]))))
                    #             #     iter_for_print += 1
                    #             #     iter_for_val += 1
                    #             #     iter_for_condition_eq += 1
                    if self.condition_bool_min is True:
                        if condition_min[self.iter_for_condition_min] is True: # if condition is true for <
                            try:
                                self.bl2.add_widget(
                                    MDLabel(text=("%s%s") % (str(self.tab), str(val_condition[self.iter_for_val]))))
                                self.iter_for_val += 1
                                self.iter_for_condition_min += 1
                            except:
                                pass
            elif "==" in self.bl.children[len(self.bl.children) - i].text:
                if condition_eq[self.check_true_for_eq] is True:
                    self.bool_condition = True
                    self.condition_bool_true = True
                    self.condition_bool_min = False
                    self.check_true_for_eq += 1
            elif "<" in self.bl.children[len(self.bl.children) - i].text:
                if condition_min[self.check_true_for_min] is True:
                    self.bool_condition = True
                    self.condition_bool_true = False
                    self.condition_bool_min = True
                    self.check_true_for_min += 1
            # for i in range(len(array_prints)):
            #     self.bl2.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str(val[array_prints[i]]))))
        # except:
        #     print("except")

    def back(self, dt):
        self.remove_widget(self.rl2)

        self.add_widget(self.triggerNavigation)


class App(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Interpretator(name="interpretator"))
        return sm


App().run()

# if App().get_running_app().stop() is None:
#     backup = open("backup.bck", "w")
