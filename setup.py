from setuptools import setup, find_packages
import os


with open('requirements.txt', 'r') as f:
    requires=f.readlines()

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'gentle', '__version__.py'), 'r') as _:
    exec(_.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=about['__url__'],
    license=about['__license__'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
    ],
    python_requires='>=3.7',
    install_requires=requires,
    include_package_data=True,
    package_data={
        '': ['gentle/core/config.conf'],
    },
)
