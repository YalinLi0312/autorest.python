# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import (
    build_visibility_delete_model_request,
    build_visibility_get_model_request,
    build_visibility_head_model_request,
    build_visibility_patch_model_request,
    build_visibility_post_model_request,
    build_visibility_put_model_request,
)
from .._vendor import VisibilityClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VisibilityClientOperationsMixin(VisibilityClientMixinABC):

    @overload
    async def get_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def get_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def get_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    async def get_model(
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.VisibilityModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_get_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.VisibilityModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def head_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def head_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> bool:
        """head_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def head_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> bool:
        """head_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def head_model(self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any) -> bool:
        """head_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_head_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
        return 200 <= response.status_code <= 299

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_put_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_patch_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_post_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """

    @overload
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "createProp": [
                        "str"
                    ],
                    "deleteProp": bool,
                    "queryProp": 0,
                    "readProp": "str",
                    "updateProp": [
                        0
                    ]
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_delete_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
