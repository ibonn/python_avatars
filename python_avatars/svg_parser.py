import os
import re
from typing import Optional, Union, Any
from xml.etree import ElementTree as ET

SVG_NAMESPACE_URI = 'http://www.w3.org/2000/svg'
XLINK_NAMESPACE_URI = 'http://www.w3.org/1999/xlink'

# Register namespaces
ET.register_namespace('', SVG_NAMESPACE_URI)
ET.register_namespace('xlink', XLINK_NAMESPACE_URI)


class SVGParser:

    def __init__(self, path: Optional[str] = None, svg: Optional[ET.Element] = None) -> None:
        if path is None and svg is None:
            raise Exception('ArgumentMissingException')

        elif path is None:
            self.tree = svg

        elif svg is None:
            tree = ET.parse(path)
            self.tree = tree.getroot()

            # Rename IDs
            self.prefix = os.path.splitext(os.path.basename(path))[0]
            self.__rename_ids()

    def __rename_ids(self) -> None:

        xlink_href = '{{{}}}href'.format(XLINK_NAMESPACE_URI)

        attrs = ['clip-path', 'filter', 'mask']

        for x in self.tree.iter():
            if x.get('id') is not None:
                new_id = '{}_{}'.format(self.prefix, x.get('id'))
                x.set('id', new_id)

            for attr in attrs:
                self.__replace(x, attr, r'url\(#(.+)\)', r'url(#{}_{})')

            self.__replace(x, xlink_href, r'#(.+)', r'#{}_{}')

    def __replace(self, x: ET.Element, attr: str, regex: str, replacement: str):
        if x.get(attr) is not None:
            match = re.match(regex, x.get(attr))
            new_id = replacement.format(self.prefix, match.group(1))
            x.set(attr, new_id)

    def get_element_by_id(self, element_id: str) -> Union['SVGParser', None]:
        result = self.tree.findall(
            '''.//*[@id='{}_{}']'''.format(self.prefix, element_id))

        if len(result) == 0:
            return None

        return SVGParser(svg=result[0])

    def set_attr(self, name: str, value: Any) -> None:
        self.tree.set(name, str(value))

    def children(self, tag_name: Optional[str] = None) -> list['SVGParser']:

        if tag_name is None:
            return [SVGParser(svg=x) for x in self.tree]

        else:
            result = self.tree.findall(
                '{{{}}}{}'.format(SVG_NAMESPACE_URI, tag_name))

            if len(result) == 0:
                raise Exception('TagNotFoundException: {}'.format(tag_name))

            return [SVGParser(svg=x) for x in result]

    def render(self, path: Optional[str] = None) -> str:

        svg_str = str(self)

        if path is not None:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(svg_str)

        return svg_str

    def set_content(self, content: Union[None, list, str, 'SVGParser']) -> None:
        if content is None:
            pass
        elif isinstance(content, list):
            for elem in content:
                self.set_content(elem)
        elif isinstance(content, str):
            self.tree.text = content
        else:
            self.tree.append(content.tree)

    def __str__(self) -> str:
        return ET.tostring(self.tree, encoding='utf-8', method='xml').decode('utf-8')


if __name__ == '__main__':
    parser = SVGParser(path='avatar_parts/styles/avataaar_circle.svg')
    hair = SVGParser(path='avatar_parts/top/bun.svg')
    hair.get_element_by_id(
        'Hair-Color').children('path')[0].set_attr('fill', '#FF0000')
    parser.get_element_by_id('Top').set_content(hair.children())
    parser.render('test.svg')
