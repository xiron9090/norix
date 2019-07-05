# -*- coding: utf-8 -*-

"""
norix.socialnetworks.nxsocialnetworks
~~~~~~~~~~~~~~~~~

This module contains abstract class for to publish in social networks.
"""
# Use of this source code is governed by the apache license.
__license__ = "Apache"


class NXSocialNetworks:
    def __init__(self):
        raise NotImplementedError("This method will be implemented")

    def getcredential(self):
        raise NotImplementedError("This method will be implemented")

    def publish(self, **kwargs):
        raise NotImplementedError("This method will be implemented")
