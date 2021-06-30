def lyrics_generator(lyric):
    one_counter=0
    final_string=""
    for number in lyric:
        if number==0:
            final_string=final_string+"Boom "
            one_counter=0
        elif number==1:
            final_string=final_string+"Drop the base "
            one_counter+=1
        if one_counter==3:
            final_string=final_string+"!!!Break the base!!! "   
    return final_string

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))