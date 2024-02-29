__all__ = (
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
