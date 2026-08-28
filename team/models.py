from django.db import models


class Player(models.Model):
    ROLE_CHOICES = [
        ('carry', 'Керри'),
        ('mid', 'Мидер'),
        ('support', 'Саппорт'),
        ('offlane', 'Оффлейнер'),
        ('igl', 'Капитан / IGL'),
        ('coach', 'Тренер'),
        ('analyst', 'Аналитик'),
    ]

    nickname = models.CharField(max_length=50, verbose_name='Никнейм')
    full_name = models.CharField(max_length=100, blank=True, verbose_name='Настоящее имя')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Роль')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    country = models.CharField(max_length=50, blank=True, verbose_name='Страна')
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст')
    bio = models.TextField(blank=True, verbose_name='О игроке')

    twitch = models.URLField(blank=True, verbose_name='Twitch')
    twitter = models.URLField(blank=True, verbose_name='Twitter / X')
    discord = models.CharField(max_length=50, blank=True, verbose_name='Discord')

    joined_date = models.DateField(blank=True, null=True, verbose_name='В команде с')
    is_active = models.BooleanField(default=True, verbose_name='В основном составе')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок на странице')

    class Meta:
        ordering = ['order', 'nickname']
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.nickname


class Match(models.Model):
    RESULT_CHOICES = [
        ('win', 'Победа'),
        ('loss', 'Поражение'),
        ('upcoming', 'Предстоящий'),
    ]

    opponent = models.CharField(max_length=100, verbose_name='Соперник')
    tournament = models.CharField(max_length=150, blank=True, verbose_name='Турнир')
    date = models.DateTimeField(verbose_name='Дата и время')
    result = models.CharField(max_length=10, choices=RESULT_CHOICES, default='upcoming', verbose_name='Результат')
    score = models.CharField(max_length=20, blank=True, verbose_name='Счёт')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    def __str__(self):
        return f'{self.opponent} — {self.date.strftime("%d.%m.%Y")}'
