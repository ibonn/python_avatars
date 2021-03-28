from setuptools import setup

from python_avatars import __version__

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='python_avatars',
    version=__version__,
    description='SVG avatar library for Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=['python_avatars'],
    package_dir={
        'python_avatars': 'python_avatars'
    },
    package_data={'python_avatars': [
        '*.json',
        'avatar_parts/**/*.svg',
        'avatar_parts/**/**/*.svg'
    ]},
    author='Ibon',
    author_email='ibonescartin@gmail.com',
    keywords=['avatar', 'svg', 'python', 'face', 'custom'],
    url='https://github.com/ibonn/python_avatars',
    download_url='https://pypi.org/project/python_avatars/',
    project_urls={
        "Documentation": "https://readthedocs.org/projects/python_avatars/",
        "Source Code": "https://github.com/ibonn/python_avatars"
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
