class CountingSort():
    def counting_sort(self, non_sorted):
        if len(non_sorted) <= 1:
            return non_sorted

        minn, maxx = min(non_sorted), max(non_sorted)
        diff = maxx - minn + 1

        count = [0] * diff

        for num in non_sorted:
            count[num - minn] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        result = [0] * len(non_sorted)

        for num in reversed(non_sorted):
            index = count[num - minn]
            result[index - 1] = num
            count[num - minn] -= 1

        return result
