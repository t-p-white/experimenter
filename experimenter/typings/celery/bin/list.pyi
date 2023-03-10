"""
This type stub file was generated by pyright.
"""

import click
from celery.bin.base import CeleryCommand, handle_preload_options

"""The ``celery list bindings`` command, used to inspect queue bindings."""

@click.group(name="list")
@click.pass_context
@handle_preload_options
def list_(ctx):  # -> None:
    """Get info from broker.

    Note:

        For RabbitMQ the management plugin is required.
    """
    ...

@list_.command(cls=CeleryCommand)
@click.pass_context
def bindings(ctx):  # -> None:
    """Inspect queue bindings."""
    ...