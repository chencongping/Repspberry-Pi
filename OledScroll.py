class OledScroll():
    def __init__(self,  start, width):
        self.start = start
        self.width = width
        
    def setText(self, oled, text):
        self.oled = oled
        self.text = text
        
    def scrollShell(self):
        start = self.start
        width = self.width
        oled = self.oled
        text = self.text
        
        if start + width >= len(text) -1 :
            self.start = 0
        showText = text[start: start + width: 1]
        self.start = start + 1
        oled.text(showText, 0, 16)
        print("text: %d %d %s" % (start, width, text))
        oled.show()