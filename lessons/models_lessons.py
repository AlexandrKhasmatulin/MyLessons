
from django.db import models


NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class Course(models.Model):
    #id = models.AutoField(verbose_name='ID курса')
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(max_length=500, verbose_name='Описание курса')
    preview = models.ImageField(upload_to='users/', verbose_name='превью', **NULLABLE)


    def __str__(self):
        return f'{self.course_name} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, default='1')
    lesson_name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(max_length=500, verbose_name='Описание урока')
    preview = models.ImageField(upload_to='users/', verbose_name='превью', **NULLABLE)
    linkvideo = models.URLField(verbose_name='превью', **NULLABLE)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, default='1')
    def __str__(self):
        return f'{self.lesson_name} {self.description}'

    class Meta:
        verbose_name = 'Урок '
        verbose_name_plural = 'Уроки'

class Payments(models.Model):
    user = models.CharField(max_length=150, verbose_name='Пользователь')
    date_of_payment = models.CharField(max_length=30, verbose_name='Дата Платежа')
    paid_lesson = models.ForeignKey("Lesson", on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    paid_course = models.ForeignKey("Course", on_delete=models.CASCADE, verbose_name='Оплаченый курс', **NULLABLE)
    amount_of_payment = models.IntegerField(verbose_name='Сумма оплаты', **NULLABLE)
    way_of_payment = models.CharField(max_length=150, verbose_name='Способ оплаты', **NULLABLE)
    def __str__(self):
        return f'{self.date_of_payment} {self.amount_of_payment}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

class Mailing(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема письма", **NULLABLE)
    content = models.TextField(verbose_name='Содержимое письма', **NULLABLE)


    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"{self.title}"


