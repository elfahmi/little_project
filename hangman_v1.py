import random
import time


def animated_hang_man():
    animations_1 = """
        |     
        |     
        |
        |    
     ___|___  
    """
    animations_2 = """
        |-------
        |     
        |   
        | 
        | 
     ___|___  
    """
    animations_3 = """
        |-----|--
        |     O
        | 
        |
        |
     ___|___  
    """
    animations_4 = """
        |-----|--
        |     O
        |     | 
        |     |
        |     
     ___|___  
    """
    animations_5 = """
        |-----|--
        |     O
        |    /|  
        |     |
        |    
     ___|___  
    """
    animations_6 = """
        |-----|--
        |     O
        |    /|\  
        |     |
        |     
     ___|___  
    """
    animations_7 = """
        |-----|--
        |     O  ====> Last Chance You Idiot
        |    /|\  
        |     |
        |    / 
     ___|___  
    """
    animations_8 = r"""
        |-----|--
        |     O  ====> You Died
        |    /|\  
        |     |
        |    / \
     ___|___  
    """
    animated_list = [animations_1, animations_2, animations_3, animations_4, animations_5,
                     animations_6, animations_7, animations_8]
    return animated_list


def main():
    animals = ['rabbit', 'elephant', 'eagle', 'chicken']
    answer = random.choice(animals)
    answer_length = len(answer)
    print('=' * 6 + ' GAME HANGMAN ' + '=' * 6)
    print()
    answer_list = ['_'] * answer_length
    animasi = animated_hang_man()
    while True:
        print(' '.join(answer_list))
        your_answer = input('\n\nMasukkan Karakter: ')
        print()
        if not your_answer:
            print('Cannot Be empty\n')
            continue
        if your_answer in answer:
            temp = []
            for index, ch in enumerate(answer):
                if your_answer == ch:
                    temp.append(index)
            for x in temp:
                answer_list[x] = your_answer
        if your_answer not in answer:
            time.sleep(0.5)
            print(animasi[0])
            del animasi[0]
            if not animasi:
                break
        if '_' not in answer_list:
            print('You Win')
            print((' '.join(answer_list)).upper())
            break


if __name__ == '__main__':
    main()
