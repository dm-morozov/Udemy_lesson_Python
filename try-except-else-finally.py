    # Обработка изключений
try:
    print(10/0)
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print("Найдет любую ошибку")
else:
    print("Where was no error")
finally:
    print("Продолжение выполнения кода...")

    
    # Обработка других ошибок

def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b
try:
    divide_nums(10, 0)
except ZeroDivisionError as e:
    print(e) 
except ValueError as e:
    print(e)
finally:
    print("Продолжение выполнения кода...")

    # Задания для самостоятельного выполнения

def image_info(dict_image):
    if 'image_title' not in dict_image or 'image_id' not in dict_image:
        raise TypeError("dict must contain 'image_title' and 'image_id' keys")
    return f"Image {dict['image_title']} has id {dict['image_id']}"


try:
    dict = {
        'image_title' : "my cat", 
        'image_id' : 5136
        }
    print(image_info(dict))
except TypeError as e:
    print(e)