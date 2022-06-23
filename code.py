with open('output/output', 'w') as output:
    with open('input/input', 'r') as input:
        for line in input:
            for word in line.split():
                num = int(word)
                output.write(str(num * num) + " ")
