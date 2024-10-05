import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname  # Возвращаем никнейм при вызове print

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему")

    def log_in(self, nickname, password):
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему")
                return
        print("Неверный логин или пароль")
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            if not isinstance(video, Video): # Проверяем, что передан объект класса Video
                print(f"Объект {video} не является видео.")
                continue
            if video in self.videos: # Проверяем, есть ли видео с таким названием
                print(f"Видео '{video.title}' уже существует.")
                continue
            self.videos.append(video)
            print(f"Добавлено видео: {video.title}")

    def get_videos(self, title):
        videos_list = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                videos_list.append(video.title)
        return videos_list

    def watch_video(self, title):
        chosen_video = next((video for video in self.videos if video.title == title), None)
        # Ищем видео с заданным заголовком в списке videos
        if chosen_video is None: # Проверяем, найдено ли видео
            print(f"Видео '{title}' не найдено.")
            return
        if self.current_user is None: # Проверяем, вошел ли пользователь в аккаунт
            print("Войдите в аккаунт, чтобы смотреть видео")  # Сообщаем, если пользователь не вошел
            return
        if chosen_video.adult_mode and self.current_user.age < 18: # Проверяем возрастное ограничение для видео
            print("Вам нет 18 лет, пожалуйста, покиньте страницу")
            return
        print(f"Смотрим видео: {chosen_video.title}")
        current_time = 0
        while current_time < chosen_video.duration:
            print(current_time)  # Отображаем текущее время просмотра
            time.sleep(1)  # Пауза на 1 секунду
            current_time += 1  # Увеличиваем время просмотра на 1 секунду

        print("Конец видео")  # Сообщаем о завершении воспроизведения видео


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
