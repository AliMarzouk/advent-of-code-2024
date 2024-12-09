def partOne(input_str: str) -> int:
    order_rules = {}
    [rules_str, pages_str] = input_str.split('\n\n')
    for rule_line in rules_str.splitlines():
        [small, big] = map(int, rule_line.split('|'))
        if not(small in order_rules):
            order_rules[small] = []
        order_rules[small] = [*order_rules[small], big]
    print(order_rules)  
    def middle_part_correct(line: str) -> int:
        page_numbers = list(map(int,line.split(',')))
        seen_numbers = {}
        for number in page_numbers:
            if list(filter(lambda x: x in order_rules[number] if number in order_rules else False, seen_numbers.keys())):
                return 0
            seen_numbers[number] = 1
        return page_numbers[len(page_numbers) // 2]
    
    result = 0
    for page_numbers_line in pages_str.splitlines():
        result += middle_part_correct(page_numbers_line)
        
    return result


def partTwo(input_str: str) -> int:
    order_rules = {}
    [rules_str, pages_str] = input_str.split('\n\n')
    for rule_line in rules_str.splitlines():
        [small, big] = map(int, rule_line.split('|'))
        if not(small in order_rules):
            order_rules[small] = []
        order_rules[small] = [*order_rules[small], big]

    def middle_part_correct(line: str) -> int:
        page_numbers = list(map(int,line.split(',')))
        seen_numbers = {}
        def get_incorrect_seen_number_index(number, current_index):
            for rule_number in order_rules[number]:
                if rule_number in seen_numbers and current_index > seen_numbers[rule_number]:
                    return seen_numbers[rule_number]
            return None
        i = 0
        while i < len(page_numbers):
            current_number = page_numbers[i]
            print('page numbers:', page_numbers)
            print('current number:', current_number)
            if current_number in order_rules:
                print('************ index: ', get_incorrect_seen_number_index(current_number, i))
            
            if current_number in order_rules and (incorrect_number_index := get_incorrect_seen_number_index(current_number, i)) != None:
                print('permuting between index : ' + str(i) + ' and incorrect inde : ' + str(incorrect_number_index))
                page_numbers[i], page_numbers[incorrect_number_index] = page_numbers[incorrect_number_index], page_numbers[i]
                i = incorrect_number_index
                continue
            seen_numbers[current_number] = i
            i += 1
        return page_numbers[len(page_numbers) // 2]
    
    result = 0
    for page_numbers_line in pages_str.splitlines():
        print('========================================================================', str(middle_part_correct(page_numbers_line)))
        result += middle_part_correct(page_numbers_line)
        
    return result

        
f = open("input.txt", "r")
input = f.read()
        
print(partTwo(input)) #11466 is too high