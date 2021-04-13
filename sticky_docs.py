import sublime_plugin


class StickyDocsMoveCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=True):
        self.view.run_command("move", {"by": "lines", "forward": forward})
        if StickyDocsToggleCommand.enabled:  # TODO: use the enabled var of self.view
            self.view.window().run_command("auto_complete_open_link")


class StickyDocsToggleCommand(sublime_plugin.TextCommand):
    enabled = False

    def run(self, edit):
        cls = self.__class__
        # TODO: make this use instance variable
        cls.enabled = not cls.enabled
        if cls.enabled:
            self.view.run_command("auto_complete_open_link")
        else:
            self.view.run_command("hide_popup")


class CompleteCloseListener(sublime_plugin.EventListener):
    def on_post_text_command(self, view, command_name, args):
        if command_name == "hide_auto_complete":
            StickyDocsToggleCommand.enabled = False
