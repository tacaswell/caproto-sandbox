#!/usr/bin/env python3
from caproto.threading.client import Context
prefix='NIH:DI245.'
ctx = Context()
counter, = ctx.get_pvs(prefix+'counter')
update_time, = ctx.get_pvs(prefix+'update_time')
