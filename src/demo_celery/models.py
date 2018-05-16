from django.db import models


STATUS_TODO = (
    (0, '等待中'),
    (1, '运行中'),
    (2, '完成'),
    (3, '错误'),
    (4, '其它'),
)

class Todo(models.Model):
    ''' celery调度的任务 '''

    title = models.CharField(max_length=128, verbose_name='标题')
    status = models.IntegerField(
        choices=STATUS_TODO, verbose_name='状态', default=0,
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    remark = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return self.title

    def to_json(self):
        info = {
            'id': self.id,
            'title': self.title,
            'status': self.get_status_display(),
            'create_time': self.create_time.isoformat(),
            'update_time': self.update_time.isoformat(),
            'remark': self.remark,
        }
        return info



class TodoSpider(models.Model):
    ''' 网站下载 '''

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    url = models.URLField()
    filename = models.FileField()
    status = models.IntegerField(
        choices=STATUS_TODO, verbose_name='状态', default=0,
    )

# 首页
#             运行中
# 首页上的链接20个
#             等待中

