from setuptools import setup, find_packages
from sample import __version__, __author__, __email__

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if __name__ == "__main__":
    setup(
        name="{{NAME_PLACEHOLDER}}",
        version=__version__,
        packages=find_packages(),
        author= __author__,
        long_description=long_description,
        long_description_content_type="text/markdown",
        author_email=__email__,
        description="{{DESCRIPTION_PLACEHOLDER}}",
        url=f"https://github.com/{__author__}/{{NAME_PLACEHOLDER}}",
        install_requires=[
            "spacepy",
            "astropy",
            "xarray",
            "selenium==4.23.1",
            "chromedriver-binary==128.*",
            "tqdm",
            "numpy",
            "aiofiles",
            "beautifulsoup4",
            "pandas",
            "pillow",
            "joblib",
            "aiohttp",
            "viresclient",
            "asyncio",
        ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: {{LICENSE_PLACEHOLDER}} License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS :: MacOS X",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Astronomy",
            "Topic :: Scientific/Engineering :: Physics",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering :: Visualization",
            "Topic :: Scientific/Engineering :: Image Processing",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Framework :: Matplotlib",
            "Framework :: Pytest",
            "Framework :: Sphinx",
            "Framework :: Jupyter",
            "Framework :: IPython",
            "Environment :: Console",
            "Environment :: Web Environment",
            "Natural Language :: English",
            "Typing :: Typed",
        ],
    )

