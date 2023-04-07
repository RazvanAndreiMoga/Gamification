# Define a User class that represents each user in the application
class User:
    def __init__(self, name):
        self.name = name  # User's name
        self.tokens = 0  # User's tokens, initially 0
        self.badges = []  # User's badges, initially empty
        self.completed_quests = []  # User's completed quests, initially empty

# Define a Quest class that represents each quest in the application
class Quest:
    def __init__(self, title, description, reward_tokens, creator):
        self.title = title  # Quest's title
        self.description = description  # Quest's description
        self.reward_tokens = reward_tokens  # Quest's reward tokens
        self.creator = creator  # User who created the quest

# Function to create a quest
def create_quest(creator, title, description, reward_tokens):
    # Check if the creator has enough tokens to create the quest
    if creator.tokens >= reward_tokens:
        # Create a new quest and deduct the reward tokens from the creator
        quest = Quest(title, description, reward_tokens, creator)
        creator.tokens -= reward_tokens
        return quest
    else:
        return None  # If not enough tokens, return None

# Function to complete a quest
def complete_quest(user, quest):
    # Add the quest's reward tokens to the user's tokens
    user.tokens += quest.reward_tokens
    # Add the completed quest to the user's completed_quests list
    user.completed_quests.append(quest)
    # Add the quest's title as a badge to the user's badges list
    user.badges.append(quest.title)
def test_gamification():
    alice = User("Alice")
    bob = User("Bob")

    # Test: Alice does not have enough tokens to create a quest
    quest1 = create_quest(alice, "Solve a puzzle", "Solve this challenging puzzle", 10)
    assert quest1 is None

    # Test: Alice gets tokens and creates a quest
    alice.tokens = 10
    quest1 = create_quest(alice, "Solve a puzzle", "Solve this challenging puzzle", 10)
    assert quest1 is not None
    assert quest1.title == "Solve a puzzle"
    assert quest1.reward_tokens == 10
    assert quest1.creator == alice

    # Test: Bob completes the quest
    complete_quest(bob, quest1)
    assert bob.tokens == 10
    assert quest1 in bob.completed_quests
    assert "Solve a puzzle" in bob.badges
    
    print("Test passed!")

test_gamification()
