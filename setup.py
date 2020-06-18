from setuptools import setup


setup(
    name='Geccoi',
    version='0.0.1',
    packages=['geccoi', 'geccoi.ic', "geccoi.gesture_recog"],
    url='https://github.com/GrandMoff100/Geccoi',
    license='GNU License',
    author='Quantum_Wizard',
    author_email='',
    description='Gesture Controlled Computer Operation and Input.',
    install_requires=["PySimpleGUI",
                      "keyboard",
                      "mouse",
                      "opencv-contrib-python-headless",
                      "numpy",
                      "click",
                      "translate"],
    entry_points='''
        [console_scripts]
        geccoic=geccoi.gecli:cli
    '''
)
