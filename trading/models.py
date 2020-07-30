from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    ticker = models.CharField(max_length = 10)
    open_value  = models.FloatField()
    close_value = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker



class StockFolioUser(models.Model):
  # Add StockFolio data to User
    first_name = models.CharField(default='', max_length=100)
    last_name = models.CharField(default='', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    earn = models.FloatField(default=0)
    spent = models.FloatField(default=0)



class StockPortfolio(models.Model):
  # Stock Table to maintain the stock bought
    user = models.ForeignKey(StockFolioUser, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField(default=0)



    class Meta:
    # The ForeignKey i.e. user and a stock symbol must be unique
      unique_together = ('user', 'stock')



    @staticmethod
    def buy(user_id, stock_symbol, num_shares, cost_per_share):
      # Create stock row or add num of shares
      stock_user = StockFolioUser.objects.get(user=user_id)
      stock_user.spent += float(cost_per_share) * int(num_shares)
      stock_user.save()
      result = StockPortfolio.objects.get_or_create(stock=stock_symbol, user=stock_user)[0]
      result.shares += int(num_shares)
      result.save()



    @staticmethod
    def sell(user_id, stock_symbol, num_shares, cost_per_share):
      # Create stock row or negate num of shares
      stock_user = StockFolioUser.objects.get(user=user_id)
      result = StockPortfolio.objects.filter(stock=stock_symbol, user=stock_user)[0]
      result.shares -= int(num_shares)
      if result.shares < 0:
        result.shares = 0
        stock_user.earn += float(cost_per_share) * result.shares
      else:
        stock_user.earn += float(cost_per_share) * int(num_shares)
      stock_user.save()
      if result.shares == 0:
        result.delete()
      else:
        result.save()

