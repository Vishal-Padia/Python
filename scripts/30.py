#Use of Filter Function
participant = ['Elon Musk', 'Jeff Bezos', 'J. Cole', 'Justin Bieber', 'Jennifer Lopez']

def SelectedPerson(participant):
    selected = ['Elon Musk', 'Justin Beiber', 'J. Cole']
    if participant in selected:
        return True

selectedList = filter(SelectedPerson, participant)
print('The selected candidates are: ')
for candiate in selectedList:
    print(candiate)