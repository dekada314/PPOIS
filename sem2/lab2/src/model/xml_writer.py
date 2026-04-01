from dataclasses import asdict
from xml.dom import minidom

import src.config as config
from src.model.teacher import Teacher


class DOMParser:
    def __init__(self):
        self.doc = minidom.Document()
        self.root = self.doc.createElement("teachers")
        self.doc.appendChild(self.root)

    def parse_doc(self, teachers: list[Teacher], file_path: str) -> None:
        for teacher in teachers:
            teacher_el = self.doc.createElement("teacher")
            data = asdict(teacher)

            for key, value in data.items():
                self._add_teacher_subnode(teacher_el, key, str(value))

            self.root.appendChild(teacher_el)

        self._write_to_file(file_path)

    def _add_teacher_subnode(
        self, main_node: minidom.Element, name: str, value: str
    ) -> None:
        subnode = self.doc.createElement(name)
        subnode_text = self.doc.createTextNode(value)
        subnode.appendChild(subnode_text)

        main_node.appendChild(subnode)

    def _write_to_file(self, file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.doc.toprettyxml(indent="  "))
