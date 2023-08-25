import nltk
from nltk.tokenize import word_tokenize
from nltk.metrics import jaccard_distance


# Define predefined questions and answers
qa_pairs = [
    ("hi", "Hi! How can I chirp you today?"),
    ("how are you", "I'm feeling chirpy and ready to chat! How about you?"),
    ("favorite", "I love singing, mimicking sounds, and hanging out with pals!"),
    ("bye", "Farewell for now. Have a flap-tastic day!"),
    ("mimic", "Absolutely! Listen to this: 'Hello there, lovely day, isn't it?'"),
    ("music", "I'm all about the beats! Upbeat tunes get me grooving and squawking along!"),
    ("move", "Squawk! Chatter is my signature move. I mimic words to confuse opponents!"),
    ("live", "I'm right at home in colorful forests and sunny tropical spots."),
    ("rain", "Rain or shine, I'm always ready to chat. But I do love sunny weather to shine brightly!"),
    ("trick", "Squawk! I'm a mimic master. Watch this dance and mimic combo!"),
    ("color", "My feathers are a colorful masterpiece, but I'm partial to vibrant blue."),
    ("explore", "Exploring new places means fresh things to chirp about. I'm all for it!"),
    ("ocean", "I've flown over expansive oceans and landed on remote tropical islands. The sights and sounds were mesmerizing!"),
    ("food", "Berries are my favorite snack. They keep my energy high for all the squawking!"),
    ("friends", "I enjoy the company of talkative Pokémon like Meowth and Ludicolo. We make quite the chatty group!"),
    ("joke", "Why don't oysters donate to charity? Because they're shellfish! Squawk, get it?"),
    ("weather", "Rain or shine, I'm always here to chat. But sunny weather makes my feathers really pop!"),
    ("tricks", "I can mimic voices, dance a little jig, and even imitate the sound of waves. Shhhhh..."),
    ("colorful", "I love vibrant colors. They match my personality and my feathers!"),
    ("ocean", "I've flown over vast oceans and landed on tropical islands. The beauty of the water and the sounds of the waves were incredible!"),
    ("joke", "Why did the Tail low sit in the shade? Because it didn't want to be a hot wing! Squawk, isn't that a funny one?")
]

def get_response(user_input):
    user_tokens = word_tokenize(user_input)
    best_score = float("inf")
    best_response = "Squawk! That's interesting! Tell me more!"

    for question, response in qa_pairs:
        question_tokens = word_tokenize(question)
        jaccard_score = jaccard_distance(set(question_tokens), set(user_tokens))
        
        if jaccard_score < best_score:
            best_score = jaccard_score
            best_response = response

    return best_response

def chatot_chat():
    print("Chatot: Squawk! Hi there, I'm Chatot, the talkative Pokémon. Let's have a delightful chat!")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input:
            print("Chatot: Squawk! Farewell for now. Have a flap-tastic day!")
            break

        response = get_response(user_input)
        print("Chatot:", response)

if __name__ == "__main__":
    chatot_chat()
