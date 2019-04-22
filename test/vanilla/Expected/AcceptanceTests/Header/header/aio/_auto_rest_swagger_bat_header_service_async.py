# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import AutoRestSwaggerBATHeaderServiceConfiguration
from .operations_async import HeaderOperations
from .. import models


class AutoRestSwaggerBATHeaderService(AsyncPipelineClient):
    """Test Infrastructure for AutoRest


    :ivar header: Header operations
    :vartype header: header.aio.operations_async.HeaderOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestSwaggerBATHeaderServiceConfiguration(**kwargs)
        super(AutoRestSwaggerBATHeaderService, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.header = HeaderOperations(
            self, self._config, self._serialize, self._deserialize)
