from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
from sample import __version__, __author__, __email__

setup(
    name='{{NAME_PLACEHOLDER}}',
    version=__version__,
    author=__author__,
    author_email=__email__,
    description='{{DESCRIPTION_PLACEHOLDER}}',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=f'https://github.com/{__author__}/{{NAME_PLACEHOLDER}}',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    ext_modules=[
        CUDAExtension(
            name='sample._C',
            sources=['src/cpu/sample.cpp', 'src/cuda/sample.cu'],
            include_dirs=['include'],
            extra_compile_args={'cxx': ['-O2'], 'nvcc': ['-O2']}
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    },
    install_requires=[
        'torch>=2.1.0',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: {{LICENSE_PLACEHOLDER}}",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
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
        "Framework :: Jupyter",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
    python_requires='>=3.10',
)
