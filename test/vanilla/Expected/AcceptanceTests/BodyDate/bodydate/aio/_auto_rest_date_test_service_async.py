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

from ._configuration_async import AutoRestDateTestServiceConfiguration
from azure.core.exceptions import map_error
from .operations_async import DateModelOperations
from .. import models


class AutoRestDateTestService(object):
    """Test Infrastructure for AutoRest


    :ivar date_model: DateModel operations
    :vartype date_model: bodydate.aio.operations_async.DateModelOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestDateTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.date_model = DateModelOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
