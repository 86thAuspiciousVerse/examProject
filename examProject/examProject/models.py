from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 电影分类
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")
    description = models.TextField(blank=True, verbose_name="分类描述")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "电影分类"
        verbose_name_plural = "电影分类"

# 电影信息
class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="电影标题")
    description = models.TextField(verbose_name="电影描述")
    director = models.CharField(max_length=100, verbose_name="导演")
    actors = models.TextField(verbose_name="主演")
    release_date = models.DateField(verbose_name="上映日期")
    duration = models.IntegerField(verbose_name="时长(分钟)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    rating = models.FloatField(default=0, verbose_name="评分")
    poster = models.ImageField(upload_to='movie_posters/', verbose_name="海报", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "电影信息"
        verbose_name_plural = "电影信息"

# 用户收藏
class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="电影")
    collected_at = models.DateTimeField(auto_now_add=True, verbose_name="收藏时间")
    
    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = "用户收藏"
        unique_together = ('user', 'movie')

# 电影评论
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="电影")
    content = models.TextField(verbose_name="评论内容")
    rating = models.IntegerField(default=5, verbose_name="评分(1-5)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    
    class Meta:
        verbose_name = "电影评论"
        verbose_name_plural = "电影评论"

# 用户分享
class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="电影")
    share_text = models.TextField(verbose_name="分享内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="分享时间")
    
    class Meta:
        verbose_name = "用户分享"
        verbose_name_plural = "用户分享"