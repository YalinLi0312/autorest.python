# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import decimal
from typing import Any, Dict, List, Literal, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field
from ._enums import ExtendedEnum

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class BooleanLiteralProperty(_model_base.Model):
    """Model with a boolean literal property.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Default value is True.
    :vartype property: bool
    """

    property: Literal[True] = rest_field()
    """Property. Required. Default value is True."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: Literal[True] = True


class BooleanProperty(_model_base.Model):
    """Model with a boolean property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: bool
    """

    property: bool = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: bool,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class BytesProperty(_model_base.Model):
    """Model with a bytes property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: bytes
    """

    property: bytes = rest_field(format="base64")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: bytes,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsIntProperty(_model_base.Model):
    """Model with collection int properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: list[int]
    """

    property: List[int] = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: List[int],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsModelProperty(_model_base.Model):
    """Model with collection model properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: list[~typetest.property.valuetypes.models.InnerModel]
    """

    property: List["_models.InnerModel"] = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: List["_models.InnerModel"],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsStringProperty(_model_base.Model):
    """Model with collection string properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: list[str]
    """

    property: List[str] = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: List[str],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DatetimeProperty(_model_base.Model):
    """Model with a datetime property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: ~datetime.datetime
    """

    property: datetime.datetime = rest_field(format="rfc3339")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: datetime.datetime,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Decimal128Property(_model_base.Model):
    """Model with a decimal128 property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: ~decimal.Decimal
    """

    property: decimal.Decimal = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: decimal.Decimal,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DecimalProperty(_model_base.Model):
    """Model with a decimal property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: ~decimal.Decimal
    """

    property: decimal.Decimal = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: decimal.Decimal,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DictionaryStringProperty(_model_base.Model):
    """Model with dictionary string properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: dict[str, str]
    """

    property: Dict[str, str] = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Dict[str, str],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DurationProperty(_model_base.Model):
    """Model with a duration property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: ~datetime.timedelta
    """

    property: datetime.timedelta = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: datetime.timedelta,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class EnumProperty(_model_base.Model):
    """Model with enum properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Known values are: "ValueOne" and "ValueTwo".
    :vartype property: str or ~typetest.property.valuetypes.models.FixedInnerEnum
    """

    property: Union[str, "_models.FixedInnerEnum"] = rest_field()
    """Property. Required. Known values are: \"ValueOne\" and \"ValueTwo\"."""

    @overload
    def __init__(
        self,
        *,
        property: Union[str, "_models.FixedInnerEnum"],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ExtensibleEnumProperty(_model_base.Model):
    """Model with extensible enum properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Known values are: "ValueOne" and "ValueTwo".
    :vartype property: str or ~typetest.property.valuetypes.models.InnerEnum
    """

    property: Union[str, "_models.InnerEnum"] = rest_field()
    """Property. Required. Known values are: \"ValueOne\" and \"ValueTwo\"."""

    @overload
    def __init__(
        self,
        *,
        property: Union[str, "_models.InnerEnum"],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FloatLiteralProperty(_model_base.Model):
    """Model with a float literal property.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Default value is 43.125.
    :vartype property: float
    """

    property: float = rest_field()
    """Property. Required. Default value is 43.125."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: float = 43.125


class FloatProperty(_model_base.Model):
    """Model with a float property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: float
    """

    property: float = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: float,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InnerModel(_model_base.Model):
    """Inner model. Will be a property type for ModelWithModelProperties.

    All required parameters must be populated in order to send to server.

    :ivar property: Required string property. Required.
    :vartype property: str
    """

    property: str = rest_field()
    """Required string property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class IntLiteralProperty(_model_base.Model):
    """Model with a int literal property.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Default value is 42.
    :vartype property: int
    """

    property: Literal[42] = rest_field()
    """Property. Required. Default value is 42."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: Literal[42] = 42


class IntProperty(_model_base.Model):
    """Model with a int property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: int
    """

    property: int = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: int,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ModelProperty(_model_base.Model):
    """Model with model properties.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: ~typetest.property.valuetypes.models.InnerModel
    """

    property: "_models.InnerModel" = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: "_models.InnerModel",  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NeverProperty(_model_base.Model):
    """Model with a property never. (This property should not be included)."""


class StringLiteralProperty(_model_base.Model):
    """Model with a string literal property.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Default value is "hello".
    :vartype property: str
    """

    property: Literal["hello"] = rest_field()
    """Property. Required. Default value is \"hello\"."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: Literal["hello"] = "hello"


class StringProperty(_model_base.Model):
    """Model with a string property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: str
    """

    property: str = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionEnumValueProperty(_model_base.Model):
    """Template type for testing models with specific properties. Pass in the type of the property you
    are looking for.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: str or ~typetest.property.valuetypes.models.ENUM_VALUE2
    """

    property: Literal[ExtendedEnum.ENUM_VALUE2] = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Literal[ExtendedEnum.ENUM_VALUE2],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionFloatLiteralProperty(_model_base.Model):
    """Model with a union of float literal as property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Is either a float type or a float type.
    :vartype property: float or float
    """

    property: float = rest_field()
    """Property. Required. Is either a float type or a float type."""

    @overload
    def __init__(
        self,
        *,
        property: float,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionIntLiteralProperty(_model_base.Model):
    """Model with a union of int literal as property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Is either a Literal[42] type or a Literal[43] type.
    :vartype property: int or int
    """

    property: Literal[42, 43] = rest_field()
    """Property. Required. Is either a Literal[42] type or a Literal[43] type."""

    @overload
    def __init__(
        self,
        *,
        property: Literal[42, 43],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionStringLiteralProperty(_model_base.Model):
    """Model with a union of string literal as property.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required. Is either a Literal["hello"] type or a Literal["world"]
     type.
    :vartype property: str or str
    """

    property: Literal["hello", "world"] = rest_field()
    """Property. Required. Is either a Literal[\"hello\"] type or a Literal[\"world\"] type."""

    @overload
    def __init__(
        self,
        *,
        property: Literal["hello", "world"],  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnknownArrayProperty(_model_base.Model):
    """Model with a property unknown, and the data is an array.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnknownDictProperty(_model_base.Model):
    """Model with a property unknown, and the data is a dictionnary.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnknownIntProperty(_model_base.Model):
    """Model with a property unknown, and the data is a int32.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnknownStringProperty(_model_base.Model):
    """Model with a property unknown, and the data is a string.

    All required parameters must be populated in order to send to server.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field()
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
