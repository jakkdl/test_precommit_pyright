# AUTOFIX
# NOANYIO # TODO
# ARG --enable=TRIO100,TRIO911
from typing import Any

import trio


# fmt: off
async def foo_no_noqa():
    with trio.fail_after(5):  # TRIO100: 9, 'trio', 'fail_after'
        yield  # TRIO911: 8, "yield", Statement("function definition", lineno-2)
    await trio.lowlevel.checkpoint()


async def foo_noqa_bare():
    with trio.fail_after(5):  # noqa
        yield  # noqa
    await trio.lowlevel.checkpoint()


async def foo_noqa_100():
    with trio.fail_after(5):  # noqa: TRIO100
        yield  # TRIO911: 8, "yield", Statement("function definition", lineno-2)
    await trio.lowlevel.checkpoint()


async def foo_noqa_911():
    with trio.fail_after(5):  # TRIO100: 9, 'trio', 'fail_after'
        yield  # noqa: TRIO911
    await trio.lowlevel.checkpoint()


async def foo_noqa_100_911():
    with trio.fail_after(5):  # noqa: TRIO100, TRIO911
        yield  # noqa: TRIO911
    await trio.lowlevel.checkpoint()


async def foo_noqa_100_911_500():
    with trio.fail_after(5):  # noqa: TRIO100, TRIO911 , TRIO500,,,
        yield  # noqa: TRIO100, TRIO911 , TRIO500,,,
    await trio.lowlevel.checkpoint()
# fmt: on

# check that noqas work after line numbers have been modified in a different visitor

# this will remove one line
with trio.fail_after(5):  # TRIO100: 5, 'trio', 'fail_after'
    ...


async def foo_changed_lineno():
    yield  # noqa: TRIO911
    await trio.lowlevel.checkpoint()


# this will add two lines
async def foo_changing_lineno():  # TRIO911: 0, "exit", Statement("yield", lineno+1)
    yield  # TRIO911: 4, "yield", Statement("function definition", lineno-1)


with trio.fail_after(5):  # noqa: TRIO100
    ...
