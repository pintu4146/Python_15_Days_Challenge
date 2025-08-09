

# ll, then insert some node , then reverse


class Node:
    def __init__(self, data:int)-> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f'node data: {self.data}'


head = Node(10)
# print(head)
head.next = Node(20)
current= head
# while current is not None:
#     print(current.data, end=' -> ')
#     current = current.next

10
def reverse_ll():
    """ reversing LL"""
    # 20 -> 10.
    stack = []
    current = head
    while current is not None:
        # print(current.data, end=' -> ')
        stack.append(current.data)
        current = current.next

    for i in range(len(stack)):
        ele = stack.pop()
        print(ele, end='->')


reverse_ll()

lst = [10, 4, 3, 2, 1, 11, 12, 13, 14,15],  [2,4,6,8,12]
# we want to get the output 1, 2, 3, 4, 5
lst.sort(lst)
print(lst)
max_seq_till_now  = 0
max_seq = 0
for i in range(len(lst)-1):
    if abs(lst[i] + lst[i+1]) == 1:
        max_seq += 1
    else:
        max_seq_till_now = max(max_seq, )






from fastapi import FastAPI



app = FastAPI()

@app.get('/api/v1/get_data')
async def get_data():
    data = await session.query(User).all()
    return data



#

class state(base):
    ot




"""
Q1) Select top purchasing customer for each store based on total purchase amount
Table: sales
Columns: store_id, customer_id, purchase_amt

Input:

store_id	customer_id	   purchase_amt

1	          101	                  500
1	101	300
1	102	500
2	101	1000
2	102	900
3	101	1000
3	102	1000


Expected Output:

store_id	customer_id	total_amt

1	101	800
2	101	1000
3	101	1000
3	102	1000
"""
"""
select sum(purchage_amount)

from sales
groupby storeid, purchage_amount






"""














