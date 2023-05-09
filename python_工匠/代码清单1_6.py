def magic_bubble_sort(numbers):
    stop_position=len(numbers)-1
    while stop_position:
        for i in range(stop_position):
            previous,latter=numbers[i],numbers[i+1]
            previous_is_even,latter_is_even=previous%2==0,latter%2==0
            should_swap=False
            if previous_is_even and not latter_is_even:
                should_swap=True
            elif previous_is_even==latter_is_even and previous>latter:
                should_swap=True
            if should_swap:
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
                stop_pos1ition-=1
    return numbers
i=1_000_000
print(i)
print(0.1+0.2)