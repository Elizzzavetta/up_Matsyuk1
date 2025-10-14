from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    email = models.EmailField(verbose_name='Почта')
    cart_id = models.IntegerField(null=True, blank=True, verbose_name='Корзина')  # Если корзина может быть пустой
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, verbose_name='Телефон')  # Можно настроить длину под формат телефона
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    my_promotions_id = models.IntegerField(null=True, blank=True, verbose_name='Мои акции')  # Если акции могут быть пустыми

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    promotion_id = models.ForeignKey('Promotion', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Акции')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя {self.user}'


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='О товаре')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.CharField(max_length=100, verbose_name='Категория')
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    article = models.CharField(max_length=50, unique=True, verbose_name='Артикул')  # Уникальный артикул
    recommended_age = models.CharField(max_length=50, verbose_name='Рекомендуемый возраст')
    characteristics = models.TextField(verbose_name='Характеристики')
    reviews_id = models.IntegerField(null=True, blank=True, verbose_name='Отзывы')  # Если отзывы могут быть пустыми

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')  # Ссылка на модель Product
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')  # Ссылка на модель User
    rating = models.IntegerField(verbose_name='Оценка')  # Оценка от 1 до 5, например
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв на {self.product_id} от {self.user_id}'
