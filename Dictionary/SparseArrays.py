def matchingStrings(strings, queries):
    result = []

    for query in queries:
        count = 0
        for string in strings:
            if query == string:
                count += 1
        result.append(count)

    return result