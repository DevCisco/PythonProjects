def powerroot(n):
    return n/2
def ciccio(n):
    return n//1.50
insurance = int(input('Price insurance: '))
age = int(input('Your age: '))
is_old = age >= 40
is_young = age <= 28
not_y_or_o = 28 < age < 40
has_license = input('Do you have license?')
if has_license == 'yes':
        has_license = True
else:
        has_license = False
if has_license and is_old:
        insurance = powerroot(insurance)
        print('Your insurance is:')
        print(insurance)
if has_license and is_young:
        insurance = ciccio(insurance)
        print('Your insurance is ')
        print(insurance)
if not has_license and not_y_or_o:
        print('Not eligible for insurance')
