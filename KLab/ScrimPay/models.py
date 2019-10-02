from django.db import models

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
    user_name = models.CharField(max_length=20)

class Service(models.Model):
    # サービスID : Char型で、主キー
    service_id = models.CharField(max_length=30, primary_key=True)

    # サービス名 : Char型
    service_name = models.CharField(max_length=20)

    # プラン名 : Char型
    plan_name = models.CharField(max_length=20)

    # 月額料金 : Integer型
    fee_per_month = models.IntegerField()