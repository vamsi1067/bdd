from behave import (
    when,
    then
)
from tests.preProcessing import filter_cols
import pandas as pd

@when('I get the values that are not allowred cert_ind {cert_ind}')
def notAllowredValues(context, cert_ind):
    List = [cert_ind]
    for item in List:
        print(item)
        if item == "empty":
            item.replace("empty", " ")
    return item
@then('validate not allowed values are removed')
def validatePreProcessing(context):
    df = pd.read_excel(r'/Users/vamsikrishnareddykapa/Desktop/Project/GitRepos/bdd/tests/steps/data_set.xlsx', engine='openpyxl')
    print("dataFrame: "+ str(df))
    NA=filter_cols(df,cert_ind,notAllowredValues)
    print(NA)