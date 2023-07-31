from fac_def import *
from variables import *

# change policy on/off depending on variables.policy_status
for policy_table in policy_tables:
    dbExecute("dbsafer3","update %s set enabled=0 where name like 'TC%%';"%policy_table)