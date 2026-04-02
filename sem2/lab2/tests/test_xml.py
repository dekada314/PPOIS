from pathlib import Path
from xml.dom import minidom
from xml.sax import make_parser

from src.model.teacher import Teacher
from src.model.xml_reader import SAXParser
from src.model.xml_writer import DOMParser


def test_dom_parser_writes_xml_with_teacher_data(tmp_path):
    out_file = tmp_path / "teachers.xml"
    teachers = [
        Teacher(
            faculty="ФКСИС",
            department="ИИТ",
            fio="Иванов Иван",
            academic_title="доцент",
            academic_degree="кандидат наук",
            work_experience=11.0,
        )
    ]

    parser = DOMParser()
    parser.parse_doc(teachers, str(out_file))

    assert out_file.exists()
    doc = minidom.parse(str(out_file))
    teacher_nodes = doc.getElementsByTagName("teacher")
    assert len(teacher_nodes) == 1
    assert doc.getElementsByTagName("faculty")[0].firstChild.nodeValue == "ФКСИС"
    assert doc.getElementsByTagName("work_experience")[0].firstChild.nodeValue == "11.0"


def test_dom_parser_add_subnode_creates_node_with_text():
    parser = DOMParser()
    teacher_node = parser.doc.createElement("teacher")

    parser._add_teacher_subnode(teacher_node, "faculty", "ФИТУ")

    assert teacher_node.getElementsByTagName("faculty")[0].firstChild.nodeValue == "ФИТУ"


def test_sax_parser_characters_accumulate_text_chunks():
    sax_handler = SAXParser()
    sax_handler.startElement("teacher", {})
    sax_handler.startElement("fio", {})
    sax_handler.characters("  Иванов ")
    sax_handler.characters(" Иван ")
    sax_handler.endElement("fio")
    sax_handler.endElement("teacher")

    assert sax_handler.teachers[0].fio == "ИвановИван"
