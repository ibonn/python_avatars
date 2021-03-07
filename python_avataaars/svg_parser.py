import os
import re
from xml.etree import ElementTree as ET

SVG_NAMESPACE_URI = 'http://www.w3.org/2000/svg'
XLINK_NAMESPACE_URI = 'http://www.w3.org/1999/xlink'

# Register namespaces
ET.register_namespace('', SVG_NAMESPACE_URI)
ET.register_namespace('xlink', XLINK_NAMESPACE_URI)

class SVGParser:

    def __init__(self, path=None, svg=None):
        if path is None and svg is None:
            raise Exception('ArgumentMissingException')

        elif path is None:
            self.tree = svg

        elif svg is None:
            tree = ET.parse(self.__get_path(path))
            self.tree = tree.getroot()
            
            # Rename IDs
            self.prefix = os.path.splitext(os.path.basename(path))[0]
            self.__rename_ids()

    def __rename_ids(self):

        xlink_href = '{{{}}}href'.format(XLINK_NAMESPACE_URI)

        for x in self.tree.iter():
            if x.get('id') is not None:
                new_id = '{}_{}'.format(self.prefix, x.get('id'))
                x.set('id', new_id)
            
            if x.get('clip-path') is not None:
                match = re.match('url\(#(.+)\)', x.get('clip-path'))
                new_id = 'url(#{}_{})'.format(self.prefix, match.group(1))
                x.set('clip-path', new_id)

            if x.get('filter') is not None:
                match = re.match('url\(#(.+)\)', x.get('filter'))
                new_id = 'url(#{}_{})'.format(self.prefix, match.group(1))
                x.set('filter', new_id)

            if x.get('mask') is not None:
                match = re.match('url\(#(.+)\)', x.get('mask'))
                new_id = 'url(#{}_{})'.format(self.prefix, match.group(1))
                x.set('mask', new_id)


            if x.get(xlink_href) is not None:
                match = re.match('#(.+)', x.get(xlink_href))
                new_id = '#{}_{}'.format(self.prefix, match.group(1))
                x.set(xlink_href, new_id)

    @staticmethod
    def __get_path(path):
        package_path = os.path.dirname(__file__)
        return os.path.join(package_path, path)

    def get_element_by_id(self, element_id):
        result = self.tree.findall('''.//*[@id='{}_{}']'''.format(self.prefix, element_id))

        if len(result) == 0:
            # raise Exception('IdNotFoundException: {}'.format(element_id))
            return None

        return SVGParser(svg=result[0])

    def set_attr(self, name, value):
        self.tree.set(name, str(value))

    def children(self, tag_name=None):

        if tag_name is None:
            return [SVGParser(svg=x) for x in self.tree]

        else:
            # TODO get namespace from document
            result = self.tree.findall('{{{}}}{}'.format(SVG_NAMESPACE_URI, tag_name))

            if len(result) == 0:
                raise Exception('TagNotFoundException: {}'.format(tag_name))
            
            return [SVGParser(svg=x) for x in result]

    def render(self, path=None):

        svg_str = str(self)

        if path is not None:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(svg_str)

        return svg_str

    def set_content(self, content):
        if content is None:
            pass
        elif isinstance(content, list):
            for elem in content:
                self.set_content(elem)
        elif isinstance(content, str):
            self.tree.text = content
        else:
            self.tree.append(content.tree)

    def __str__(self):
        return ET.tostring(self.tree, encoding='utf-8', method='xml').decode('utf-8')


if __name__ == '__main__':
    parser = SVGParser(path='avatar_parts/styles/avataaar_circle.svg')
    hair = SVGParser(path='avatar_parts/top/bun.svg')
    hair.get_element_by_id('Hair-Color').children('path')[0].set_attr('fill', '#FF0000')
    parser.get_element_by_id('Top').set_content(hair.children())
    parser.render('test.svg')
