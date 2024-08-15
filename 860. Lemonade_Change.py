class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {}
        # No. of possible notes that we can get
        notesList = [5,10,20]
        # current lemonade price
        lemonadePrice = 5
        # add all the notes to our dictionary
        for note in notesList:
            notes[note] = 0

        # calculate change on basis of current notes we have with us
        def calculateChange(notes: dict, changeAmount: int) -> dict:
            # change dictionary 
            changeDict = {}
            # start making change greedily with highest note
            for currentNote in reversed(notesList):
                # no. of denominations that can be made with the current note
                changeNoteCnt = changeAmount // currentNote
                if changeNoteCnt != 0:
                    # if we have the sufficient denominations
                    # then reduce the change and start with other notes
                    if notes[currentNote] >= changeNoteCnt:
                        changeAmount -= currentNote * changeNoteCnt
                        changeDict[currentNote] = changeNoteCnt
            return changeDict
        

        for bill in bills:
            # Remove lemonadePrice from bill which gives change
            changeToBeGiven = bill - lemonadePrice
            # Get the dictionary of changes based on change to be given
            changeDict = calculateChange(notes, changeToBeGiven)
            # Change given to the customer
            changeGiven = 0
            for changeNote, changeNoteCnt in changeDict.items():
                # reduce the current notes in business by change note count
                notes[changeNote] -= changeNoteCnt
                # track the change given to the customer
                changeGiven += changeNote * changeNoteCnt
            # if the change given to the customer is not same as change to be given to customer
            # then we can safely say it can't be done and return false
            if changeGiven != changeToBeGiven:
                return False
            notes[bill] += 1
        
        # finally return true
        return True
