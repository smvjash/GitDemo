class generator():
    def __init__(self):
        self.text_ls = []

    def echo_text(self, text):
        print(text)
            
    def add_text(self, text):
        self.text_ls.append(text)

    def empty_text(self):
        self.text_ls.clear()

    def add_suffix(self, suffix, text):
        return text + " " + suffix
    
    def add_prefix(self, prefix, text):
        return prefix + " " + text
if __name__ == '__main__':
    text_generator = generator()
    text_generator.echo_text("This is a demo text")