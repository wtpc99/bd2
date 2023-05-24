import gc

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyClass(name={self.name})"

def create_objects():
    obj1 = MyClass("Object 1")  # 객체1을 생성
    obj2 = MyClass("Object 2")  # 객체2를 생성
    obj1.ref = obj2  # 객체 1이 객체 2를 참조합니다.

    # 객체 1에 대한 참조를 제거합니다.
    obj1 = None

    # gc 실행 요청하는것
    gc.collect()

def main():
    create_objects()

if __name__ == '__main__':
    main()
