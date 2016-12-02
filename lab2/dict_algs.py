def children_older_18(arr):
    result = []
    for i in range(0,len(arr)):
        children_length = len(arr[i].get('children'))
        flag = 0
        for j in range(0, children_length):
            if int(arr[i].get('children')[j].get('age'))>18:
                flag = 1
                break
        if flag:
            result.append((arr[i].get('name')))
    return result


ivan = {
    'name': 'ivan',
    'age': '34',
    'children': [{
        'name': 'vasja',
        'age': '12'
    }, {
        'name': 'petja',
        'age': '10'
    }]
}
darja = {
    'name': 'darja',
    'age': '41',
    'children': [{
        'name': 'kirill',
        'age': '21'
    },{
        'name': 'pavel',
        'age': '15'
    }]
}


emps = [ivan, darja]

result = children_older_18(emps)

print(result)