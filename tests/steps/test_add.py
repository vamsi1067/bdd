from behave import fixture
from behave import (
    given,
    when,
)

from tests.add_function import add

#
# scenario = partial(bdd_scenario, "test.feature")
#
#
# @scenario("As a user I want to sum 2 numbers {number} {number1}")
# def test_add(context):
#     """ Add """


# @fixture
# def result():
#     return {}


@given('A number')
def number(context,value1):
    print('abc')
    return value1


@given('Another number')
def another_number(context,value2):
    print('123')
    return value2


@fixture
@when('I want to compare the sum')
def when_sum(context):
    result = add(number(context,2),another_number(context,5))
    print('result {}'.format(result))

# @then('The sum matches')
# def sum_matches(context):
#     assert result['result'] == (number(context,number) + another_number(context,another_number))

