import math

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]


def enrollment_status(universities):
    student_value_list = []
    tution_value_list = []
    for data in universities:
        student_value_list.append(data[1])
        tution_value_list.append(data[2])

    return student_value_list, tution_value_list


# student_value_list, tution_value_list = enrollment_status(universities)
# print(student_value_list)
# print(tution_value_list)


def mean(my_list):
    total = sum(my_list)
    calculated_mean = total/len(my_list)
    calculated_mean = round(calculated_mean, 2)
    return total, calculated_mean


def median(my_list):
    my_list.sort()
    if (len(my_list) + 1) % 2 == 0:
        middle_term = ((len(my_list) + 1) // 2) - 1
        return my_list[middle_term]
    else:
        middle_term = ((len(my_list) + 1) / 2) - 1
        mt_1 = math.floor(middle_term)
        mt_2 = math.ceil(middle_term)
        median = (my_list[mt_1] + my_list[mt_2]) / 2
        return median


student_value_list, tution_value_list = enrollment_status(universities)

total_student, student_mean = mean(student_value_list)
total_tution, tution_mean = mean(tution_value_list)
student_median = median(student_value_list)
tution_median = median(tution_value_list)


print("********************************************************")

print(f"Total students:  {total_student}")
print(f"Total tution: {total_tution}")

print("\n\n")

print(f"Student mean: {student_mean}")
print(f"Student midian: {student_median}")

print("\n\n")

print(f"Tution mean: $ {tution_mean}")
print(f"Tution median $ {tution_median}")
print("********************************************************")
