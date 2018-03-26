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
        """Called when the tool is activated
        """
        print("Activated tool {}".format(self.text))

    def on_disabled(self):
        """Called when the tool is deactivated
        """
        print("Deactivated tool {}".format(self.text))

    def on_click_down(self, event):
        """Called when a click down event happens on the target.
        """
        print("Clicked down with tool {}".format(self.text))

    def on_click_up(self, event):
        """Called when a click release event happens on the target.
        """
        print("Clicked up with tool {}".format(self.text))

    def on_clicked_motion(self, event):
        """Called when a clicked motion event happens on the target.
        """
        pass

    def on_hover(self, event):
        """Called when a motion event happens on the target.
        """
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
