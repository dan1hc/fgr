__all__ = (
    'Query',
    'QuerySortBy',
    )

import typing

from . import constants
from . import dtypes
from . import enums
from . import fields
from . import objects


class Constants(constants.PackageConstants):  # noqa

    pass


class QuerySortBy(objects.Object):
    """Simple specification for sorting Query results by field."""

    field: fields.Field[str]
    direction: fields.Field[str] = fields.Field(
        default=enums.SortDirection.asc.value,
        enum=enums.SortDirection,
        nullable=False,
        )


class Query(objects.Object):
    """
    Database agnostic query object.

    ---

    ### Usage

    Queries for `Objects` can be generated from their fields \
    using the following comparison operators:

    * `field_1_eq_filter = Object.field_1 == 'test_value_123'`
    * `field_1_ne_filter = Object.field_1 != 'test_value_123'`
    * `field_1_ge_filter = Object.field_1 >= 'test_value_123'`
    * `field_1_gt_filter = Object.field_1 > 'test_value_123'`
    * `field_1_le_filter = Object.field_1 <= 'test_value_123'`
    * `field_1_lt_filter = Object.field_1 < 'test_value_123'`

    And the following special operators:

    * `field_1_contains_filter = Object.field_1 << 'test_value_123'`
    * `field_1_similarity_filter = Object.field_1 % 'test_value_123'`
    * `field_1_similarity_filter_with_threshold = Object.field_1 % ('test_value_123', 0.8)`

    Queries may be chained together using the `&` and `|` bitwise \
    operators, corresponding to `and` and `or` clauses respectively.

    Additionally, the invert (`~`) operator may be prefixed to any \
    Query to match the opposite of any conditions specified \
    instead.

    Queries also support optional result limiting and sorting, which \
    can be specified by setting the 'sorting' and 'limit' fields.

    ---

    ### Example

    ```py
    query: Query = (
        (
            (Object.integer_field >= 1)
            | (Object.string_field % ('test', 0.75))
            )
        & ~(Object.list_field << 'test')
        )
    ```

    In the example above, the query would match any `Object` for which \
    the string `'test'` is `not` a member of `list_field` and for which \
    either the value for `integer_field` is greater than or equal to `1` \
    or the value for `string_field` is at least `75%` similar to `'test'`.

    """

    sorting: fields.Field[list[QuerySortBy]] = []  # type: ignore[assignment]
    limit: fields.Field[typing.Optional[int]] = None

    def __and__(self, other: typing.Self) -> 'AndQuery':
        return AndQuery(and_=[self, other])  # type: ignore[arg-type]

    def __or__(self, other: typing.Self) -> 'OrQuery':
        return OrQuery(or_=[self, other])  # type: ignore[arg-type]

    def __invert__(self) -> 'InvertQuery':
        return InvertQuery(invert=self)  # type: ignore[arg-type]


class QueryCondition(Query):
    """Base query filter."""

    field: fields.Field[str]


class SimilarQueryCondition(QueryCondition):
    """Filters where field is similar to value."""

    like: 'fields.Field[dtypes.Primitive]'
    threshold: fields.Field[typing.Optional[float]] = None


class ContainsQueryCondition(QueryCondition):
    """Filters where field contains value."""

    contains: 'fields.Field[dtypes.Primitive]'


class EqQueryCondition(QueryCondition):
    """Filters where == value."""

    eq: 'fields.Field[dtypes.Primitive]'


class NeQueryCondition(QueryCondition):
    """Filters where != value."""

    ne: 'fields.Field[dtypes.Primitive]'


class LeQueryCondition(QueryCondition):
    """Filters where <= value."""

    le: 'fields.Field[dtypes.Primitive]'


class LtQueryCondition(QueryCondition):
    """Filters where < value."""

    lt: 'fields.Field[dtypes.Primitive]'


class GeQueryCondition(QueryCondition):
    """Filters where >= value."""

    ge: 'fields.Field[dtypes.Primitive]'


class GtQueryCondition(QueryCondition):
    """Filters where > value."""

    gt: 'fields.Field[dtypes.Primitive]'


class AndQuery(Query):
    """Filters on all conditions."""

    and_: 'fields.Field[list[type[Query]]]'


class OrQuery(Query):
    """Filters on any condition."""

    or_: 'fields.Field[list[type[Query]]]'


class InvertQuery(Query):
    """Inverts the filter."""

    invert: 'fields.Field[type[Query]]'
