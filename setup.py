from setuptools import setup, find_packages
setup(
    name="torngas",
    version="0.1.0",
    description="torngas based on tornado",
    author="qingyun meng",
    url="http://github.com/mqingyn/torngas",
    license="LGPL",
    packages= find_packages(),
    package_data={'torngas': ['resource/app/*.*',
                              'resource/app/app/*.*',
                              'resource/app/translations',
                              'resource/app/Main/*.*',
                              'resource/app/Main/models/*.*',
                              'resource/app/templates/*.*',
                              'resource/app/Main/views/*.*',
                              'resource/*.*']},
    author_email = "maingyn@gmail.com",
    requires=['Tornado'],
    scripts=["torngas/scripts/create_torngas.py"],
    )
