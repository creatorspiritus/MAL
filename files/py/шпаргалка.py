import streamlit as st
import time

st.header('Элементы текста')
st.text('Обычный текст параграфа.')
st.text('Каждый элемент - это новый абзац.')
st.markdown("""\
## Применение языка Markdown
            
Для вывода форматированного текста можно использовать язык Markdown. 
Это позвляет выводить на экран форматированные блоки текста.
            
Каждый абзац разделяется пустой строкой.
            
> ВАЖНО! Заголовок второго уровня Markdown соответствует заголовку 
> раздела `st.header('Заголовок раздела')`
            """) # see #*
st.caption("Элемент подпись (st.caption('...'))")
st.latex(r''' e^{i\pi} + 1 = 0 ''')
имя = "Миша"
st.write('Функция `write` может выводить на экран различные объекты:') # df, err, func, keras!
st.write('Имя: ', имя) # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('Название соответствует первому уровню заголовка Markdown')
st.header('Заголовок раздела')
st.subheader('Заголовок подраздела')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True



st.header('Отображение данных')
# st.dataframe(my_dataframe)
# st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Температура", value="273 °C", delta="1.2 °C")
st.metric(label="Крейсерская скорость", value="280 км/ч", help="Vкр")



st.header('Отображение медиафайлов')
st.image('c:\\Users\\kotlyarov_m\\Documents\\MK\\files\\jpg\\Я куда-то нажал и всё сломалось.jpg')
# st.audio(data)
# st.video(data)



st.header('Отображение столбцов данных')
col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# Три столбца с различной шириной
col1, col2, col3 = st.columns([3,1,1],)
# col1 is wider

# Using 'with' notation:
with col1:
    st.write('Столбец № 1')
    st.write('Данные этого столбца размещаются ',
             'в области, в три раза превышающую ширину двух других ',
             'столбцов')
with col2:
    st.write('Столбец № 2')
with col3:
    st.write('Столбец № 3')


st.header('Отображение вкладок')
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Вкладка 1", "Вкладка 2"],)
tab1.write("Содержимое первой вкладки")
# # Использовать "with" для :
with tab1:
  st.radio('Выберите значение:', [1, 2])
tab2.write("Содержимое второй вкладки")
# 

with tab2:
  st.radio('Выберите имя:', ["Миша", "Света", "Женя", "Федя"])


st.header('Управление потоками')
# Stop execution immediately:
# st.stop()
# Rerun script immediately:
# st.experimental_rerun()

# Group multiple widgets:
# >>> with st.form(key='my_form'):
# >>>   username = st.text_input('Username')
# >>>   password = st.text_input('Password')
# >>>   st.form_submit_button('Login')



st.header('Персонализация приложений для пользователей')
# Показывать различный контент в зависимости от адреса электронной почты пользователя.
# >>> if st.user.email == 'jane@email.com':
# >>>    display_jane_content()
# >>> elif st.user.email == 'adam@foocorp.io':
# >>>    display_adam_content()
# >>> else:
# >>>    st.write("Пожалуйста, получите доступ к данным!")



st.header('Отображение интерактивных виджетов')
st.button('Нажать!')
# st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Выберите вариант:', ['Ёжики','Бобры'])
выбор = st.selectbox('Select', [1,2,3])
множественный_выбор = st.multiselect('Множественный выбор', ["Миша","Света","Женя", "Фёдор"])
print(множественный_выбор)
st.slider('Передвинуть ползунок на требуемое значение', min_value=0, max_value=10)
st.select_slider('Стадии жизненного цикла', options=[
   "Разработка документации",
   'Проверка руководителем', 
   "Согласование с подразделениями",
   "Утверждение у руководства",
   "Отправка заказчику",
   "Исправление замечаний",
   "Утверждение заказчиком",
   "Ввод в эксплуатацию"], value="Исправление замечаний")
st.text_input('Поле для ввода текста', placeholder="Введите текст")
st.number_input('Ввод значения', help="Требуется указать значение стоимости")
st.text_area('Поле ввода текстового блока', placeholder="Введите текст")
st.date_input('Укажите или выберите дату')
st.time_input('Укажите или выберите время вылета')
st.file_uploader('Загрузите файл данных',)
# st.download_button('On the dl', data)
st.camera_input("Внимание! Мотор!")
st.color_picker('Выберите цвет')


# Use widgets' returned values in variables
# >>> for i in range(int(st.number_input('Num:'))): foo()
# >>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
# >>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
# >>> st.write(slider_val)



# Disable widgets to remove interactivity:
# >>> st.slider('Pick a number', 0, 100, disabled=True)



st.header('Создавайте приложения на основе чата')
# Insert a chat message container.
# >>> with st.chat_message("user"):
# >>>    st.write("Hello 👋")
# >>>    st.line_chart(np.random.randn(30, 3))
# 
# Display a chat input widget.
# >>> st.chat_input("Say something")



st.header('Изменяемые данные')
# Add rows to a dataframe after
# showing it.
# >>> element = st.dataframe(df1)
# >>> element.add_rows(df2)

# Add rows to a chart after
# showing it.
# >>> element = st.line_chart(df1)
# >>> element.add_rows(df2)



st.header('Отображение кода')
# st.echo()
# >>> with st.echo():
# >>>     st.write('Code will be executed and printed')



st.header('Подсказки, помощь и настройки')
# Замена элемента
element = st.empty()
element.caption('Подпись')
time.sleep(2)
element.button("Кнопка")
# element.line_chart(...)
# element.text_input(...)  # Replaces previous.

# Insert out of order.
# >>> elements = st.container()
# >>> elements.line_chart(...)
# >>> st.write("Hello")
# >>> elements.text_input(...)  # Appears above "Hello".
# 
# st.help(pandas.DataFrame)
# st.get_option(key)
# st.set_option(key, value)
# st.set_page_config(layout='wide')
# st.experimental_show(objects)
# st.experimental_get_query_params()
# st.experimental_set_query_params(**params)



st.header('Подключение к пользовательским данным')
# st.experimental_connection('pets_db', type='sql')
# conn = st.experimental_connection('sql')
# conn = st.experimental_connection('snowpark')
# 
# >>> class MyConnection(ExperimentalBaseConnection[myconn.MyConnection]):
# >>>    def _connect(self, **kwargs) -> MyConnection:
# >>>        return myconn.connect(**self._secrets, **kwargs)
# >>>    def query(self, query):
# >>>       return self._instance.query(query)



st.header('Оптимизация')
st.subheader('Кэширование объектов данных')
# E.g. Dataframe computation, storing downloaded data, etc.
# >>> @st.cache_data
# ... def foo(bar):
# ...   # Do something expensive and return data
# ...   return data
# # Executes foo
# >>> d1 = foo(ref1)
# # Does not execute foo
# # Returns cached item by value, d1 == d2
# >>> d2 = foo(ref1)
# # Different arg, so function foo executes
# >>> d3 = foo(ref2)
# # Clear all cached entries for this function
# >>> foo.clear()
# # Clear values from *all* in-memory or on-disk cached functions
# >>> st.cache_data.clear()



st.subheader('Кэширование глобальных ресурсов')
# E.g. TensorFlow session, database connection, etc.
# >>> @st.cache_resource
# ... def foo(bar):
# ...   # Create and return a non-data object
# ...   return session
# # Executes foo
# >>> s1 = foo(ref1)
# # Does not execute foo
# # Returns cached item by reference, s1 == s2
# >>> s2 = foo(ref1)
# # Different arg, so function foo executes
# >>> s3 = foo(ref2)
# # Clear all cached entries for this function
# >>> foo.clear()
# # Clear all global resources from cache
# >>> st.cache_resource.clear()



st.subheader('Устаревшее кэширование')
# >>> @st.cache
# ... def foo(bar):
# ...   # Do something expensive in here...
# ...   return data
# >>> # Executes foo
# >>> d1 = foo(ref1)
# >>> # Does not execute foo
# >>> # Returns cached item by reference, d1 == d2
# >>> d2 = foo(ref1)
# >>> # Different arg, so function foo executes
# >>> d3 = foo(ref2)



st.header('Отображение прогресса и статуса')
# Показ спиннера во время выполнения процедуры
with st.spinner(text='В процессе выполнения...'):
   time.sleep(3)
   st.success('Процедура завершена', icon="✅")

# Показ линии завершения операции с отображением названий промежуточных этапов
bar = st.progress(0)
time.sleep(1)
bar.progress(1, text="Предварительная...")
time.sleep(1)
bar.progress(20, text="Промежуточная...")
time.sleep(1)
bar.progress(50, text="Продувка...")
time.sleep(1)
bar.progress(100, text="Выполнено")

# Функция запускает на экране обозревателя шарики
# st.balloons()


# Функция запускает на экране обозревателя снежинки
# st.snow()


# Функция отображает текстовое поле в нижнем правом углу обозревателя
# st.toast('Функция `st.toast` отработала штатно!')

st.header('Поля для вывода сообщений на экран')
st.error('Сообщение об ошибке', icon="🚨")
st.warning('Предупреждение об отклоненнии', icon="⚠️")
st.info('Важное сообщение', icon="ℹ️")
st.success('Сообщение о выполнении процедуры', icon="✅")
e = RuntimeError('Ошибка выполнения!')
st.exception(e)
