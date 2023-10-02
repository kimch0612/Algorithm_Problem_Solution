num_char = input()
t = 0

t += num_char.count("A") * 3 + num_char.count("B") * 3 + num_char.count("C") * 3
t += num_char.count("D") * 4 + num_char.count("E") * 4 + num_char.count("F") * 4
t += num_char.count("G") * 5 + num_char.count("H") * 5 + num_char.count("I") * 5
t += num_char.count("J") * 6 + num_char.count("K") * 6 + num_char.count("L") * 6
t += num_char.count("M") * 7 + num_char.count("N") * 7 + num_char.count("O") * 7
t += num_char.count("P") * 8 + num_char.count("Q") * 8 + num_char.count("R") * 8 + num_char.count("S") * 8
t += num_char.count("T") * 9 + num_char.count("U") * 9 + num_char.count("V") * 9
t += num_char.count("W") * 10 + num_char.count("X") * 10 + num_char.count("Y") * 10 + num_char.count("Z") * 10

print(t)
