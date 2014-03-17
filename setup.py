from setuptools import setup

setup(
    name="cepko",
    packages=["cepko"],
    version="1.0.1",
    description="Communication with CloudSigma's VMs through a virtual serial port",
    author="CloudSigma AG",
    author_email="dev-support@cloudsigma.com",
    url="https://github.com/cloudsigma/cepko",
    keywords=["cepko", "cloud", "cloudsigma", "serial port", "serial", "console"],
    install_requires=['pyserial'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Terminals :: Serial",
    ],
    long_description="""\
Cepko implements easy-to-use communication with CloudSigma's VMs through a virtual
serial port without bothering with formatting the messages properly nor parsing the
output with the specific and sometimes confusing shell tools for that purpose.

Having the server definition accessible by the VM can ve useful in various ways.
For example it is possible to easily determine from within the VM, which network
interfaces are connected to public and which to private network. Another use is
to pass some data to initial VM setup scripts, like setting the hostname to the
VM name or passing ssh public keys through server meta.

For more information take a look at the Server Context section of CloudSigma
API Docs: http://cloudsigma-docs.readthedocs.org/en/latest/server_context.html

Usage
=====

Imports and definitions
-----------------------

    >>> from cepko import Cepko
    >>> client = Cepko()


Fetch the whole server context
------------------------------

    >>> server_context = client.all()
    >>> server_context['name']


Fetch the server's meta
-----------------------

    >>> meta = client.meta()
    >>> meta['ssh_public_key']
    'ssh-rsa AAAAB3NzaC1yc2EAAAAD...'

Fetch conrete key from the server context
-----------------------------------------

    >>> drives = client.get('drives')
    >>> [key for key in drives[0]['drive']]
    ['uuid', 'tags', 'media', 'name', 'meta', 'allow_multimount', 'licenses', 'affinities', 'size']
    >>> drives[0]['drive']['size']
    10737418240

Fetch nested key from the server context
----------------------------------------

    >>> first_drive = client.get('drives/0/drive')
    >>> first_drive['size']
    10737418240
    """
)
