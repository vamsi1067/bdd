from functools import partial
from behave import fixture
from behave import (
    scenario as bdd_scenario,
    given,
    when,
    then,
)

@given("I am the main directory")
def in_main_dir(context):
    print('abc abc')

@then("I should also be in the main directory")
def also_in_main_dir(context):
    pass

@given("I am in subdirectory of main directory")
def in_sub_dir(context):
    pass

@given("I am negative test in main steps")
def negative(context):
    pass