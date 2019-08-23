from setuptools import setup, find_packages

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GPLv3",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 1",
    "Programming Language :: Python :: 3.7",
]

setup(
    name="kelfi",
    version="1.0",
    author="Kelvin Hsu",
    author_email="cliff@thekerrlab.com",
    description="Kernel Embedding Likelihood-Free Inference",
    keywords=["stochastic", "optimization"],
    platforms=["OS Independent"],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "ghalton",
        "tensorflow",
    ],
)