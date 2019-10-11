from django.db import models
from django.core import validators

# Create your models here.
class Main(models.Model):
    # ID : Integer型で、主キー 下記内容が自動追加される
    # 参考 : https://djangoproject.jp/doc/ja/1.0/topics/db/models.html
    # id = models.AutoField(primary_key=True)

    # ユーザーID : Char型で、外部キー
    user_id = models.CharField(max_length=20)

    # サービスID : Char型で、外部キー
    service_id = models.CharField(max_length=30)



class User(models.Model):
    # ユーザーID : Char型で、主キー
    user_id = models.CharField(max_length=20, primary_key=True)

    # メールアドレス : Char型
    mail_address = models.CharField(max_length=100)

    # パスワード : Char型
    password = models.CharField(max_length=30)

    # ユーザー名 : Char型
    user_name = models.CharField(max_length=20, null=True, blank=True)

class Service(models.Model):
    # サービスID : Char型で、主キー
    service_id = models.CharField(max_length=30, primary_key=True)

    # サービス名 : Char型
    service_name = models.CharField(max_length=20)

    # プラン名 : Char型
    plan_name = models.CharField(max_length=20, null=True, blank=True)

    # 月額料金 : Integer型
    fee_per_month = models.IntegerField()

"""
class Item(models.Model):
    service_name1 : models.BooleanField(verbose_name="Amazon Prime(月額)")
    service_name2 : models.BooleanField(verbose_name="Amazon Prime(年額)")
    service_name3 : models.BooleanField(verbose_name="Amazon Prime Prime student(月額)")
    service_name4 : models.BooleanField(verbose_name="Amazon Prime Prime student(年額)")
    service_name5 : models.BooleanField(verbose_name="Hulu(月額)")
    service_name6 : models.BooleanField(verbose_name="Netflix(ベーシック)")
    service_name7 : models.BooleanField(verbose_name="Netflix(スタンダード)")
    service_name8 : models.BooleanField(verbose_name="Netflix(プレミアム)")
    service_name9 : models.BooleanField(verbose_name="U-NEXT")
    service_name10 : models.BooleanField(verbose_name="dTV")
    service_name11 : models.BooleanField(verbose_name="dアニメストア")
    service_name12 : models.BooleanField(verbose_name="Youtube Premioum(一般)")
    service_name13 : models.BooleanField(verbose_name="Youtube Premioum(iOS版)")
    service_name14 : models.BooleanField(verbose_name="Youtube Premioum(ファミリー)")
    service_name15 : models.BooleanField(verbose_name="Youtube Premioum(学割)")
    service_name16 : models.BooleanField(verbose_name="DAZN(一般)")
    service_name17 : models.BooleanField(verbose_name="DAZN(DAZN for docomo)")
    service_name18 : models.BooleanField(verbose_name="DAZN(スマホナビ割)")
    service_name19 : models.BooleanField(verbose_name="Abemaプレミアム")
    service_name20 : models.BooleanField(verbose_name="ビデオパス")
    service_name21 : models.BooleanField(verbose_name="FOD(FODプレミアム)")
    service_name22 : models.BooleanField(verbose_name="FOD(ネクストsmart)")
    service_name23 : models.BooleanField(verbose_name="FOD(ワンツーsmart)")
    service_name24 : models.BooleanField(verbose_name="FOD(ワンツーネクストsmart)")
    service_name25 : models.BooleanField(verbose_name="Paravi")
    service_name26 : models.BooleanField(verbose_name="TSUTAYA TV(見放題プラン)")
    service_name27 : models.BooleanField(verbose_name="TSUTAYA TV(動画見放題+定額レンタル8)")
    service_name28 : models.BooleanField(verbose_name="ビデオマーケット(プレミアムコース)")
    service_name29 : models.BooleanField(verbose_name="ビデオマーケット(プレミアム&見放題コース)")
                    #service_name10 : models.BooleanField
"""
