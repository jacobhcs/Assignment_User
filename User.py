class User:
  def __init__(self, f_name, l_name, email, age):
    self.first_name = f_name
    self.last_name = l_name
    self.email = email
    self.age = age
    is_rewards_memeber = False
    gold_card_points = 0
  def display_info(self):
    print(self.first_name)
    print(self.last_name)
    print(self.email)
    print(self.age)
  def enroll(self):
    self.is_rewards_memeber = True
    self.gold_card_points = 200
  def spend_points(self, amount):
    self.gold_card_points -= amount

user_profile = User("Jacob", "Harris", "jacobh@aol.com", 24)
print(user_profile)
user_profile.display_info()
user_profile.enroll()
user_profile.spend_points(25)
print(user_profile.is_rewards_memeber, user_profile.gold_card_points)