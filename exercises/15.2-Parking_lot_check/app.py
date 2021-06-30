parking_state = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 2]
]

# Your code go here:




def get_parking_lot():
    state = {"total_Slots": 0, "available_Slots": 0, "occupied_Slots": 0}

    for i in range(0, len(parking_state), 1):
        for j in parking_state[i]:

            if j == 2:
                state["available_Slots"] = state["available_Slots"]+1
            elif j == 1:
                state["occupied_Slots"] = state["occupied_Slots"]+1
        state["total_Slots"] = state["total_Slots"]+1
    return state

print(get_parking_lot())
