def maxMeetings(S,F,N):
    #Algorithm take n log n time due to Timsort builtin sorting
    # it requires O(N) Auxilliary space due to zipped array
    try:
        #constraints are checked according to description
        def constraintChecker(zippedMeetings,startIndex,endIndex):
            if (0 <= zippedMeetings[endIndex][0] <=105) and (0 <= zippedMeetings[startIndex][1]<=105):
                return True
            else:
                raise Exception("Constraint Not Match value is less than 1 or greater than 105")


        if N<1 or N> (105) or len(S) != len(F):
            raise Exception("Length is greater than 105 or less than 1 or both of them are not equal")


        #Alogrithm start here
        zippedMeetings = list(zip(S, F))
        zippedMeetings.sort(key=lambda x: x[1])  # Timsort sorting activities with respect to finish time
        counter=0
        if constraintChecker(zippedMeetings,0,0) and zippedMeetings[0][1] < zippedMeetings[0][0]:
            counter=1

        i = 0
        for j in range(1, N):
            if constraintChecker(zippedMeetings,i,j):
                if zippedMeetings[i][1] < zippedMeetings[j][0]:
                    i = j
                    counter=counter+1
        return counter


    except Exception as e:
        return 'Exception Occured '+ str(e)