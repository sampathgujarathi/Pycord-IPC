
import discord

if discord.version_info.major < 2:
    raise RuntimeError("You must have py-cord (v2.0 or greater) to use this library.")

__title__ = "Pycord-IPC"
__author__ = "Sampath"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__copyright__ = "Copyright (C) 2023 Sampath"
__version__ = "1.0.1"


from .errors import BaseException, NoEndpointFound, MulticastFailure, InvalidReturn, ServerAlreadyStarted
from .client import Client
from .server import Server
from .objects import ClientPayload, ServerResponse

