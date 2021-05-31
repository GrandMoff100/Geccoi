from setuptools import setup
import requests

MAX = 20


def up(version):
    version = [int(x) for x in version.split('.')]
    version[-1] += 1
    version.reverse()
    for i, x in enumerate(version):
        quotient = (x - x % MAX) // MAX
        if quotient > 0:
            version[i + 1] += quotient
        version[i] = x % MAX
    version.reverse()
    return '.'.join([str(x) for x in version])


def current_version():
    data = requests.get('https://pypi.org/pypi/Geccoi/json').json()
    return data['info']['version']


setup(
    name='Geccoi',
    version=up(current_version()),
    packages=['geccoi', 'geccoi.ic', "geccoi.gesture_recog"],
    url='https://github.com/GrandMoff100/Geccoi',
    license='GNU License',
    author='Quantum_Wizard',
    author_email='nlarsen23.student@gmail.com',
    description='Gesture Controlled Computer Operation and Input.',
    install_requires=open('requirements.txt', 'r').read().splitlines(),
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        geccoic=geccoi.gecli:cli
    '''
)
