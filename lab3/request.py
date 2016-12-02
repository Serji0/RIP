from client import Client
from friends import Friends

u_id = Client('id44014204').execute()
friends = Friends(u_id).execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))