from setuptools import setup, find_packages

setup(
    name="zctest",
    version="1.0",
    url='http://github.com/jzvelc/zctest',
    license='BSD',
    description="Django buildout test.",
    author='Jure Zvelc',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
)
