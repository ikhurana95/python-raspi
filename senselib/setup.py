from setuptools import setup

setup(name='senselib',
      version='0.1',
      description='Drawing functions for Raspberry Pi Sense HAT',
      author='Ishan Khurana',
      author_email='ishan.khurana.15@ucl.ac.uk',
      license='MIT',
      packages=['senselib'],
      install_requires=['numpy', 'senseGraphics', 'time'],
      )
