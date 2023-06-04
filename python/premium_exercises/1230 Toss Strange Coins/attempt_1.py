class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        n = len(prob)

        target_head = target / n
        target_tail = (n - target) / n

        total_head_prob = 1
        total_tail_prob = 1
        total_prob = 0

        for head_prob in prob:
            tail_prob = 1-head_prob

            total_head_prob *= target_head * head_prob
            total_tail_prob *= target_tail * tail_prob

            current_prob = (target_head) * head_prob * (target_tail * tail_prob)
            total_prob += current_prob

        return total_prob
