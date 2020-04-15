import random
from util import Queue
import time

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            #print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            #print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'user {i + 1}')

        possible_friendships = []

        # Create friendships
        # for user in self.users:
        #     for friend in range(user + 1, self.last_id + 1):
        #         possible_friendships.append((user, friend))

        added_friendships = 0
        desired_friendships = (num_users * avg_friendships) // 2
        failed = 0

        start_time = time.time()

        while added_friendships < desired_friendships:
            friend_1 = random.randint(1, len(self.users))
            friend_2 = random.randint(1, len(self.users))

            if self.add_friendship(friend_1, friend_2):
                possible_friendships.append((friend_1, friend_2))
                added_friendships += 1
            else:
                failed += 1

        end_time = time.time()
        print(f'Populate time: {end_time - start_time}')
        
        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            last_v = path[-1]
            if last_v not in visited:
                visited[last_v] = path
                for n in sg.friendships[last_v]:
                    path_copy = path.copy()
                    path_copy.append(n)
                    q.enqueue(path_copy)  

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    #print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    #print(connections)
    print(f'Percentage of users in a users extended network: {len(connections) / len(sg.users) * 100}%')


