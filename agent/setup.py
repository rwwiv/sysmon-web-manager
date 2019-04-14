from setuptools import setup, find_packages

setup(
    name='SysMonager Agent',
    version='0.1.0',
    description='Client agent to communicate with SysMonager and manage sysmon locally.',
    author='William Wernert',
    author_email='william.wernert@gmail.com',
    url='https://github.com/rwwiv/sysmon-web-manager',
    packages=find_packages(exclude=('tests', 'docs'))
)
