from collections import Counter
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        slow = 0
        picked_fruit = Counter()
        max_fruit = 0
        for fast, fruit in enumerate(fruits):
            picked_fruit[fruit] += 1

            while len(picked_fruit) > 2:
                picked_fruit[fruits[slow]] -= 1
                if picked_fruit[fruits[slow]] == 0:
                    picked_fruit.pop(fruits[slow])
                slow += 1

            max_fruit = max(max_fruit, fast-slow+1)

        return max_fruit
