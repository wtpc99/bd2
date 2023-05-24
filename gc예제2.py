import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list():
    head = Node(0)
    current = head

    for i in range(1, 1000000):
        new_node = Node(i)
        current.next = new_node
        current = new_node

# head 변수만 반환하여 나머지 노드들에 대한 참조가 사라지지 않는다.
    return head

def main():
    linked_list = create_linked_list()
# linked_list 변수에 다른 값을 할당하여 참조 해제가 일어나지 않는다.
    linked_list = None

    # 가비지 컬렉션 실행 요청합ㄴㅣ다.
    gc.collect()

if __name__ == '__main__':
    main()
#이렇게 연결 리스트의 노드들이 서로를 참조하여 가비지로 인식되지 않고 메모리에 유지되는 상황이 메모리 누수를 발생시킵니다.
