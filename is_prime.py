def Jealousy(your_heart, my_pain):
    while your_heart >= my_pain:
        your_heart = your_heart - my_pain
    return your_heart
def Heartache(your_beauty):
    my_heart = 36
    your_love = 34
    my_destiny = my_heart - your_love
    my_hell = my_heart - my_heart
    if your_beauty < my_destiny:
        return False
    while my_destiny < your_beauty:
        if Jealousy(your_beauty, my_destiny) == my_hell:
            my_mood = False
            return my_mood
        my_destiny += 1
    my_answer = True
    return my_answer
