"""
cepko implements easy-to-use communication with CloudSigma's VMs through
a virtual serial port without bothering with formatting the messages
properly nor parsing the output with the specific and sometimes
confusing shell tools for that purpose.

Having the server definition accessible by the VM can ve useful in various ways.
For example it is possible to easily determine from within the VM, which network
interfaces are connected to public and which to private network. Another use is
to pass some data to initial VM setup scripts, like setting the hostname to the
VM name or passing ssh public keys through server meta.

For more information take a look at the Server Context section of CloudSigma
API Docs: http://cloudsigma-docs.readthedocs.org/en/latest/server_context.html
"""
import json
import platform

import serial

SERIAL_PORT = '/dev/ttyS1'
if platform.system() == 'Windows':
    SERIAL_PORT = 'COM2'


class Cepko(object):
    """
    One instance of that object could be use for one or more
    queries to the serial port.
    """
    request_pattern = "<\n{}\n>"

    def get(self, key="", request_pattern=None):
        if request_pattern is None:
            request_pattern = self.request_pattern
        return CepkoResult(request_pattern.format(key))

    def all(self):
        return self.get()

    def meta(self, key=""):
        request_pattern = self.request_pattern.format("/meta/{}")
        return self.get(key, request_pattern)

    def global_context(self, key=""):
        request_pattern = self.request_pattern.format("/global_context/{}")
        return self.get(key, request_pattern)


class CepkoResult(object):
    """
    CepkoResult executes the request to the virtual serial port as soon
    as the instance is initialized and stores the result in both raw and
    marshalled format.
    """
    def __init__(self, request):
        self.request = request
        self.raw_result = self._execute()
        self.result = self._marshal(self.raw_result)

    def _execute(self):
        connection = serial.Serial(SERIAL_PORT)
        connection.write(self.request)
        return connection.readline().strip('\x04\n')

    def _marshal(self, input):
        try:
            return json.loads(input)
        except ValueError:
            return input

    def __len__(self):
        return self.result.__len__()

    def __getitem__(self, key):
        return self.result.__getitem__(key)

    def __contains__(self, item):
        return self.result.__contains__(item)

    def __iter__(self):
        return self.result.__iter__()
