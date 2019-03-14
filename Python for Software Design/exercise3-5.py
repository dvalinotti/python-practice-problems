# Write a function that draws a box using - for sides and + for corners

def draw_box():
    for i in range(11):
        line = ""
        if (i % 5 == 0):
            for k in range(21):
                if k == 0 or (k)% 10 == 0:
                    line+='+ '
                elif k % 2 == 0:
                    line+='- '
        else:
            line = '|' + (' ' * 9) + '|' + (' ' * 9) + '|'
        print(line)
            
draw_box()