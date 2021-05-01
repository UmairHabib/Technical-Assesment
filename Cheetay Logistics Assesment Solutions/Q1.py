def activityselection(start,end,N):
    #Algorithm take n log n time due to Timsort builtin sorting
    # it requires O(N) Auxilliary space due to zipped array
    try:
        #constraints are checked according to description
        def constraintChecker(zippedActivities,startIndex,endIndex):
            if (1 <= zippedActivities[endIndex][0] <=109) and (1 <= zippedActivities[startIndex][1]<=109):
                return True
            else:
                raise Exception("Constraint Not Match value is less than 0 or greater than 109")


        if N<1 or N> (2*105) or len(start) != len(end):
            raise Exception("Length is greater than 2*105 or less than 1 or both of them are not equal")


        #Alogrithm start here
        zippedActivities = list(zip(start, end))
        zippedActivities.sort(key=lambda x: x[1])  # Timsort sorting activities with respect to finish time
        counter=0
        if constraintChecker(zippedActivities,0,0):
            counter=1

        i = 0
        for j in range(1, N):
            if constraintChecker(zippedActivities,i,j):
                if zippedActivities[i][1] < zippedActivities[j][0]:
                    i = j
                    counter=counter+1
        return counter


    except Exception as e:
        return 'Exception Occured '+ str(e)
