
from difflib import get_close_matches


def get_best_match(user_question, questions):
    questions = [q for q in questions]
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def chatbot(knowledge):
    while True:
        user_input = input("you:")
        best_match = get_best_match(user_input,knowledge)
        if answer :=knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand')

if __name__ == '__main__':
    brain = {'hello': 'Hey there',
             'how are you': 'I am good. thanks!',
             "what are you doing":  "i am chilling.",
             "bye":"see you later"
             }

    chatbot(knowledge=brain)




