import xml.etree.ElementTree as ET
import json
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book) -> str:
        pass


class SerializerJson(Serializer):
    def serialize(self, book: Book):
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXml(Serializer):
    def serialize(self, book: Book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
