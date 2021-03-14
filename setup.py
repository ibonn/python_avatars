from setuptools import setup

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='python_avataaars',
    version='1.0.0',
    description='SVG Avatar library for Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=['python_avataaars'],
    package_dir={'python_avataaars': 'python_avataaars'},
    package_data={'python_avataaars': ['*.json', 'avatar_parts/**/*.svg', 'avatar_parts/**/**/*.svg']},
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
        'Development Status :: 3 - Alpha',
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