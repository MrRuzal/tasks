# {
# 	'year' : '2025',
# 	'month': '12',
# 	'day'  : '31',
# }
# Из элементов этого словаря соберите дату в следующем формате:
# '2025-12-31'


def formatting_date(input_date):
    return f"{input_date['year']}-{input_date['month']}-{input_date['day']}"


if __name__ == '__main__':
    input_date = {
        'year': '2025',
        'month': '12',
        'day': '31',
    }
    print(formatting_date(input_date))
