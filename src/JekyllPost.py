
class JekyllPost:

    def __init__(self, file_path):
        f = open(file_path)
        state = 0
        self.contents = ""
        for line in f:
            # remove newline character 
            line = line[:-1]
            if len(line.split(":")) > 1 and state == 1:
                self.__setattr__(line.split(":")[0].strip(), line.split(":")[1].strip())
            elif line.strip() == "---":
                state = state ^ 1
            else:
                self.contents += line + "\n"
    
    def get_title(self) -> str:
        try:
            return self.title.replace("\"", "")
        except AttributeError:
            return ""
    
    def get_contents(self) -> str:
        try:
            return self.contents
        except AttributeError:
            return ""
    
    def get_categories(self):
        try:
            return self.category.split(" ")
        except AttributeError:
            return []
    
    
