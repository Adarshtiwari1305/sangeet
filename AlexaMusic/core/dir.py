#
# Copyright (C) 2021-2022 by Adriti_fed@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Hitler Indian Largest Chatting Group

# Kanged By © @shaitaan_baccha
# Hitler © @aadriti_fed
# Owner Adarsh tiwari
# 
# All rights reserved. © Alisha © Alexa © Yukki


import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
