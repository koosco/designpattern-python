"""
기본 싱글턴

* 조잡한 싱글턴은 생성자를 숨기고 정적 생성 메서드만을 제공하면 된다
* 다중 쓰레드 환경에서 동작하지 못하는 문제가 있다
* 여러 스레드가 생성 메서드를 동시에 호출할 수 있으며, 싱글턴 클래스의 여러 인스턴스를 가져올 수 있다
"""
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance")
    else:
        print("Singleton failed, variables contain different instances")
