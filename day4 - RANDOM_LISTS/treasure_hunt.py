# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# turning user's input from string to integer
#position_int = int(position)

# isolating each digit into column/row variable
#position_column = (position_int // 10) - 1
#position_row = (position_int % 10) - 1

#alternative----
position_column = int(position[0]) - 1
position_row = int(position[1]) - 1

# assigning new value to specified position
map[position_row][position_column] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")