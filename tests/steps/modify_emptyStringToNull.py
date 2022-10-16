from behave import (
    when,
    then
)
from tests.preProcessing import to_str_replace_null
import pandas as pd

@when('I get the empty field in the dataframe field userId {userId} ssId {ssId} {resource_seq} {entl_seq} {cert_ind} {job_desc}')
def when_emptyString(context, userId,ssId,resource_seq,entl_seq,cert_ind,job_desc):
    List = [userId, ssId,resource_seq,entl_seq,cert_ind,job_desc]
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