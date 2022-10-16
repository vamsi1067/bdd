from behave import (
    when,
    then
)
from tests.preProcessing import append_hierarchical_manager
import pandas as pd

@when('I get the hierarchical manager level {level} userId {userId} ssId {ssId}')
def hierarchicalMang(context, level, userId,ssId):
    List = [level,userId, ssId]
    for item in List:
        print(item)
        if item == "empty":
            item.replace("empty", " ")
    return item
@then('Validate hierarchical manager data')
def validatePreProcessing(context):
    df = pd.read_excel(r'/Users/vamsikrishnareddykapa/Desktop/Project/GitRepos/bdd/tests/steps/data_set.xlsx', engine='openpyxl')
    print("dataFrame: "+ str(df))
    # point preprocessing.py
    NA=append_hierarchical_manager(df,hierarchicalMang)
    print(NA)