from setuptools import setup, find_packages
from tidal_dl.printf import VERSION

setup(
    name='tidal-dl',
    version=VERSION,
    license="Apache2",
    description="tidal-dl lets you download videos and tracks from Tidal.",

    author='les.cx',
    author_email="luca@les.cx",

    packages=find_packages(exclude=['tidal_gui*']),
    include_package_data=False,
    platforms="any",
    install_requires=["aigpy>=2022.7.8.1", 
                      "requests>=2.22.0",
                      "pycryptodome", 
                      "pydub", 
                      "prettytable",
                      "lxml"],
    entry_points={'console_scripts': ['tidal-dl = tidal_dl:main', ]}
)
