def bind_to(event):
    def decorator(func):
        func._bind_to = event
        return func
    return decorator


class Tool:
    text = "BaseTool"
    icon = None

    def __init__(self, target):
        self.target = target

    def on_enabled(self):
        print("Activated tool {}".format(self.text))

    def on_disabled(self):
        print("Deactivated tool {}".format(self.text))

    def on_click_down(self, event):
        print("Clicked down with tool {}".format(self.text))

    def on_click_up(self, event):
        print("Clicked up with tool {}".format(self.text))

    def on_clicked_motion(self, event):
        pass

    def on_hover(self, event):
        pass

    @bind_to("<ButtonPress-1>")
    def _on_click_down(self, event):
        self.on_click_down(event)

    @bind_to("<ButtonRelease-1>")
    def _on_click_up(self, event):
        self.on_click_up(event)

    @bind_to("<Button1-Motion>")
    def _on_clicked_motion(self, event):
        self.on_clicked_motion(event)

    @bind_to("<Motion>")
    def _on_hover(self, event):
        self.on_hover(event)
