from django.db import models



class Poll(models.Model):
    question = models.TextField(max_length=300, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return "{}. {}".format(self.pk, self.question)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='polls',
                                on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.TextField(max_length=40,null=False, blank=False, verbose_name='Комментарий')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

