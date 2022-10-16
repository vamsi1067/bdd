from behave import (
    when,
    then
)
from tests.add_function import to_str_replace_null
import pandas as pd

@when('I get the empty field in the dataframe field userId {userId} ssId {ssId}')
def when_emptyString(context, userId,ssId):
    List = [userId, ssId]
    for item in List:
        print(item)
        if item == "empty":
            item.replace("empty", " ")
    return item
@then('validate empty string field is updated with NV')
def validatePreProcessing(context):
    df = pd.read_excel(r'/Users/vamsikrishnareddykapa/Desktop/Project/GitRepos/bdd/tests/steps/data_set.xlsx', engine='openpyxl')
    print("dataFrame: "+ str(df))
    NA=to_str_replace_null(df,when_emptyString)
    print(NA)