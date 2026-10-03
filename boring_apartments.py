#if number is 22, we need to count the digits in 1, 11, 111, 1111, 2, 22
#max we can go till 9999
#digit_cnt_map is used to add leftovers, like in case of 22
# from 1 uptil 1111 we have 10 digits guaranteed, plus we need to add 3 digits for 2 and 22
# therefore we map 2:3 where 2 represents len(the final number)
#so if we want to go till 2222, we have 10 + digit_cnt_map(len(2222)) => 10+10 = 20
tc = int(input())
tc_items = []
sumn = 0
res = []
digit_cnt_map = {
    1:1,
    2:3,
    3:6,
    4:10
}
for i in range(tc):
    num = input()
    tc_items.append(int(num))
for i in tc_items:
    aptmnt_digit_rchd = int(str(i)[0])
    sumn = (aptmnt_digit_rchd-1)*10 + digit_cnt_map[len(str(i))]
    res.append(sumn)

for i in res:
    print(i, end="\n")



