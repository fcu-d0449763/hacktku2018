# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-31 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20180331_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='constellation',
            field=models.CharField(choices=[('Aquarius', '水瓶座'), ('Pisces', '雙魚座'), ('Aries', '牡羊座'), ('Taurus', '金牛座'), ('Gemini', '雙子座'), ('Cancer', '巨蟹座'), ('Leo', '獅子座'), ('Virgo', '處女座'), ('Libra', '天秤座'), ('Scorpio', '天蠍座'), ('Sagittarius', '射手座'), ('Capricorn', '摩羯座')], default='Capricorn', max_length=20, verbose_name='喜愛水果'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fruit',
            field=models.CharField(choices=[('apple', '蘋果'), ('watermelon', '西瓜'), ('peach', '桃子'), ('guava', '芭樂'), ('papaya', '木瓜'), ('cantaloup', '哈密瓜'), ('tomato', '蕃茄'), ('cherry', '櫻桃'), ('strawberry', '草莓'), ('pineapple', '鳳梨'), ('grape', '葡萄'), ('banana', '香蕉'), ('star_fruit', '楊桃'), ('lychee', '荔枝'), ('passion_fruit', '百香果'), ('kiwi', '奇異果'), ('mango', '芒果'), ('orange', '柳橙'), ('wax_apple', '蓮霧')], default='apple', max_length=20, verbose_name='喜愛水果'),
        ),
    ]
