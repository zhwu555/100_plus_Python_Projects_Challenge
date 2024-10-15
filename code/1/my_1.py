import time
from random import randint, choice
from threading import Thread


def generate_problems(time_start, problems_list, time_total):
    global problem_count
    global correct_count
    global wrong_count
    problem_count = 0
    correct_count = 0
    wrong_count = 0
    while True:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        operator_index = randint(0, 3)
        answer = 0
        problem_count += 1
        try:
            if operator_index == 0:
                problems_list.append(f"{number1} + {number2} = {answer}")
                answer = int(input(f"remaining time: {time_total-(time.time()-time_start)}\nprease anser: {number1} + {number2} = "))
                correct_answer = number1 + number2
                problems_list[-1] = f"{number1} + {number2} = {answer}"

            elif operator_index == 1:
                problems_list.append(f"{number1} - {number2} = {answer}")
                answer = int(input(f"remaining time: {time_total-(time.time()-time_start)}\nprease anser: {number1} - {number2} = "))
                correct_answer = number1 -number2
                problems_list[-1] = f"{number1} - {number2} = {answer}"

            elif operator_index == 2:
                problems_list.append(f"{number1} * {number2} = {answer}")
                answer = int(input(f"remaining time: {time_total-(time.time()-time_start)}\nprease anser: {number1} * {number2} = "))
                correct_answer = number1 * number2
                problems_list[-1] = f"{number1} * {number2} = {answer}"

            else:
                # 除法需要特殊处理,必须整除且除数不能为0
                # 计算number1的所有因子
                problems_list.append(f"{number1} / {number2} = {answer}")
                factor_set = set()
                for i in range(1, number1+1):
                    if number1 % i == 0:
                        factor_set.add(i)
                factor_list = list(factor_set)
                number2 = choice(factor_list)
                answer = int(input(f"remaining time: {time_total-(time.time()-time_start)}\nprease anser: {number1} / {number2} = "))
                correct_answer = number1 / number2
                problems_list[-1] = f"{number1} / {number2} = {answer}"

            if answer == correct_answer:
                correct_count += 1
            else:
                wrong_count += 1
        except ValueError:
            print('您输入的答案不符合标准，请输入数字')
            continue


def main():
    time_total = 10
    time_start = time.time()
    problems_list = []
    thread1 = Thread(target=generate_problems, args=(time_start, problems_list, time_total,), daemon=True)
    thread1.start()
    time.sleep(time_total)
    print(f"一共{problem_count}道题目\n正确率为：{correct_count / problem_count:.2f}")
    print(f"具体题目及答案如下：")
    for problem in problems_list:
        print(problem)


if __name__ == '__main__':
    main()