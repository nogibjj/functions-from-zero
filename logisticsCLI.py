#!/usr/bin/env python

from mylib.logistics import total_distance
import click

#build a click group
@click.group()
def cli():
    """Tool for calculating total distance between a list of cities"""

#build a click command
@cli.command("total")
def total():
    """Calculate the total distance between a list of cities"""
    print

#invoke the click command
if __name__ == "__main__":
    cli()

