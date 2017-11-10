from django.db import models


class UserInfo(models.Model):
    user = models.CharField('用户名', max_length=20, default='')
    name = models.CharField('真实姓名', max_length=20, default='')
    sex = models.CharField('性别', max_length=2, default='')
    idcard = models.CharField('身份证号', max_length=20, default='')
    org = models.CharField('单位', max_length=40, default='')
    subject = models.CharField('专业', max_length=20, default='')
    zhicheng = models.CharField('职称', max_length=20, default='')
    tele = models.CharField('电话号码', max_length=10, default='')
    email = models.CharField('邮箱', max_length=30, default='')
    adress = models.CharField('地址', max_length=40, default='')


class UserApply(models.Model):
    uid = models.ForeignKey(UserInfo)
    data_year = models.CharField('申请数据年份', max_length=10, default='')
    goal = models.CharField('申请目的', max_length=1000, default='')
    certificate = models.FileField('上传申请表')
    result_list = (
        ('审核中', '审核中'),
        ('审核通过', '审核通过'),
        ('审核未通过', '审核未通过')
    )
    result = models.CharField('申请结果', max_length=10, choices=result_list)
    apply_date = models.DateTimeField('申请时间', auto_now=True)
    check_date = models.DateTimeField('审核时间', auto_now=True)

class DataCass(models.Model):
    data_year = models.CharField('数据年份', max_length=10, default='')
    data_file1 = models.FileField('数据附件1')
    data_file2 = models.FileField('数据附件2')
    data_file3 = models.FileField('数据附件3')
    update_time = models.DateTimeField('更新时间')