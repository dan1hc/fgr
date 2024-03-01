__all__ = (
    'dataclass_transform',
    'Array',
    'BaseType',
    'Default',
    'Enum',
    'Field',
    'FieldType',
    'GenericType',
    'Immutable',
    'MetaType',
    'NoneType',
    'NumberType',
    'Primitive',
    'RePatternDict',
    'Query',
    'Serial',
    'SupportsFields',
    'Type',
    'ValidLogType',
    )

import collections
import decimal
import enum
import re
import sys
import types
import typing

if typing.TYPE_CHECKING:
    from .. import _fields
    from .. import fields
    from .. import meta
    from .. import query

from . import constants
from . import utils


class Constants(constants.TypeConstants):  # noqa

    pass


T = typing.TypeVar('T')
Default = typing.TypeVar('Default')
Type = typing.TypeVar('Type', bound=type[typing.Any])
BaseType = typing.TypeVar('BaseType', bound='meta.Base')
MetaType = typing.TypeVar('MetaType', bound='meta.Meta')
GenericType = typing.TypeVar('GenericType', bound=typing.Any)
Array = typing.Union[
    collections.deque,
    frozenset,
    list,
    set,
    tuple,
    ]
Enum = typing.Union[
    enum.EnumMeta,
    Array
    ]
Container = typing.Union[
    Array,
    collections.OrderedDict,
    collections.defaultdict,
    dict,
    ]
FieldType = typing.Union[
    '_fields.Field',
    'fields.Field'
    ]
NoneType = None.__class__
NumberType = typing.Union[
    decimal.Decimal,
    float,
    int,
    ]
Primitive = typing.Union[
    bool,
    bytes,
    float,
    int,
    str,
    ]
Serial = typing.Union[
    Primitive,
    dict,
    list
    ]
Immutable = typing.Union[
    Primitive,
    enum.EnumMeta,
    frozenset,
    tuple,
    ]
Query = typing.Union[
    'query.Query',
    'query.QueryCondition',
    'query.AndQuery',
    'query.OrQuery',
    'query.InvertQuery',
    'query.ContainsQueryCondition',
    'query.EqQueryCondition',
    'query.NeQueryCondition',
    'query.LeQueryCondition',
    'query.LtQueryCondition',
    'query.GeQueryCondition',
    'query.GtQueryCondition',
    ]
ValidLogType = typing.Union[
    str,
    dict,
    'meta.Base',
    'meta.Meta'
    ]


class SupportsFields(typing.Protocol):
    """Meta protocol."""

    if typing.TYPE_CHECKING:
        __fields__: typing.ClassVar[typing.Mapping[str, FieldType]] = {}
        __heritage__: typing.ClassVar[tuple[type['meta.Base'], ...]] = ()
        __cache__: typing.ClassVar[dict[str, typing.Any]] = {}

        description: typing.ClassVar[str] = Constants.UNDEFINED
        distribution: typing.ClassVar[str] = Constants.UNDEFINED
        enumerations: typing.ClassVar[dict[str, list]] = {}
        fields: typing.ClassVar[tuple[str, ...]] = ()
        hash_fields: typing.ClassVar[tuple[str, ...]] = ()
        reference: typing.ClassVar[str] = Constants.UNDEFINED
        is_snake_case: typing.ClassVar[bool] = True
        isCamelCase: typing.ClassVar[bool] = False


class Field(types.GenericAlias):
    """Generic alias type."""

    def __repr__(self) -> str:
        ftypes = typing.get_args(self)
        _delim = (
            ' | '
            if isinstance(self, typing._UnionGenericAlias)  # type: ignore[attr-defined]
            else ', '
            )
        _ftypes = _delim.join(
            (
                getattr(t, '__name__', 'Any')
                for t
                in ftypes
                )
            )
        return f'Field[{_ftypes}]'


class RePatternDict(typing.TypedDict):

    ID: str
    Severity: str
    Title: str
    Regex: re.Pattern


if sys.version_info < (3, 11):


    def dataclass_transform(  # pragma: no cover
        *,
        eq_default: bool = True,
        order_default: bool = False,
        kw_only_default: bool = False,
        frozen_default: bool = False,
        field_specifiers: tuple[type[typing.Any] | typing.Callable[..., typing.Any], ...] = (),  # noqa
        **kwargs: typing.Any,
        ) -> typing.Callable[[SupportsFields], SupportsFields]:
        """Decorator to mark an object as providing dataclass-like behaviour.

        The decorator can be applied to a function, class, or metaclass.

        Example usage with a decorator function::

            @dataclass_transform()
            def create_model[T](cls: type[T]) -> type[T]:
                ...
                return cls

            @create_model
            class CustomerModel:
                id: int
                name: str

        On a base class::

            @dataclass_transform()
            class ModelBase: ...

            class CustomerModel(ModelBase):
                id: int
                name: str

        On a metaclass::

            @dataclass_transform()
            class ModelMeta(type): ...

            class ModelBase(metaclass=ModelMeta): ...

            class CustomerModel(ModelBase):
                id: int
                name: str

        The ``CustomerModel`` classes defined above will
        be treated by type checkers similarly to classes created with
        ``@dataclasses.dataclass``.
        For example, type checkers will assume these classes have
        ``__init__`` methods that accept ``id`` and ``name``.

        The arguments to this decorator can be used to customize this behavior:
        - ``eq_default`` indicates whether the ``eq`` parameter is assumed to be
            ``True`` or ``False`` if it is omitted by the caller.
        - ``order_default`` indicates whether the ``order`` parameter is
            assumed to be True or False if it is omitted by the caller.
        - ``kw_only_default`` indicates whether the ``kw_only`` parameter is
            assumed to be True or False if it is omitted by the caller.
        - ``frozen_default`` indicates whether the ``frozen`` parameter is
            assumed to be True or False if it is omitted by the caller.
        - ``field_specifiers`` specifies a static list of supported classes
            or functions that describe fields, similar to ``dataclasses.field()``.
        - Arbitrary other keyword arguments are accepted in order to allow for
            possible future extensions.

        At runtime, this decorator records its arguments in the
        ``__dataclass_transform__`` attribute on the decorated object.
        It has no other runtime effect.

        See PEP 681 for more details.
        """
        def decorator(cls_or_fn: SupportsFields) -> SupportsFields:  # noqa
            cls_or_fn.__dataclass_transform__ = {  # type: ignore[attr-defined]
                "eq_default": eq_default,
                "order_default": order_default,
                "kw_only_default": kw_only_default,
                "frozen_default": frozen_default,
                "field_specifiers": field_specifiers,
                "kwargs": kwargs,
                }
            return cls_or_fn
        return decorator


else:  # pragma: no cover

    from typing import dataclass_transform
