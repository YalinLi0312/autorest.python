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

from ._configuration_async import AutoRestParameterFlatteningConfiguration
from msrest.exceptions import HttpOperationError
from .operations_async import AvailabilitySetsOperations
from .. import models


class AutoRestParameterFlattening(AsyncPipelineClient):
    """Resource Flattening for AutoRest


    :ivar availability_sets: AvailabilitySets operations
    :vartype availability_sets: parameterflattening.aio.operations_async.AvailabilitySetsOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestParameterFlatteningConfiguration(**kwargs)
        super(AutoRestParameterFlattening, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.availability_sets = AvailabilitySetsOperations(
            self, self._config, self._serialize, self._deserialize)
