from xml.sax import handler, make_parser

from src import config
from src.model.teacher import Teacher


class SAXParser(handler.ContentHandler):
    def __init__(self):
        self.teachers: list[Teacher] = []
        self.curr_teacher: None | Teacher = None
        self.curr_field: None | str = None
        self.buffer: str = ""
        
    def startElement(self, name, attrs) -> None:  #noqa 
        if name == 'teacher':
            self.curr_teacher = Teacher()
        elif self.curr_teacher is not None:
            self.curr_field = name
            
    def endElement(self, name) -> None: #noqa
        if self.curr_field:
            setattr(self.curr_teacher, self.curr_field, self.buffer)
            self.curr_field = None
            self.buffer = ""
            
        if name == 'teacher':
            self.teachers.append(self.curr_teacher)
            self.curr_teacher = None
        
    
    def characters(self, content):
        subnode_text = content.strip()
        self.buffer += subnode_text
        

if __name__ == "__main__":
    parser = make_parser()
    sax_handler = SAXParser()
    parser.setContentHandler(sax_handler)
    parser.parse(config.TEACHER_XML_PATH)
    print(sax_handler.teachers)
        