class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

    def __repr__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._User__access_level = 'admin'
        self.__users_list = []

    def add_user(self, user):
        if not any(u.get_user_id() == user.get_user_id() for u in self.__users_list):
            self.__users_list.append(user)
            print(f"{user.get_name()} Добавлен/а.")
        else:
            print(f"Такой пользователь уже существует.")

    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"User(ID: {user_id}) удален.")
                return
        print("Такого пользователя не существует.")

    def list_users(self):
        for user in self.__users_list:
            print(user)


# Тестирование системы
admin = Admin(1, "K!D")

user1 = User(2, "Вова Синий")
user2 = User(3, "Мария Зеленая")

admin.add_user(user1)
admin.add_user(user2)

# Вывести список пользователей
admin.list_users()

# Удаление пользователя
admin.remove_user(2)
admin.list_users()