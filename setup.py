# setup.py

from setuptools import setup, find_packages

setup(
    name="netsec_lib",
    version="0.1.0",
    description="Une bibliothèque pour capturer et analyser le trafic réseau",
    author="Ton Nom",
    author_email="tonemail@example.com",
    url="https://github.com/tonnom/netsec_lib",
    packages=find_packages(),
    install_requires=[
        'scapy>=2.4.5',
        'pyshark>=0.4.2.9',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
