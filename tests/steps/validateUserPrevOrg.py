from behave import (
    when,
    then
)
from tests.preProcessing import filter_cols
import pandas as pd

@when('I get the user organisation privileges {userCol} orgCol {orgCol}')
def validateUserPrevOrg(context, userCol,orgCol):
    List = [userCol,orgCol]
    for item in List:
        print(item)
        if item == "empty":
            item.replace("empty", " ")
    return item
@then('validate user organisation privileges')
def validatePreProcessing(context):
    df = pd.read_excel(r'/Users/vamsikrishnareddykapa/Desktop/Project/GitRepos/bdd/tests/steps/data_set.xlsx', engine='openpyxl')
    print("dataFrame: "+ str(df))
    # point preprocessing.py
    NA=filter_cols(df,cert_ind,notAllowredValues)
    print(NA)