# timod

Library for creating ThingsDB modules using the Python language

## Installation

```shell
$ pip install py-timod
```

## Usage

Modules for ThingsDB read from `stdin` and write a response back to `stdout`. Work by the module must be non-blocking.

If the module requires configuration data, for example a connection string, then this configuration will be send immediately after start-up but may be received again when the module configuration is changed in ThingsDB.

Do not use functions like `print` since these function will write to `stdout` and this is reserved for ThingsDB. Instead, use `logging...` to write to `stderr` instead.

The following code may be used as a template: (see: https://github.com/thingsdb/ThingsDB/tree/master/modules/python/demo)

```python
import logging
from timod import start_module, TiHandler, LookupError


class Handler(TiHandler):

    async def on_error(self, e):
        logging.error(e)

    async def on_config(self, cfg):
        logging.info(cfg)

    async def on_request(self, req):
        if 'message' not in req:
            raise LookupError('missing `message` in request')

        return req['message']


if __name__ == '__main__':
    start_module('demo', Handler())
```


