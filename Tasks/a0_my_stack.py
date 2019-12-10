"""
My little Stack
"""
from typing import Any, List

stack: List[Any] = []


def push(elem: Any) -> None:
    """
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
    global stack
    stack.append(elem)  # pushing elem to stack

    print("Pushed elem {} to stack".format(elem))
    return None


def pop() -> Any:
    """
	Pop element from the top of the stack

	:return: popped element
	"""
    global stack
    if stack:
        return stack.pop()
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
    print("Выбран индекс {}".format(ind))
    global stack
    return stack[len(stack) - ind - 1]


def clear() -> None:
    """
	Clear my stack

	:return: None
	"""
    global stack
    stack.clear()

    return None


if __name__ == "__main__":
    push(1)
    print(stack)
