def solution(string):
    return string[::-1]


def human_years_cat_years_dog_years(human_years):
    time = human_years-2
    if human_years == 1:
        return [1,15,15]
    elif human_years == 2:
                return [2,24,24]
    else:
        return [human_years,24+4*time,24+5*time]