import re
from rest_framework import serializers
from collections import defaultdict
import json
from operator import itemgetter
class phoneSerializer(serializers.Serializer):
    # 定义需要序列化的字段
    telephone = serializers.CharField()
    reg_info=serializers.DictField()
    check_time=serializers.CharField()
    # isreg = serializers.IntegerField()
    # 添加其他字段...

    def create(self, validated_data):
        # 创建和返回一个新对象
        pass

    def update(self, instance, validated_data):
        # 更新并返回现有对象
        pass
class NestedlistSerializer(serializers.ListSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['child']=phoneSerializer()
        super().__init__(*args, **kwargs)
    def to_representation(self, data):
        return [phoneSerializer(item).data for item in data]




def clear_dict_values(dictionary):
    for key in dictionary:
        
        dictionary[key] = '-'
        
def set_to_list(querysets):
    group_data=defaultdict(list)
    for set in querysets:
        set.reg_info = json.loads(set.reg_info.replace("'", '"'))
        set.reg_info.update({'create_time':set.check_time})
        group_data[set.check_time].append(set)
    
    sorted_data=sorted(group_data.items(),key=itemgetter(0),reverse=True)
    
    result=[data for _, data in sorted_data]
    return result

def validate_phone_number(phone_number):
    regex = r'^13[4-9]|14[7]|15[0-2,7-9]|16[2-3,5-9]|17[0-3,5-8]|18[0-9]|19[1,8,9]|13[0-2]|14[5]|15[5-6]|16[6]|17[1,5-6]|18[5-6]|13[3]|14[9]|15[3]|16[8-9]|17[3,7]|18[0-1,9]|19[1,9]$'
    if re.match(regex, phone_number) and phone_number.isdigit() :
        return True
    else :
        return False