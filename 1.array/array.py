# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 10:29
# @Author  : lenny
# @desc    :


test_str = "01:03"

item1, item2 = test_str.split(":")
if int(item1) != 23:
    min_after = str(int(item1) + 1)
    if len(min_after) == 1:
        min_after = "0" + min_after
else:
    min_after = "00"

print(min_after + ":" + item2)

haha = {
    "name": "cptest1",
    "dbinstance_id": "60ac7efa-f7ee-49c4-814d-d1ce5e32754f",
    "schedule_type": "scheduled",
    "device_type": "AnyBackup",
    "data_cycle": "1month",
    "backup_policy_way": "B0",
    "description": "xxx",
    "backup_log_create": True,
    "full_freq": "1week",
    "backup_time": "17:03",
    "backup_days": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
    ],
    "backup_full_create": True,
    "cum_data_schedules": []
}
