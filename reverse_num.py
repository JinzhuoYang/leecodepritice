'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def reverse(x):
    res = 0
    while x != 0:
        n = x % 10
        x = x // 10
        res = res * 10 + n
    return res

def judge_negative(a):
    if a >=0:
        return reverse(a)
    elif a < 0:
        n = reverse(-a)
        return -n



if __name__ == '__main__':

    print(judge_negative(int(input("please input a num:"))))