def book_is_given(R,L,person):
    if person == R:
        return """person says: 
            'Вот! Прочтите мою книгу!'"""
    else:
        return """person says: 'О, если бы 
            мне не была дана моя книга!"""

R,L = "in right hand","in left hand"
person = input()   
print(book_is_given(R,L,person))