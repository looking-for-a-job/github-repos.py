import setuptools

setuptools.setup(
    name='github-repos',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
