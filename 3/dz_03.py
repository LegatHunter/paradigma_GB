# Императивная vs Декларативная парадигма:

# Императивное решение:

# def sum_imperative(n):
#     result = 0
#     for i in range(1, n+1):
#         result += i
#     return result
# print(sum_imperative(5))

# Декларативное решение:

# def sum_declarative(n):
#     return sum(range(1, n+1))
# print(sum_declarative(5))



# ООП Концепции:


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print("Меня зовут", self.name, "и мне", self.age, "лет.")

# person1 = Person("Иван", 25)
# person2 = Person("Анна", 30)
# person3 = Person("Петр", 35)

# person1.introduce()
# person2.introduce()
# person3.introduce()



# Шаблон Singleton:

# class Logger:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

#     def log(self, message):
#         print("Logging:", message)


# logger1 = Logger()
# logger2 = Logger()

# logger1.log("Message 1")
# logger2.log("Message 2")

# print(logger1 is logger2)



# Шаблон Наблюдатель:

# class NotificationSystem:
#     def __init__(self):
#         self.observers = []

#     def add_observer(self, observer):
#         self.observers.append(observer)

#     def remove_observer(self, observer):
#         self.observers.remove(observer)

#     def notify_observers(self, message):
#         for observer in self.observers:
#             observer.update(message)


# class Observer:
#     def update(self, message):
#         pass


# class EmailNotification(Observer):
#     def update(self, message):
#         print("Sending email notification:", message)


# class SMSNotification(Observer):
#     def update(self, message):
#         print("Sending SMS notification:", message)


# notification_system = NotificationSystem()
# email_notification = EmailNotification()
# sms_notification = SMSNotification()

# notification_system.add_observer(email_notification)
# notification_system.add_observer(sms_notification)

# notification_system.notify_observers("New message received")