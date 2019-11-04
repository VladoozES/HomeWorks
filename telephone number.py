import re


class PhoneNumberException(ValueError):
    pass


def check_num_correct(number: str):
    t = re.findall(
        '([+][7] ?|[8] ?)?(\([9]\d\d\)|[9]\d\d|[-] ?\([9]\d\d\) ?[-]) ?([-] ?)?(\d{3}) ?([-] ?)?(\d\d) ?([-] ?)?(\d\d)',
        number
    )
    if len(t) != 1:
        raise PhoneNumberException('Invalid Number')
    print('OK')


while True:
    check_num_correct(input('num: '))
