"""Sub-command for listing all topologies running on a Storm cluster.
"""
from __future__ import absolute_import

from pyleus.cli.commands.subcommand import SubCommand
from pyleus.cli.topologies import add_storm_cluster_ip_argument
from pyleus.cli.topologies import list_topologies


class ListSubCommand(SubCommand):
    """List subcommand class"""

    NAME = "list"
    DESCRIPTION = "List all topologies running on a Storm cluster"

    def add_arguments(self, parser):
        add_storm_cluster_ip_argument(parser)

    def run(self, configs):
        list_topologies(configs)
