from typing import Any
from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['location', 'dating_sex', 'min_distance', 'max_distance', 'min_dating_age',
                  'max_dating_age', 'vibration', 'only_match', 'auto_play']

    # 对需要判断的字段进行逻辑判断，只需要在clean_加上需要判断的字段名称， 返回
    # 清洗过的数据
    def clean_max_distance(self):
        cleaned_data = super().clean()
        if cleaned_data['min_distance'] > cleaned_data['max_distance']:
            raise forms.ValidationError('最小距离min_distance 不能大于 最大距离 max_distance')
        return cleaned_data['max_distance']
    
    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        if cleaned_data['min_dating_age'] > cleaned_data['max_dating_age']:
            raise forms.ValidationError('最小年龄 min_dating_agee 不能大于 最大年龄 max_dating_age')
        return cleaned_data['max_dating_age']