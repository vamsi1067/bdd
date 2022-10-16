import pyspark.sql.functions as f


def add(num1, num2):
    value = num1 + num2
    valueCheck = value >= 5
    return value, valueCheck


def update_config(self, param, config_value):
    command = 'sudo sh -c "sed -i'
    command = command + " '/" + param + "/c\\" + param + "= " + config_value + " \\' {0}\""
    print(command)
    command = command.format(self.config_file)
    self.il_ssh.runcmd(command)


def to_str_replace_null(input_df, columns):
    return input_df.select([f.col(udf_input_col).cast("string") for udf_input_col in columns]).na.fill('NV')

#need to point
def filter_cols(input_df, column,values):
    return input_df

def userPreOrg(input_df, column,values):
    return input_df
