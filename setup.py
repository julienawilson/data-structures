"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Data Structures.',
    version=0.1,
    author='Patrick Saunders, Julien Wilson',
    author_email='patrick.a.n.saunders@gmail.com, julienawilson@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['deque', 'dll', 'bst'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    install_requires=[
        alabaster==0.7.9
        appdirs==1.4.0
        appnope==0.1.0
        Babel==2.3.4
        backports.shutil-get-terminal-size==1.0.0
        bleach==1.5.0
        cycler==0.10.0
        -e git+https://github.com/julienawilson/data-structures.git@54a801f4f70daf5008929ae2cc98680d7240e353#egg=data_structures
        decorator==4.0.11
        docutils==0.13.1
        entrypoints==0.2.2
        gnureadline==6.3.3
        html5lib==0.9999999
        imagesize==0.7.1
        ipykernel==4.5.2
        ipyparallel==6.0.0
        ipython==5.2.1
        ipython-genutils==0.1.0
        ipywidgets==5.2.2
        Jinja2==2.9.5
        jsonschema==2.5.1
        jupyter-client==4.4.0
        jupyter-core==4.2.1
        MarkupSafe==0.23
        matplotlib==2.0.0
        mistune==0.7.3
        nbconvert==5.1.1
        nbformat==4.2.0
        nose==1.3.7
        notebook==4.3.1
        numpy==1.12.0
        packaging==16.8
        pandas==0.19.2
        pandocfilters==1.4.1
        path.py==10.1
        pexpect==4.2.1
        pickleshare==0.7.4
        prompt-toolkit==1.0.10
        ptyprocess==0.5.1
        Pygments==2.2.0
        pyparsing==2.1.10
        python-dateutil==2.6.0
        pytz==2016.10
        pyzmq==16.0.2
        qtconsole==4.2.1
        requests==2.13.0
        scikit-learn==0.18.1
        scipy==0.18.1
        simplegeneric==0.8.1
        six==1.10.0
        snowballstemmer==1.2.1
        Sphinx==1.5.2
        terminado==0.6
        testpath==0.3
        tornado==4.4.2
        traitlets==4.3.1
        wcwidth==0.1.7
        widgetsnbextension==1.2.6]
)
