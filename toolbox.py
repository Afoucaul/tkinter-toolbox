import tkinter as tk


def unbinder(instance):
    def unbind(sequence, funcid=None):
        if not funcid:
            instance.tk.call('bind', instance._w, sequence, '')
            return
        func_callbacks = instance.tk.call(
            'bind', instance._w, sequence, None).split('\n')
        new_callbacks = [
            l for l in func_callbacks if l[6:6 + len(funcid)] != funcid]
        instance.tk.call(
            'bind', instance._w, sequence, '\n'.join(new_callbacks))
        instance.deletecommand(funcid)

    return unbind


class Toolbox(tk.Frame):
    def __init__(self, parent, target, toolClasses):
        super().__init__(parent)
        self.target = target
        self.target.unbind = unbinder(self.target)
        self.target._toolboxBindings = []
        self.tools = [t(self.target) for t in toolClasses]
        self.buttons = []
        self.currentTool = None

        for i, t in enumerate(self.tools):
            button = tk.Button(
                self,
                text=t.text,
                image=t.icon,
                command=self._tool_selector(i),
                relief=tk.RAISED)
            button.pack(side=tk.LEFT)
            self.buttons.append(button)

    def _tool_selector(self, n):
        return lambda: self.select_tool(self.tools[n])

    def select_tool(self, tool):
        if self.currentTool is not None:
            for event, bindingId in self.target._toolboxBindings:
                self.target.unbind(event, bindingId)

            self.target._toolboxBindings.clear()
            self.currentTool.on_disabled()
            button = self.buttons[self.tools.index(self.currentTool)]
            button.config(relief=tk.RAISED)

        if tool == self.currentTool:
            self.currentTool = None
            return

        for member in dir(tool):
            member = getattr(tool, member)
            if '_bind_to' in dir(member):
                self.target._toolboxBindings.append(
                    (member._bind_to,
                     tool.target.bind(member._bind_to, member, "+")))

        self.currentTool = tool
        self.currentTool.on_enabled()
        self.buttons[self.tools.index(tool)].config(relief=tk.SUNKEN)
