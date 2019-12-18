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

    def __str__(self):
        return self.user_id + ',' + self.service_id

    # 組み合わせが重複禁止
    class Meta:
        unique_together = ('user_id', 'service_id')

class User(models.Model):
    # ユーザーID : Char型で、主キー
    user_id = models.CharField(max_length=20, primary_key=True)

    # メールアドレス : Char型
    mail_address = models.CharField(max_length=100)

    # パスワード : Char型
    password = models.CharField(max_length=30)

    # ユーザー名 : Char型
    user_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user_id + ',' + self.mail_address + ',' + self.user_name

class Service(models.Model):
    # サービスID : Char型で、主キー
    service_id = models.CharField(max_length=30, primary_key=True)

    # サービス名 : Char型
    service_name = models.CharField(max_length=20)

    # プラン名 : Char型
    plan_name = models.CharField(max_length=20, null=True, blank=True)

    # 月額料金 : Integer型
    fee_per_month = models.IntegerField()

    # グラフ表示用の色コード : Char型
    color = models.CharField(max_length=10, null=True, blank=True)

    # プラン識別子 : Char型
    plan_identifier = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.service_id + ',' + self.service_name + ',' + str(self.fee_per_month)

class Genre(models.Model):
    # サービス ID : Char型で、主キー
    service_id = models.CharField(max_length=30, primary_key=True)

    # アニメの重み : Integer型
    anime_weight = models.IntegerField()

    # ドラマの重み : Integer型
    drama_weight = models.IntegerField()

    # 邦画の重み : Integer型
    japanese_movie_weight = models.IntegerField()

    # スポーツの重み : Integer型
    sports_weight = models.IntegerField()

    # バラエティーの重み : Integer型
    variety_weight = models.IntegerField()

    def __str__(self):
        return self.service_id