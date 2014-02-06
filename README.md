Cepko
=====

Cepko implements easy-to-use communication with
[CloudSigma](http://cloudsigma.com)'s VMs through a virtual serial port
without bothering with formatting the messages properly nor parsing the
output with the specific and sometimes confusing shell tools for that purpose.

Having the server definition accessible by the VM can ve useful in various ways.
For example it is possible to easily determine from within the VM, which network
interfaces are connected to public and which to private network. Another use is
to pass some data to initial VM setup scripts, like setting the hostname to the
VM name or passing ssh public keys through server meta.

For more information take a look at the [Server Context section of CloudSigma
API Docs](http://cloudsigma-docs.readthedocs.org/en/latest/server_context.html)


Installation
============

     pip install cepko


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


License
=======

    Copyright (C) 2013-2014 CloudSigma

    Author: Kiril Vladimiroff <kiril.vladimiroff@cloudsigma.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 3, as
    published by the Free Software Foundation.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
