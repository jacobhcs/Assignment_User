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
user_profile2 = User("John", "Doe", "johnd@aol.com", 99)
user_profile3 = User("Jane", "Doe", "janed@aol.com", 99)
print(user_profile)
user_profile2.enroll()
user_profile.spend_points(50)
user_profile2.spend_points(80)
print(user_profile.is_rewards_memeber, user_profile.gold_card_points)
user_profile.display_info()
user_profile2.display_info()
user_profile3.display_info()