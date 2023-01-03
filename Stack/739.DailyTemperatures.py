def DailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)


    for cur_day, cur_temp in enumerate(temperatures):
        while stack and cur_temp > stack[-1][1]:
            prev_day, prev_temp = stack.pop()

            res[prev_day] = cur_day - prev_day
            
            stack.append((cur_day, cur_temp))

    return res




if __name__ == '__main__':
    print(DailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))