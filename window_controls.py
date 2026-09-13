class WindowToggler:
    def __init__(self, root):
        self.root = root
        self.visible = True
    def toggle(self):
        if self.visible == True:
            self.root.iconify()
            self.visible = False
        else:
            self.root.deiconify()
            self.visible = True
    def on_hotkey(self):
        self.root.after(0, self.toggle)