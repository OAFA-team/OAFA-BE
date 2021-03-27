from django.db import models

# Create your models here.


class Case(models.Model):
    CASE_CATEGORY_CORRUPTION = 1
    CASE_CATEGORY_BRIBE_TAKING = 2
    CASE_CATEGORY_SELLING_TRADE_SECRETS = 3
    CASE_CATEGORY_ROUTINE_INSPECTION = 4

    CASE_CATEGORY_CHOICES = (
        (CASE_CATEGORY_CORRUPTION, '贪污'),
        (CASE_CATEGORY_BRIBE_TAKING, '受贿'),
        (CASE_CATEGORY_SELLING_TRADE_SECRETS, '出卖商业机密'),
        (CASE_CATEGORY_ROUTINE_INSPECTION, '日常检查'),
    )

    class Meta:
        verbose_name = '案件'
        verbose_name_plural = '案件'

    name = models.CharField(verbose_name='项目名称', max_length=64)
    category = models.PositiveSmallIntegerField(
        verbose_name='案件类别',
        choices=CASE_CATEGORY_CHOICES,
        default=CASE_CATEGORY_ROUTINE_INSPECTION)
    create_time = models.DateTimeField(verbose_name='创建时间',
                                       auto_now_add=True)
    description = models.TextField(verbose_name='活动描述', default='')
