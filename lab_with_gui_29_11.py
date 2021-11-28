import os
from kivy.core.window import Window
from kivy.properties import ObjectProperty, partial
from kivy.uix.checkbox import CheckBox
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
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
        elif keycode == 68:
            self.remove.active = True
        elif keycode == 41:
            Clock.schedule_once(self.back)
        elif keycode == 40:
            if "if" in self.text_input.text:
                self.condition = True
                condition_start.append(int(len(self.bl.children)))
            elif "endif" == self.text_input.text:
                self.condition = False
                condition_start.append(int(len(self.bl.children)) + 1)

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
                            s = MDRectangleFlatButton(text=self.text_input.text,
                                                      pos_hint={"left": 1}, size=[18, 20],
                                                      on_release=self.change_conf)
                            s.text_color = (0, 0, 0, 1)
                            s.line_color = (0, 0, 0, 1)
                            self.bl.add_widget(s)
                        else:
                            tab = ""
                            if len(self.bl.children) > 0:
                                for i in range(len(self.text_input.text) + 5):
                                    tab += " "
                                self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab1), str("|"))))
                            s = MDRectangleFlatButton(text=self.text_input.text,
                                                      pos_hint={"left": 1}, size=[18, 20],
                                                      on_release=self.change_conf)
                            s.text_color = (0, 0, 0, 1)
                            s.line_color = (0, 0, 0, 1)
                            self.bl.add_widget(s)
                        self.text_input.text = ''
                        if len(self.bl.children) > 26:
                            self.sv.scroll_y = 0
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
                            s = MDRectangleFlatButton(text=self.text_input.text,
                                                              pos_hint={"left": 1}, size=[18, 20],
                                                              on_release=self.change_conf)
                            s.text_color = (0, 0, 0, 1)
                            s.line_color = (0, 0, 0, 1)
                            self.bl.add_widget(s)
                        else:
                            tab = ""
                            if len(self.bl.children) > 0:
                                for i in range(len(self.text_input.text) + 5):
                                    tab += " "
                                self.bl.add_widget(MDLabel(text=("%s%s") % (str(self.tab1), str("|"))))
                            s = MDRectangleFlatButton(text=self.text_input.text,
                                               pos_hint={"left": 1}, size=[18, 20],
                                               on_release=self.change_conf)
                            s.text_color = (0, 0, 0, 1)
                            s.line_color = (0, 0, 0, 1)
                            self.bl.add_widget(s)
                        self.text_input.text = ''
                        if len(self.bl.children) > 26:
                            self.sv.scroll_y = 0
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
        self.add_to_condition = None
        self.start = False
        self.transit = []
        check = len(condition_start) - 2
        try:
            for i in range(1, len(self.bl.children) + 1):
                if self.bl.children[len(self.bl.children) - i].text == self.bl.children[condition_start[check] + 3].text:
                    check -= 2
        except:
            pass

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

        Clock.schedule_once(self.clear)

    def clear(self, dt):
        self.iter = 1
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
        self.bool_condition = None
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
        self.view_interpreter(self.iter)

    def view_interpreter(self, dt):
        for i in range(self.iter, len(self.bl.children) + 1):
            if "==" in self.bl.children[len(self.bl.children) - i].text:
                check = 3
                stop = 0
                for k in range(3, len(self.bl.children[len(self.bl.children) - i].text)):
                    if stop > 0:
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
                                    else:  # var <var2
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
                        else:  # var<var2
                            if val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                             check:k
                                             ])] == val[var.index(self.bl.children[len(self.bl.children) - i].text[
                                                                 k + 2:len(self.bl.children[len(
                                                                     self.bl.children) - i].text) - 1])]:
                                condition_eq.append(True)
                                stop += 1
                                self.add_to_condition = True
                            else:
                                condition_eq.append(False)
                                stop += 1
                                self.add_to_condition = False
            elif "=" in self.bl.children[len(self.bl.children) - i].text:
                if self.add_to_condition is True:
                    for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
                        if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                            if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=":  # var = val
                                if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                    if self.bl.children[len(self.bl.children) - i].text[0:j - 1] in var_condition:
                                        pass
                                    else:
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                        val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                else:
                                    if self.bl.children[len(self.bl.children) - i].text[0:j] in var_condition:
                                        pass
                                    else:
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                        val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                break
                        else:  # (without space)
                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=":
                                if self.bl.children[len(self.bl.children) - i].text[j + 2] != " ":
                                    if self.bl.children[len(self.bl.children) - i].text[j] == " ": # var =val
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                    else:
                                        var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                    val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                        self.bl.children[len(self.bl.children) - i].text)])
                                    if self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                        self.bl.children[len(self.bl.children) - i].text)] in var_condition:
                                        for v in range(len(var_condition)):
                                            if self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                        self.bl.children[len(self.bl.children) - i].text)] == var_condition[v]:
                                                val_condition[val_condition.index(
                                                    self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                                        self.bl.children[len(self.bl.children) - i].text)])] = \
                                                val_condition[v]
                                                break

                                    else:
                                        val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                    break
                                else:
                                    if "input()" not in self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                            self.bl.children[len(self.bl.children) - i].text)]:
                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ": # var = val
                                            var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                        else:
                                            var_condition.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                        if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                            self.bl.children[len(self.bl.children) - i].text)] in var_condition:
                                            pass
                                        else:
                                            val_condition.append(self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                            self.bl.children[len(self.bl.children) - i].text)])
                                    else:
                                        for j in range(len(self.bl.children[len(self.bl.children) - 1].text)):
                                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                                                if self.bl.children[len(self.bl.children) - i].text[
                                                        j + 2] != "=":  # val
                                                    if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                                        pass
                                            else:  # (without space)
                                                if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=":  # =
                                                    if self.bl.children[len(self.bl.children) - i].text[
                                                            j + 2] != " ":  # = (with space)
                                                        pass
                                                    else:  # = (without space)
                                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                                            if var_condition:
                                                                if self.bl.children[len(self.bl.children) - i].text[
                                                                   0:j] in var_condition:
                                                                    for m in range(len(var_condition)):
                                                                        if var_condition[m] == self.bl.children[len(
                                                                                self.bl.children) - i].text[
                                                                                     0:j]:
                                                                            if m not in array_prints:
                                                                                if self.bl.children[
                                                                                       len(self.bl.children) - i].text[
                                                                                   j + 3:len(
                                                                                       self.bl.children[
                                                                                           len(
                                                                                               self.bl.children) - i].text)] in var_condition:
                                                                                    for n in range(len(var_condition)):
                                                                                        if self.bl.children[
                                                                                               len(
                                                                                                   self.bl.children) - i].text[
                                                                                           j + 3:len(
                                                                                               self.bl.children[
                                                                                                   len(
                                                                                                       self.bl.children) - i].text)] == \
                                                                                                var_condition[n]:
                                                                                            var_condition.append(self.bl.children[
                                                                                                           len(
                                                                                                               self.bl.children) - i].text[
                                                                                                       0:j])
                                                                                            var_condition.pop(m)
                                                                                            val_condition.pop(m)
                                                                                            break
                                                                                else:
                                                                                    var_condition.pop(m)
                                                                                    val_condition.pop(m)
                                                                                    var_condition.append(self.bl.children[
                                                                                                   len(
                                                                                                       self.bl.children) - i].text[
                                                                                               0:j])
                                                                                break
                                                                            else:
                                                                                if self.bl.children[
                                                                                       len(self.bl.children) - i].text[
                                                                                   j + 3:len(
                                                                                       self.bl.children[
                                                                                           len(
                                                                                               self.bl.children) - i].text)] in var_condition:
                                                                                    for n in range(len(var_condition)):
                                                                                        if self.bl.children[
                                                                                               len(
                                                                                                   self.bl.children) - i].text[
                                                                                           j + 3:len(
                                                                                               self.bl.children[
                                                                                                   len(
                                                                                                       self.bl.children) - i].text)] == \
                                                                                                var_condition[n]:
                                                                                            var_condition.append(
                                                                                                self.bl.children[
                                                                                                    len(
                                                                                                        self.bl.children) - i].text[
                                                                                                0:j])
                                                                                else:
                                                                                    if self.bl.children[
                                                                                           len(
                                                                                               self.bl.children) - i].text[
                                                                                       0:j] in var_condition:
                                                                                        ind = var_condition.index(
                                                                                            self.bl.children[
                                                                                                len(
                                                                                                    self.bl.children) - i].text[
                                                                                            0:j])
                                                                                        var_condition.pop(ind)
                                                                                        val_condition.pop(ind)
                                                                                        var_condition.append(
                                                                                            self.bl.children[
                                                                                                len(
                                                                                                    self.bl.children) - i].text[
                                                                                            0:j])
                                                                                    else:
                                                                                        var_condition.append(
                                                                                            self.bl.children[
                                                                                                len(
                                                                                                    self.bl.children) - i].text[
                                                                                            0:j])
                                                                                break
                                                                else:
                                                                    if self.bl.children[len(self.bl.children) - i].text[
                                                                       j + 3:len(
                                                                           self.bl.children[
                                                                               len(self.bl.children) - i].text)] in var_condition:
                                                                        var_condition.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[0:j])
                                                                    else:
                                                                        var_condition.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[0:j])
                                                                    break
                                                            else:
                                                                if self.bl.children[len(self.bl.children) - i].text[
                                                                   j + 3:len(
                                                                           self.bl.children[
                                                                               len(self.bl.children) - i].text)] in var_condition:
                                                                    for n in range(len(var_condition)):
                                                                        if self.bl.children[
                                                                               len(self.bl.children) - i].text[
                                                                           j + 3:len(self.bl.children[len(
                                                                               self.bl.children) - i].text)] == var_condition[n]:
                                                                            var_condition.append(self.bl.children[len(
                                                                                self.bl.children) - i].text[0:j])
                                                                            break
                                                                else:
                                                                    var_condition.append(self.bl.children[
                                                                                   len(self.bl.children) - i].text[0:j])
                                                        break
                    if "input()" in self.bl.children[len(self.bl.children) - i].text:
                        self.input_cond(i)
                        break
                elif "input()" in self.bl.children[len(self.bl.children) - i].text:
                    for j in range(len(self.bl.children[len(self.bl.children) - 1].text)):
                        if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                            if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=":  # val
                                if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                    pass
                        else:  # (without space)
                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=":  # =
                                if self.bl.children[len(self.bl.children) - i].text[j + 2] != " ":  # = (with space)
                                    pass
                                else:  # = (without space)
                                    if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                        if var:
                                            if self.bl.children[len(self.bl.children) - i].text[0:j] in var:
                                                for m in range(len(var)):
                                                    if var[m] == self.bl.children[len(self.bl.children) - i].text[
                                                                 0:j]:
                                                        if m not in array_prints:
                                                            if self.bl.children[len(self.bl.children) - i].text[
                                                               j + 3:len(
                                                                   self.bl.children[
                                                                       len(self.bl.children) - i].text)] in var:
                                                                for n in range(len(var)):
                                                                    if self.bl.children[
                                                                           len(self.bl.children) - i].text[
                                                                       j + 3:len(
                                                                           self.bl.children[
                                                                               len(self.bl.children) - i].text)] == \
                                                                            var[n]:
                                                                        var.append(self.bl.children[
                                                                                       len(
                                                                                           self.bl.children) - i].text[
                                                                                   0:j])
                                                                        var.pop(m)
                                                                        val.pop(m)
                                                                        break
                                                            else:
                                                                var.pop(m)
                                                                val.pop(m)
                                                                var.append(self.bl.children[
                                                                               len(self.bl.children) - i].text[0:j])
                                                            break
                                                        else:
                                                            if self.bl.children[len(self.bl.children) - i].text[
                                                               j + 3:len(
                                                                   self.bl.children[
                                                                       len(self.bl.children) - i].text)] in var:
                                                                for n in range(len(var)):
                                                                    if self.bl.children[
                                                                           len(self.bl.children) - i].text[
                                                                       j + 3:len(
                                                                           self.bl.children[
                                                                               len(self.bl.children) - i].text)] == \
                                                                            var[n]:
                                                                        var.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[
                                                                            0:j])
                                                            else:
                                                                if self.bl.children[
                                                                       len(self.bl.children) - i].text[
                                                                   0:j] in var:
                                                                    ind = var.index(self.bl.children[
                                                                                        len(self.bl.children) - i].text[
                                                                                    0:j])
                                                                    var.pop(ind)
                                                                    val.pop(ind)
                                                                    var.append(
                                                                        self.bl.children[
                                                                            len(self.bl.children) - i].text[
                                                                        0:j])
                                                                else:
                                                                    var.append(
                                                                        self.bl.children[
                                                                            len(self.bl.children) - i].text[
                                                                        0:j])
                                                            break
                                            else:
                                                if self.bl.children[len(self.bl.children) - i].text[
                                                   j + 3:len(
                                                       self.bl.children[
                                                           len(self.bl.children) - i].text)] in var:
                                                    var.append(
                                                        self.bl.children[len(self.bl.children) - i].text[0:j])
                                                else:
                                                    var.append(
                                                        self.bl.children[len(self.bl.children) - i].text[0:j])
                                                break
                                        else:
                                            if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                    self.bl.children[len(self.bl.children) - i].text)] in var:
                                                for n in range(len(var)):
                                                    if self.bl.children[len(self.bl.children) - i].text[
                                                       j + 3:len(self.bl.children[len(
                                                           self.bl.children) - i].text)] == var[n]:
                                                        var.append(self.bl.children[len(
                                                            self.bl.children) - i].text[0:j])
                                                        break
                                            else:
                                                var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                    break

                    self.input(i)
                    break
                elif self.bl.children[len(self.bl.children) - i].text[0:2] != "if" and "print" not in self.bl.children[
                    len(self.bl.children) - i].text and "input()" not in self.bl.children[len(self.bl.children) - 1].text:
                    if self.add_to_condition is None:
                        for j in range(len(self.bl.children[len(self.bl.children) - i].text)):
                            if self.bl.children[len(self.bl.children) - i].text[j + 1] == " ":
                                if self.bl.children[len(self.bl.children) - i].text[j + 2] != "=": # val
                                    if self.bl.children[len(self.bl.children) - i].text[j - 1] == " ":
                                        if var:
                                            for m in range(len(var)):
                                                if var[m] == self.bl.children[len(self.bl.children) - i].text[0:j - 1]:
                                                    if m not in array_prints:
                                                        var.pop(m)
                                                        val.pop(m)
                                                        val[m] = self.bl.children[len(
                                                            self.bl.children) - i].text[j + 2:len(self.bl.children[len(
                                                                self.bl.children) - i].text)]
                                                        var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                                        val.append(
                                                            self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                                                self.bl.children[len(self.bl.children) - i].text)])
                                        else:
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j - 1])
                                            val.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                                self.bl.children[len(self.bl.children) - i].text)])
                                    else:
                                        if var:
                                            for m in range(len(var)):
                                                if var[m] == self.bl.children[len(self.bl.children) - i].text[0:j]:
                                                    if m not in array_prints:
                                                        var.pop(m)
                                                        val.pop(m)
                                                        var.append(
                                                            self.bl.children[len(self.bl.children) - i].text[0:j])
                                                        val.append(
                                                            self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                                                self.bl.children[len(self.bl.children) - i].text)])
                                        else:
                                            var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                            val.append(self.bl.children[len(self.bl.children) - i].text[j + 2:len(
                                                self.bl.children[len(self.bl.children) - i].text)])
                                    break
                            else: # (without space)
                                if self.bl.children[len(self.bl.children) - i].text[j + 1] == "=": # =
                                    if self.bl.children[len(self.bl.children) - i].text[j + 2] != " ": # = (with space)
                                        pass
                                    else: # = (without space)
                                        if self.bl.children[len(self.bl.children) - i].text[j] == " ":
                                            if var:
                                                if self.bl.children[len(self.bl.children) - i].text[0:j] in var:
                                                    for m in range(len(var)):
                                                        if var[m] == self.bl.children[len(self.bl.children) - i].text[
                                                                     0:j]:
                                                            if m not in array_prints:
                                                                if self.bl.children[len(self.bl.children) - i].text[
                                                                   j + 3:len(
                                                                           self.bl.children[
                                                                               len(self.bl.children) - i].text)] in var:
                                                                    for n in range(len(var)):
                                                                        if self.bl.children[
                                                                               len(self.bl.children) - i].text[
                                                                           j + 3:len(
                                                                               self.bl.children[
                                                                                   len(self.bl.children) - i].text)] ==\
                                                                                var[n]:
                                                                            var.append(self.bl.children[
                                                                                           len(
                                                                                               self.bl.children) - i].text[
                                                                                       0:j])
                                                                            val.append(val[n])
                                                                            var.pop(m)
                                                                            val.pop(m)
                                                                            break
                                                                else:
                                                                    var.pop(m)
                                                                    val.pop(m)
                                                                    var.append(self.bl.children[
                                                                                   len(self.bl.children) - i].text[0:j])
                                                                    val.append(self.bl.children[
                                                                                   len(self.bl.children) - i].text[
                                                                               j + 3:len(
                                                                                   self.bl.children[len(
                                                                                       self.bl.children) - i].text)])
                                                                break
                                                            else:
                                                                if self.bl.children[len(self.bl.children) - i].text[
                                                                   j + 3:len(
                                                                           self.bl.children[
                                                                               len(self.bl.children) - i].text)] in var:
                                                                    for n in range(len(var)):
                                                                        if self.bl.children[
                                                                               len(self.bl.children) - i].text[
                                                                           j + 3:len(
                                                                               self.bl.children[
                                                                                   len(self.bl.children) - i].text)] ==\
                                                                                var[n]:
                                                                            var.append(
                                                                                self.bl.children[
                                                                                    len(self.bl.children) - i].text[
                                                                                0:j])
                                                                            val.append(val[n])
                                                                else:
                                                                    if self.bl.children[
                                                                            len(self.bl.children) - i].text[
                                                                        0:j] in var:
                                                                        ind = var.index(self.bl.children[
                                                                                      len(self.bl.children) - i].text[
                                                                                  0:j])
                                                                        var.pop(ind)
                                                                        val.pop(ind)
                                                                        var.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[
                                                                            0:j])
                                                                        val.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[
                                                                            j + 3:len(
                                                                                self.bl.children[
                                                                                    len(self.bl.children) - i].text)])
                                                                    else:
                                                                        var.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[
                                                                            0:j])
                                                                        val.append(
                                                                            self.bl.children[
                                                                                len(self.bl.children) - i].text[
                                                                            j + 3:len(
                                                                                self.bl.children[
                                                                                    len(self.bl.children) - i].text)])
                                                                break
                                                else:
                                                    if self.bl.children[len(self.bl.children) - i].text[
                                                               j + 3:len(
                                                                   self.bl.children[
                                                                       len(self.bl.children) - i].text)] in var:
                                                        var.append(
                                                            self.bl.children[len(self.bl.children) - i].text[0:j])
                                                        val.append(val[var.index(self.bl.children[len(
                                                            self.bl.children) - i].text[j + 3:len(
                                                                   self.bl.children[
                                                                       len(self.bl.children) - i].text)])])
                                                    else:
                                                        var.append(
                                                            self.bl.children[len(self.bl.children) - i].text[0:j])
                                                        val.append(self.bl.children[len(self.bl.children) - i].text[
                                                                   j + 3:len(
                                                                       self.bl.children[
                                                                           len(self.bl.children) - i].text)])
                                                    break
                                            else:
                                                if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                        self.bl.children[len(self.bl.children) - i].text)] in var:
                                                    for n in range(len(var)):
                                                        if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                    self.bl.children[len(self.bl.children) - i].text)] == var[n]:
                                                            var.append(self.bl.children[len(
                                                                self.bl.children) - i].text[0:j])
                                                            val.append(val[n])
                                                            var.pop(n)
                                                            val.pop(n)
                                                            break
                                                else:
                                                    var.append(self.bl.children[len(self.bl.children) - i].text[0:j])
                                                    val.append(
                                                        self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                            self.bl.children[len(self.bl.children) - i].text)])
                                        else:
                                            if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                    self.bl.children[len(self.bl.children) - i].text)] in var:
                                                for n in range(len(var)):
                                                    if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                            self.bl.children[len(
                                                                self.bl.children) - i].text)] == var[n]:
                                                        var.append(self.bl.children[len(
                                                            self.bl.children) - i].text[0:j])
                                                        val.append(val[n])
                                                        var.pop(n)
                                                        val.pop(n)
                                            else:
                                                if self.bl.children[len(self.bl.children) - i].text[0:j + 1] in var:
                                                    for n in range(len(var)):
                                                        if self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                    self.bl.children[len(self.bl.children) - i].text)] == var[n]:
                                                            var.append(self.bl.children[len(
                                                                self.bl.children) - i].text[0:j + 1])
                                                            val.append(val[n])
                                                            var.pop(n)
                                                            val.pop(n)
                                                            break
                                                else:
                                                    var.append(self.bl.children[len(self.bl.children) - i].text[0:j + 1])
                                                    val.append(self.bl.children[len(self.bl.children) - i].text[j + 3:len(
                                                        self.bl.children[len(self.bl.children) - i].text)])
                                                    break
                                        break
            elif "<" in self.bl.children[len(self.bl.children) - i].text: # condition <
                check = 3
                stop = 0
                for k in range(3, len(self.bl.children[len(self.bl.children) - i].text)):
                    if stop > 0:
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
                                            else:
                                                condition_min.append(False)
                                                stop += 1
                                                self.add_to_condition = False
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
                                            else:
                                                condition_min.append(False)
                                                stop += 1
                                                self.add_to_condition = False
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
            elif "print" in self.bl.children[len(self.bl.children) - i].text:
                if self.add_to_condition is True:
                    index = -1
                    for m in range(len(var_condition)):
                        if var_condition[m] == self.bl.children[len(self.bl.children) - i].text[
                                               6:len(self.bl.children[len(self.bl.children) - i].text) - 1]:
                            if var_condition[m] in var:
                                for n in range(len(var)):
                                    if var[n] == var_condition[m]:
                                        if val_condition[m] != val[n]:
                                            val_condition[m] = val[n]
                                            index = -2
                            else:
                                index = m
                    if index != -1 and index != -2:
                        array_print_condition.append(index)
                        self.bl2.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str(val_condition[index]))))
                    else:
                        for m in range(len(var)):
                            if var[m] == self.bl.children[len(self.bl.children) - i].text[
                                               6:len(self.bl.children[len(self.bl.children) - i].text) - 1]:
                                index = m
                        if index != -1:
                            var_condition.append(var[index])
                            val_condition.append(val[index])
                            array_print_condition.append(len(array_print_condition))
                            self.bl2.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str(val[index]))))
                else:
                    if self.add_to_condition is None:
                        index = -1
                        for m in range(len(var)):
                            if var[m] == self.bl.children[len(self.bl.children) - i].text[
                                        6:len(self.bl.children[len(self.bl.children) - i].text) - 1]:
                                index = m
                        if index != -1:
                            array_prints.append(index)
                            self.bl2.add_widget(MDLabel(text=("%s%s") % (str(self.tab), str(val[index]))))
            elif "endif" == self.bl.children[len(self.bl.children) - i].text:
                self.add_to_condition = None

        try:
            os.remove("backup.txt")
        except:
            pass
        file = open("backup.txt", "a")
        for i in range(1, len(self.bl.children) + 1):
            if "|" not in self.bl.children[len(self.bl.children) - i].text:
                file.write(self.bl.children[len(self.bl.children) - i].text)
                file.write('\n')

    def input(self, iter):
        self.iter = iter + 1
        Clock.schedule_interval(self.input2, 0.1)

    def input2(self, iter):
        if self.text_input2.text != "":
            if self.text_input2.focus is False:
                Clock.unschedule(self.input2)
                val.append(self.text_input2.text)
                self.text_input2.text = ""
                self.view_interpreter(iter)

    def input_cond(self, iter):
        self.iter = iter + 1
        Clock.schedule_interval(self.input2_cond, 0.1)

    def input2_cond(self, iter):
        if self.text_input2.text != "":
            if self.text_input2.focus is False:
                Clock.unschedule(self.input2_cond)
                val_condition.append(self.text_input2.text)
                self.text_input2.text = ""
                self.view_interpreter(iter)


    def back(self, dt):
        self.remove_widget(self.rl2)

        self.add_widget(self.triggerNavigation)


class App(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Interpretator(name="interpretator"))
        return sm


App().run()
