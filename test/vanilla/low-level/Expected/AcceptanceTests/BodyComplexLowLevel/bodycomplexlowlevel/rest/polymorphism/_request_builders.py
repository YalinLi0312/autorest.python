# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types that are polymorphic.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "length": 0.0,
                "siblings": [
                    ...
                ],
                "species": "str",  # Optional.
                fishtype: fishtype
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/valid')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_put_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types that are polymorphic.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put a salmon that looks like this:
     {
             'fishtype':'Salmon',
             'location':'alaska',
             'iswild':true,
             'species':'king',
             'length':1.0,
             'siblings':[
               {
                 'fishtype':'Shark',
                 'age':6,
                 'birthday': '2012-01-05T01:00:00Z',
                 'length':20.0,
                 'species':'predator',
               },
               {
                 'fishtype':'Sawshark',
                 'age':105,
                 'birthday': '1900-01-05T01:00:00Z',
                 'length':10.0,
                 'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
                 'species':'dangerous',
               },
               {
                 'fishtype': 'goblin',
                 'age': 1,
                 'birthday': '2015-08-08T00:00:00Z',
                 'length': 30.0,
                 'species': 'scary',
                 'jawsize': 5
               }
             ]
           };.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put a salmon that looks like this:
     {
             'fishtype':'Salmon',
             'location':'alaska',
             'iswild':true,
             'species':'king',
             'length':1.0,
             'siblings':[
               {
                 'fishtype':'Shark',
                 'age':6,
                 'birthday': '2012-01-05T01:00:00Z',
                 'length':20.0,
                 'species':'predator',
               },
               {
                 'fishtype':'Sawshark',
                 'age':105,
                 'birthday': '1900-01-05T01:00:00Z',
                 'length':10.0,
                 'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
                 'species':'dangerous',
               },
               {
                 'fishtype': 'goblin',
                 'age': 1,
                 'birthday': '2015-08-08T00:00:00Z',
                 'length': 30.0,
                 'species': 'scary',
                 'jawsize': 5
               }
             ]
           };.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            fishtype = 'Salmon' or 'Shark'

            # JSON input template you can fill out and use as your body input.
            json = {
                "length": 0.0,
                "siblings": [
                    ...
                ],
                "species": "str",  # Optional.
                fishtype: fishtype
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/valid')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_dot_syntax_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types that are polymorphic, JSON key contains a dot.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "species": "str",  # Optional.
                fish.type: fish.type
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/dotsyntax')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_composed_with_discriminator_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex object composing a polymorphic scalar property and array property with polymorphic
    element type, with discriminator specified. Deserialization must NOT fail and use the
    discriminator type specified on the wire.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "fishes": [
                    {
                        "species": "str",  # Optional.
                        fish.type: fish.type
                    }
                ],
                "salmons": [
                    {
                        "iswild": bool,  # Optional.
                        "location": "str",  # Optional.
                        "species": "str",  # Optional.
                        fish.type: DotSalmon
                    }
                ],
                "sampleFish": {
                    "species": "str",  # Optional.
                    fish.type: fish.type
                },
                "sampleSalmon": {
                    "iswild": bool,  # Optional.
                    "location": "str",  # Optional.
                    "species": "str",  # Optional.
                    fish.type: DotSalmon
                }
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/composedWithDiscriminator')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_composed_without_discriminator_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex object composing a polymorphic scalar property and array property with polymorphic
    element type, without discriminator specified on wire. Deserialization must NOT fail and use
    the explicit type of the property.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "fishes": [
                    {
                        "species": "str",  # Optional.
                        fish.type: fish.type
                    }
                ],
                "salmons": [
                    {
                        "iswild": bool,  # Optional.
                        "location": "str",  # Optional.
                        "species": "str",  # Optional.
                        fish.type: DotSalmon
                    }
                ],
                "sampleFish": {
                    "species": "str",  # Optional.
                    fish.type: fish.type
                },
                "sampleSalmon": {
                    "iswild": bool,  # Optional.
                    "location": "str",  # Optional.
                    "species": "str",  # Optional.
                    fish.type: DotSalmon
                }
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/composedWithoutDiscriminator')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_complicated_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types that are polymorphic, but not at the root of the hierarchy; also have
    additional properties.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "iswild": bool,  # Optional.
                "length": 0.0,
                "location": "str",  # Optional.
                "siblings": [
                    {
                        "length": 0.0,
                        "siblings": [
                            ...
                        ],
                        "species": "str",  # Optional.
                        fishtype: fishtype
                    }
                ],
                "species": "str",  # Optional.
                fishtype: salmon
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/complicated')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_put_complicated_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
    additional properties.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            fishtype = 'SmartSalmon'

            # JSON input template you can fill out and use as your body input.
            json = {
                "iswild": bool,  # Optional.
                "length": 0.0,
                "location": "str",  # Optional.
                "siblings": [
                    {
                        "length": 0.0,
                        "siblings": [
                            ...
                        ],
                        "species": "str",  # Optional.
                        fishtype: fishtype
                    }
                ],
                "species": "str",  # Optional.
                fishtype: salmon
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/complicated')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_put_missing_discriminator_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types that are polymorphic, omitting the discriminator.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            fishtype = 'SmartSalmon'

            # JSON input template you can fill out and use as your body input.
            json = {
                "iswild": bool,  # Optional.
                "length": 0.0,
                "location": "str",  # Optional.
                "siblings": [
                    {
                        "length": 0.0,
                        "siblings": [
                            ...
                        ],
                        "species": "str",  # Optional.
                        fishtype: fishtype
                    }
                ],
                "species": "str",  # Optional.
                fishtype: salmon
            }

            # response body for status code(s): 200
            response.json() == {
                "iswild": bool,  # Optional.
                "length": 0.0,
                "location": "str",  # Optional.
                "siblings": [
                    {
                        "length": 0.0,
                        "siblings": [
                            ...
                        ],
                        "species": "str",  # Optional.
                        fishtype: fishtype
                    }
                ],
                "species": "str",  # Optional.
                fishtype: salmon
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/missingdiscriminator')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_put_valid_missing_required_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types that are polymorphic, attempting to omit required 'birthday' field - the
    request should not be allowed from the client.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please attempt put a sawshark that looks like this, the
     client should not allow this data to be sent:
     {
         "fishtype": "sawshark",
         "species": "snaggle toothed",
         "length": 18.5,
         "age": 2,
         "birthday": "2013-06-01T01:00:00Z",
         "location": "alaska",
         "picture": base64(FF FF FF FF FE),
         "siblings": [
             {
                 "fishtype": "shark",
                 "species": "predator",
                 "birthday": "2012-01-05T01:00:00Z",
                 "length": 20,
                 "age": 6
             },
             {
                 "fishtype": "sawshark",
                 "species": "dangerous",
                 "picture": base64(FF FF FF FF FE),
                 "length": 10,
                 "age": 105
             }
         ]
     }.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please attempt put a sawshark that looks like this, the
     client should not allow this data to be sent:
     {
         "fishtype": "sawshark",
         "species": "snaggle toothed",
         "length": 18.5,
         "age": 2,
         "birthday": "2013-06-01T01:00:00Z",
         "location": "alaska",
         "picture": base64(FF FF FF FF FE),
         "siblings": [
             {
                 "fishtype": "shark",
                 "species": "predator",
                 "birthday": "2012-01-05T01:00:00Z",
                 "length": 20,
                 "age": 6
             },
             {
                 "fishtype": "sawshark",
                 "species": "dangerous",
                 "picture": base64(FF FF FF FF FE),
                 "length": 10,
                 "age": 105
             }
         ]
     }.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            fishtype = 'Salmon' or 'Shark'

            # JSON input template you can fill out and use as your body input.
            json = {
                "length": 0.0,
                "siblings": [
                    ...
                ],
                "species": "str",  # Optional.
                fishtype: fishtype
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/complex/polymorphism/missingrequired/invalid')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )
