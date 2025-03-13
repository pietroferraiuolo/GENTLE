from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requires=f.readlines()

setup(
    name='GENTLE',
    version='0.2.1',
    author='Pietro Ferraiuolo',
    author_email='pietro.ferraiuolo@inaf.it',
    description='GENeral inTerferometer Laboratory intErface',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pietroferraiuolo/GENTLE',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=requires,
    include_package_data=True,
)
