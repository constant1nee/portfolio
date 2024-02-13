import socket
import pygame
import pygame_menu
import easygui
import os.path
import json
import random
import pygame_menu.widgets
from ast import literal_eval
from datetime import datetime
from load_image import load_image
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# connection to the server

cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
cl_socket.connect(('localhost', 10000))

# pygame window initialization

pygame.init()
screen_width, screen_height = 500, 500
button_clicked = ''
start_typing = False
active = False
first_time = True
all_coords = []
#user_data = {'hanwriting': [[]], 'text': [[]], 'files': []}

config_file_path = 'config.json'


def check_first_time():
    try:
        with open(config_file_path, 'r') as file:
            config = json.load(file)
            return config.get('first_time', True)
    except FileNotFoundError:
        return True


def set_not_first_time():
    config = {'first_time': False}
    with open(config_file_path, 'w') as file:
        json.dump(config, file)


# Check if it's the first time
if check_first_time():
    print("Welcome! It's your first time.")
    # Perform first-time setup

    # Set flag to indicate it's not the first time
    set_not_first_time()
else:
    print("Welcome back!")
    first_time = False


def draw_background(screen):
    for i in range(-10000, 10000, 30):
        pygame.draw.line(screen, (100, 100, 100), (i, 10000), (i, -i), 1)
        pygame.draw.line(screen, (100, 100, 100), (-i, i), (10000, i))
    pygame.draw.rect(app.new_screen, 'white', (0, 0, 50, 200))
    pygame.draw.rect(app.new_screen, 'white', (0, 400, 50, 100))


class LoadFile:
    def __init__(self):
        self.active = False
        self.count = 0
        self.image_lst = []

    def click(self):
        self.count += 1
        print(self.count)
        if self.count % 2 != 0:
            self.active = True
            print('active')
        else:
            self.active = False
            print('non_active')

    def load_file(self, screen):
        try:
            input_file = easygui.fileopenbox()
            image = pygame.image.load(input_file)
            image = pygame.transform.scale(image, (300, 250))
            self.image_lst.append(image)
            screen.blit(image, (150, 150))
        except TypeError:
            pass
        except pygame.error:
            pass

    def display(self):
        if len(self.image_lst) > 0:
            screen.blit(self.image_lst[-1], (150, 150))
        if not app.running:
            self.image_lst.clear()


class Erasing:
    def __init__(self):
        self.active = False
        self.count = 0
        self.x, self.y = 100, 100
        self.width, self.height = 20, 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def click(self):
        self.count += 1
        print(self.count)
        if self.count % 2 != 0:
            self.active = True
            print('active')
        else:
            self.active = False
            print('non_active')

    def erasing(self, event, screen):
        self.rect.x, self.rect.y = event.pos
        pygame.draw.rect(screen, 'red', self.rect)
        for segment in all_coords:
            if self.rect.collidepoint(segment[1]):
                segment[2] = 'white'


class Handwriting:
    def __init__(self):
        global all_coords
        self.active = False
        self.make_click = True
        self.count = 0
        self.coords_lst = []
        self.obj = []
        '''self.rects = []
        self.x_lst, self.y_lst = [], []
        self.x_lst_2, self.y_lst_2 = [], []'''
        self.lst = []
        self.color = 'black'

    def click(self):
        global start_writing
        self.count += 1
        print(self.count)
        if self.count % 2 != 0:
            self.active = True
            print('active')
        else:
            self.active = False
            print('non_active')

    def handwriting(self, coords_lst):
        '''for elem in coords_lst:
            self.x_lst.append(elem[0])
            self.y_lst.append(elem[1])'''
        if len(coords_lst) > 2:
            pygame.draw.lines(screen, self.color, True, [[coords_lst[-2][0], coords_lst[-2][1]],
                                                         [coords_lst[-1][0], coords_lst[-1][1]]], 3)
            all_coords.append([(coords_lst[-2][0], coords_lst[-2][1]), (coords_lst[-1][0], coords_lst[-1][1]),
                               self.color])

    def text_surf(self):
        pass
        '''rect = pygame.Rect(min(self.x_lst), min(self.y_lst),
                           max(self.x_lst) - min(self.x_lst), max(self.y_lst) - min(self.y_lst))
        self.rects.append(rect)'''

    def load(self, lst, screen):
        print('load')
        for obj in lst:
            self.obj = obj
            if self.obj:
                pygame.draw.lines(screen, self.obj[2], True, self.obj[:2], 3)


class TextInput:
    def __init__(self):
        self.x, self.y = 150, 250
        self.width, self.height = 20, 50
        self.string_num = 1
        self.count = 0
        self.active = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.symb_x, self.symb_y = self.rect.x, self.rect.y
        self.text_data = {}
        self.ready_to_move = False
        self.text = ''
        self.font = pygame.font.Font(None, 50)

    def click(self):
        self.count += 1
        if self.count % 2 == 0:
            self.active = False
            print('not active')
        else:
            self.active = True
            print('active')

    def typing(self, event):
        if event.type == pygame.KEYDOWN:
            print('start_typing')
            if event.key == pygame.K_RETURN:
                self.text = ''
                self.rect.height += 50
                self.symb_y += 50
                self.string_num += 1
            elif event.key == pygame.K_BACKSPACE:
                if self.text == '':
                    self.text_data.pop(f'{self.string_num}')
                    self.string_num -= 1
                    self.symb_y -= 50
                    self.text = self.text_data[f'{self.string_num}'][0]
                else:
                    self.text = self.text[:-1]
                self.rect.width -= 17
                self.text_data[f'{self.string_num}'] = [self.text, [self.symb_x, self.symb_y]]
            else:
                self.text += event.unicode
                self.rect.width += 20
                self.text_data[f'{self.string_num}'] = [self.text, [self.symb_x, self.symb_y]]
            print(self.text, self.text_data)

    def move(self, shift):
        self.rect.x += shift[0]
        self.rect.y += shift[1]
        self.symb_x += shift[0]
        self.symb_y += shift[1]
        for item in self.text_data:
            self.text_data[item][1][0] += shift[0]
            self.text_data[item][1][1] += shift[1]

    def display(self, screen):
        for item in self.text_data:
            string = self.font.render(self.text_data[item][0], True, 'black')
            screen.blit(string, (self.text_data[item][1][0], self.text_data[item][1][1]))

    def load(self, txt_data, mode=None):
        for item in txt_data:
            string = self.font.render(txt_data[item][0], True, 'black')
            screen.blit(string, (txt_data[item][1][0], txt_data[item][1][1]))


class Button(pygame.sprite.Sprite):
    def __init__(self, group, y, btn_passive, btn_active, btn_in_process, on_click, btn_2=None):
        super().__init__(group)
        self.btn_passive, self.btn_active = btn_passive, btn_active
        self.btn_in_process = btn_in_process
        self.btn_2 = btn_2
        self.on_click = on_click
        self.image = btn_passive
        self.rect = self.image.get_rect(topleft=(0, y))
        self.count = 0
        self.status = 'private'

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(args[0].pos):
                self.image = self.btn_passive
            else:
                self.image = self.btn_in_process
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                if self.btn_2:
                    self.count += 1
                self.on_click()
        if self.btn_2 and self.count % 2 == 0:
            self.image = self.btn_passive
            self.status = 'private'
        elif self.btn_2 and self.count % 2 != 0:
            self.image = self.btn_2
            self.status = 'public'


class Database:
    def __init__(self):
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.sample_spreadsheet_id = "1wX5KOYqSK6g_VigmqOWGJ8bTDc0YffAzD_s2qE2QU7I"
        self.sample_range_name = "Class Data!A2:E"
        self.values = None
        self.data = None
        self.creds = Credentials.from_authorized_user_file("token.json", self.scopes)
        self.shift = 0
        self.abc = 'ABCDEF'

    def get_data(self, *args, usr_data=None):
        for arg in args:
            if type(arg) == dict:
                # ******************* to store dict instead of list *******************
                # if usr_data:
                #     self.make_request(arg, mode='write',
                #                     row=f'{self.count_rows()}', col=f'{self.abc[5]}')
                # else:
                for i, k in enumerate(arg.keys()):
                    self.make_request(arg[k], mode='write',
                                      row=f'{self.count_rows()}', col=f'{self.abc[i]}')
            elif type(arg) == str:
                if arg == 'public' or arg == 'private':
                    self.make_request(arg, mode='write',
                                      row=f'{self.count_rows()}', col=f'{self.abc[3]}')
                else:
                    self.make_request(arg, mode='write',
                                      row=f'{self.count_rows()}', col=f'{self.abc[2]}')
            elif type(arg) == datetime:
                self.make_request(arg, mode='write',
                                  row=f'{self.count_rows()}', col=f'{self.abc[4]}')
            elif type(arg) == list:
                self.make_request(arg, mode='write',
                                  row=f'{self.count_rows()}', col=f'{self.abc[5]}')
        if not app.running:
            self.count_rows()

    def make_request(self, data=None, mode=None, col=None, row=None, range_to_fetch=None):
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", self.scopes)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.scopes
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())
        if mode == 'write':
            self.write(data, col, row)
        elif mode == 'read':
            if range_to_fetch:
                self.read(col=range_to_fetch, row='')
            else:
                self.read(task='get', col='F', row=self.count_rows(value=self.get_username()))

    def read(self, task=None, col=None, row=None):
        service = build("sheets", "v4", credentials=self.creds)
        sheet = service.spreadsheets()
        self.values = sheet.values().get(
            spreadsheetId=self.sample_spreadsheet_id,
            range=f'Лист1!{col}{row}',
            majorDimension='ROWS'
        ).execute()
        if task == 'get':
            self.values = literal_eval(self.values['values'][0][0])

    def write(self, data, col=None, row=None):
        service = build("sheets", "v4", credentials=self.creds)
        range_name = f'Лист1!{col}{row}' if row else 'Лист1!A1'
        self.values = service.spreadsheets().values().append(
            spreadsheetId=self.sample_spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body={'values': [[str(data)]]}).execute()

    def update_status(self, data, status):
        request_body = {'values': [[status]]}
        row = self.count_rows(value=data)
        service = build('sheets', 'v4', credentials=self.creds)
        sheet = service.spreadsheets()
        self.values = sheet.values().update(
            spreadsheetId=self.sample_spreadsheet_id,
            range=f'Лист1!D{row}',
            valueInputOption='RAW',
            body=request_body).execute()

    def count_rows(self, value=None, count_all=None):
        rows = []
        print(f'initial value: {value} in {app.all_ids}')
        if value in app.all_ids:
            range_to_fetch = 'Лист1!C:C'
        else:
            range_to_fetch = 'Лист1!A:A'
        service = build('sheets', 'v4', credentials=self.creds)
        result = service.spreadsheets().values().get(spreadsheetId=self.sample_spreadsheet_id,
                                                     range=range_to_fetch).execute()
        values = result.get('values', [])
        if not values:
            print('The spreadsheet is empty.')
            return 1
        for i, row in enumerate(values, start=1):
            if value:
                if row[0] == value:
                    rows.append(i)
            else:
                rows.append(i)
        if count_all:
            return rows
        else:
            return rows[-1] if rows else 1

    def get_username(self):
        with open(config_file_path, 'r') as file:
            existing_config = json.load(file)
        username = existing_config['username']
        return str(username)


class Application:
    def __init__(self):
        self.new_screen = pygame.display.set_mode((screen_width, screen_height))
        self.new_screen.fill('white')
        self.menu = pygame_menu.Menu('EWAP', screen_width, screen_height)
        self.eraser_btn_passive = load_image('buttons/eraser_passive.png')
        self.eraser_btn_active = load_image('buttons/eraser_active.png')
        self.eraser_btn_on_click = load_image('buttons/eraser_clicked.png')
        self.pencil_btn_passive = load_image('buttons/pencil_passive.png')
        self.pencil_btn_active = load_image('buttons/pencil_active.png')
        self.pencil_btn_on_click = load_image('buttons/pencil_clicked.png')
        self.text_btn = load_image('buttons/text_input_passive.png')
        self.text_btn_on_click = load_image('buttons/text_input_active.png')
        self.input_file_btn = load_image('buttons/input_file_passive.png')
        self.input_file_btn_on_click = load_image('buttons/input_file_active.png')
        self.access_private_btn_active = load_image('buttons/private_active.png')
        self.access_private_btn_passive = load_image('buttons/private_passive.png')
        self.access_public_btn_active = load_image('buttons/public_active.png')
        self.access_public_btn_passive = load_image('buttons/public_passive.png')
        self.all_sprites = pygame.sprite.Group()
        self.eraser_btn = Button(self.all_sprites, 0, self.eraser_btn_passive, self.eraser_btn_active,
                                 self.eraser_btn_on_click, erasing.click)
        self.pencil_btn = Button(self.all_sprites, 50, self.pencil_btn_passive, self.pencil_btn_active,
                                 self.pencil_btn_on_click, handwriting.click)
        self.txt_btn = Button(self.all_sprites, 100, self.text_btn, None, self.text_btn_on_click, text.click)
        self.file_btn = Button(self.all_sprites, 150, self.input_file_btn, None,
                               self.input_file_btn_on_click, load_file.click)
        self.set_access_btn = Button(self.all_sprites, 400, self.access_public_btn_active,
                                     None, self.access_public_btn_active, set_access,
                                     btn_2=self.access_private_btn_active)
        self.quit_btn = Button(self.all_sprites, 450, self.eraser_btn_passive,
                               None, self.eraser_btn_on_click, self.click)
        self.all_ids = []
        self.coords_lst = []
        self.x_lst, self.y_lst = [], []
        self.start_writing = False
        self.start_erasing = False
        self.new_session_started = False
        self.running = True
        self.public = False
        self.current_session_id = 0
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def mainloop(self, mode=None):
        global all_coords
        # global user_data
        self.running = True
        self.new_screen = pygame.display.set_mode((screen_width, screen_height))
        if mode == 'new':
            self.send_user_info()
            all_coords.clear()
            text.text_data.clear()
        elif mode == 'load':
            all_coords.clear()
            all_coords = db.values
            # user_data.clear()
            # user_data = db.values
            print(all_coords)
            self.send_user_info()
        self.current_session_id = self.generate_id()
        db.get_data(self.current_session_id, 'private',
                    datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M"))
        while self.running:
            self.new_screen.fill('white')
            handwriting.load(all_coords, self.new_screen)
            # handwriting.load(user_data['handwriting'])
            # text.load(user_data['text'])
            # load_file.load(user_data['file'])
            for event in pygame.event.get():
                current_coords = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if erasing.active:
                        self.start_erasing = True
                    if handwriting.active:
                        self.start_writing = True
                        handwriting.lst.clear()
                    if text.rect.collidepoint(event.pos):
                        text.ready_to_move = True
                elif event.type == pygame.MOUSEMOTION:
                    self.coords_lst.append(current_coords)
                    if text.ready_to_move and text.active:
                        text.move(event.rel)
                    if self.start_writing:
                        handwriting.handwriting(self.coords_lst)
                    elif self.start_erasing:
                        erasing.erasing(event, self.new_screen)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    print(all_coords)
                    self.start_writing = False
                    load_file.active = False
                    text.ready_to_move = False
                    if self.x_lst and self.y_lst:  # Use the truthy nature of non-empty lists
                        handwriting.text_surf()
                    if self.start_erasing:
                        self.start_erasing = False
                    self.coords_lst.clear()
                    self.x_lst.clear()
                    self.y_lst.clear()
                self.all_sprites.update(event)
                if text.active:
                    text.typing(event)
            text.display(self.new_screen)
            draw_background(self.new_screen)
            self.all_sprites.draw(screen)
            self.all_sprites.update()
            if load_file.active:
                load_file.load_file(self.new_screen)
            load_file.display()
            pygame.display.flip()
            pygame.display.update()
            cl_socket.send('Действие клиента'.encode())
            data = cl_socket.recv(1024)
            try:
                data = data.decode('utf-8')
            except UnicodeDecodeError:
                pass
            self.clock.tick(self.FPS)

    def click(self):
        self.running = False
        self.start_writing = False
        # user_data['handwriting'] = all_coords
        # user_data['text'] = text_data
        # user_data['files'] = file_data
        # db.get_data(user_data)
        db.get_data(all_coords)
        drop_sessions_list()

    def send_user_info(self):
        with open(config_file_path, 'r') as file:
            existing_config = json.load(file)
        db.get_data({'user': existing_config['username'],
                     'password': existing_config['password']})

    def generate_id(self):
        session_id = ''
        for _ in range(4):
            session_id += str(random.randint(0, 9))
        self.all_ids.append(session_id)
        return session_id


class ButtonCallback:
    def __init__(self, session_id):
        self.session_id = session_id

    def __call__(self):
        db.read(task='get', col='F', row=db.count_rows(value=self.session_id))
        app.mainloop('load')


def resume_clicked():
    '''db.read(task='get', col='F', row=db.count_rows(value=btn.get_id()))
    app.mainloop('load')'''


def launch_main_menu():
    main_menu.enable()
    authorization_menu.disable()


def sign_in():
    user_info = sign_in_menu.get_input_data()
    try:
        with open(config_file_path, 'r') as file:
            existing_config = json.load(file)
    except FileNotFoundError:
        existing_config = {}
    existing_config['username'] = user_info['Username']
    existing_config['password'] = user_info['Password']
    if 'first_time' not in existing_config:
        existing_config['first_time'] = True
    with open(config_file_path, 'w') as file:
        json.dump(existing_config, file)
    launch_main_menu()


def sign_up():
    valid_username = False
    valid_password = False
    try:
        with open(config_file_path, 'r') as file:
            existing_config = json.load(file)
        user_input = sign_up_menu.get_input_data()
        username = user_input['Username2']
        password = user_input['Password2']
        db.make_request(mode='read', range_to_fetch='A:A')
        if [username] in db.values['values']:
            valid_username = True
        db.make_request(mode='read', range_to_fetch='B:B')
        if [password] in db.values['values']:
            valid_password = True
        if valid_password and valid_username:
            launch_main_menu()
            existing_config['username'] = username
            existing_config['password'] = password
            with open(config_file_path, 'w') as file:
                json.dump(existing_config, file)
        else:
            raise ValueError
    except ValueError:
        print('Wrong username or password. Try again!')


def func():
    if db.count_rows == 1:
        app.mainloop()
    else:
        app.mainloop('new')


def switch_to_authorization():
    global first_time
    first_time = True


def drop_sessions_list():
    val = 'values'
    try:
        if not first_time:
            rows = db.count_rows(value=db.get_username(), count_all=True)
            db.read(col='C', row=rows[-1])
            session_id = db.values[val][0][0]
            db.read(col='D', row=rows[-1])
            status = db.values[val][0][0]
            db.read(col='E', row=rows[-1])
            date = db.values[val][0][0]
            resume_menu.add.button(f'ID:{session_id} | {status} | {date}', ButtonCallback(session_id))
    except (KeyError, TypeError, IndexError) as e:
        pass


def set_access():
    db.update_status(app.current_session_id, app.set_access_btn.status)


def join_session():
    try:
        user_input = join_menu.get_input_data()
        session_id = [str(user_input['SessionID'])]
        db.read(col='C:C', row='')
        all_ids = db.values['values']
        row = db.count_rows(value=''.join(session_id))
        db.read(col='D', row=row)
        access = ''.join(db.values['values'][0])
        if session_id in all_ids and access == 'public':
            db.read(task='get', col='F', row=row)
            app.mainloop('load')
        else:
            print('something went wrong')
    except ValueError as e:
        print(e)


text = TextInput()

handwriting = Handwriting()

erasing = Erasing()

load_file = LoadFile()

app = Application()

db = Database()


running = True
while running:
    print('in main loop', first_time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('EWAP')
    main_menu = pygame_menu.Menu('EWAP', screen_width, screen_height)
    authorization_menu = pygame_menu.Menu('Authorization', screen_width, screen_height)
    sign_in_menu = pygame_menu.Menu('Sign In', screen_width, screen_height)
    resume_menu = pygame_menu.Menu('Resume Session', screen_width, screen_height)
    join_menu = pygame_menu.Menu('Join session', screen_width, screen_height)
    sign_up_menu = pygame_menu.Menu('Sign Up', screen_width, screen_height)
    main_menu.add.button('New Session', func)
    main_menu.add.button('Resume Session', resume_menu)
    main_menu.add.button('Join Session', join_menu)
    main_menu.add.button('Switch Account', authorization_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    sign_in_menu.add.text_input('Username: ', textinput_id='Username')
    sign_in_menu.add.text_input('Password: ', textinput_id='Password')
    sign_in_menu.add.button('Confirm', sign_in)
    sign_up_menu.add.text_input('Username: ', textinput_id='Username2')
    sign_up_menu.add.text_input('Password: ', textinput_id='Password2')
    sign_up_menu.add.button('Confirm', sign_up)
    join_menu.add.text_input('Session ID: ', textinput_id='SessionID')
    join_menu.add.button('Confirm', join_session)
    authorization_menu.add.button('Sign In', sign_in_menu)
    authorization_menu.add.button('Sign Up', sign_up_menu)
    drop_sessions_list()
    if first_time:
        authorization_menu.mainloop(screen)
        first_time = False
    else:
        main_menu.mainloop(screen)
pygame.quit()

