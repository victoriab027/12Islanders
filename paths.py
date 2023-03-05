import random

succesful = []
num = 3

was_just_successful = False
while(len(succesful) < num):
    ## PROBLEM SETUP

    while was_just_successful:
        print("Attempting path: "+str(current_path))
        for idx in range (0,len(islanders)):
            print("at index "+ str(idx))
            islanders = [1] * 12
            rand_value = random.choice([0.5, 1.5])  # randomly select a value of -1 or 1 (over or underweight)
            islanders[idx] = rand_value  # assign the random value to the random index

            for attempt in range(0,3):
                on_seesaw_left = current_path[attempt][0]-1 # subtract one for the indexs
                on_seesaw_right = current_path[attempt][1]-1

                sum_left = sum(islanders[:on_seesaw_left])
                sum_right = sum(islanders[on_seesaw_left:on_seesaw_right])
            
                if(sum_left == sum_right):#if they are the same, none of the islanders on the seesaw are different
                    islanders = islanders[on_seesaw_right:]
                else: #someone in here is different
                    islanders = islanders[:on_seesaw_right]
        
            if len(islanders) == 1:
                succesful.append(current_path)
            else:
                was_just_successful = False
                print("Failed at index: "+str(idx))

            if idx == 11 and len(islanders) == 1: #we've reached the end and it was good for all!  
                succesful.append(current_path) 
    else:
        islanders = [1] * 12
        rand_index = random.randint(0, 11)  # randomly select an index between 0 and 11
        rand_value = random.choice([0.5, 1.5])  # randomly select a value of -1 or 1 (over or underweight)
        islanders[rand_index] = rand_value  # assign the random value to the random index
        current_path = []
        for attempt in range(0,3):
            num_left = len(islanders)
            if attempt == 0: # num left & num right need to equal
                on_seesaw_left = random.randint(0, num_left/2)
                on_seesaw_right = on_seesaw_left+on_seesaw_left+1
            else:
                on_seesaw_left = random.randint(0, num_left)
                on_seesaw_right = random.randint(on_seesaw_left, num_left)
        
            sum_left = sum(islanders[:on_seesaw_left])
            sum_right = sum(islanders[on_seesaw_left:on_seesaw_right-on_seesaw_left])

            current_path.append([on_seesaw_left,on_seesaw_right])
        
            if(sum_left == sum_right):#if they are the same, none of the islanders on the seesaw are different
                islanders = islanders[on_seesaw_right:]
            else: #someone in here is different
                islanders = islanders[:on_seesaw_right]
        if len(islanders) == 1:
            was_just_successful = True

print(succesful)