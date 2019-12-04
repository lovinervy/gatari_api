<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="gatariapi____0"></a>gatariapi (В процессе редактирование)</h1>
<blockquote>
<p class="has-line-data" data-line-start="1" data-line-end="2">run &amp; first_plays_checker пока не работают</p>
</blockquote>
<p class="has-line-data" data-line-start="3" data-line-end="6">ДЛЯ ЗАПУСКА СКРИПТА ТРЕБУЕТСЯ УСТАНОВИТЬ PYTHON<br>
А ДЛЯ КОРРЕКТНОЙ РАБОТЫ УСТАНОВИТЬ МОДУЛИ.<br>
НУЖНЫЕ МОДУЛИ РАСПИСАНЫЙ В ФАЙЛЕ <code>requirements.txt</code></p>
<blockquote>
<h3 class="code-line" data-line-start=8 data-line-end=9 ><a id="___GATARIAPI_8"></a><strong>ДОКУМЕНТАЦИЯ ПО МОДУЛЮ GATARIAPI:</strong></h3>
</blockquote>
<p class="has-line-data" data-line-start="9" data-line-end="11">Все запросы происходят по html, в ответ возвращается html текст, которое сохраняется и обрабатывается как json файл.<br>
Подробнее для анализа json файлов и последующей манипуляции можно ознакомиться на сайте <code>https://osu.gatari.pw/docs/api</code> .</p>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th><strong><code>Game modes</code></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>0</strong> – standard</td>
</tr>
<tr>
<td><strong>1</strong> – taiko</td>
</tr>
<tr>
<td><strong>2</strong> – catch the beat</td>
</tr>
<tr>
<td><strong>3</strong> – mania</td>
</tr>
</tbody>
</table>
<blockquote>
<p class="has-line-data" data-line-start="20" data-line-end="23"><strong><code>user_info</code></strong> принимает информацию о пользователе.<br>
<strong>Входные данные: <code>u</code></strong><br>
<strong>«u»</strong> - должен присваиваться значение <strong>id</strong> пользователя, которая идет как <strong>int</strong>, при присвоении к <strong>«u»</strong> не <strong>id</strong>, а <em>username/nickname</em>, то функция будет возвращать пустой массив с кодом <code>200</code> <em>(Спасибо Сдем, что не сообщаешь об ошибке)</em></p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="24" data-line-end="27"><strong><code>users_info_pars</code></strong> принимает от одного до n-ое кол-во юзеров. (Не знаю зачем её юзать)<br>
<strong>Входные данные: u1, u2</strong><br>
Какое количество вернет зависит от того, какой диапазон был вбит в <strong>«u1»</strong> &amp; <strong>«u2»</strong> возвращает тоже самое что и <code>user_info</code>, но в виде массива с n-е кол-во юзеров, <strong>«u1»</strong> &amp; <strong>«u2»</strong> должно принимать значение <strong>«int»</strong> от <em>1000</em> и более</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="28" data-line-end="33"><strong><code>user_stats</code></strong> принимает значение о статистике юзера по выбранным модам<br>
<strong>Входные данные: <code>u</code></strong>, <strong><code>mode</code></strong><br>
Возвращает информацию о статистике пользователя т.е. ср.%, кол-во сыгранных мап и т.д.<br>
Нужно отправлять 2 значения это <strong>«u»</strong> <em>(id пользователя)</em> и <strong>«mode»</strong> <em>(режим игры)</em>, где <strong>«mode»</strong><br>
принимает значение от <code>0</code> до <code>3</code><em>(Что эти числа значат можно почитать в начале документации)</em>.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="34" data-line-end="42"><strong><code>recent_scores</code></strong>, принимает значение об последних играх от пользователя.<br>
<strong>Входные данные: <code>u</code></strong>, <strong><code>l</code></strong>, <strong><code>p</code></strong>, <strong><code>mode</code></strong>, <strong><code>f</code></strong>, <strong><code>ppf</code></strong><br>
<strong>«u»</strong> id пользователя, формат <code>int</code><br>
<strong>«l»</strong> length кол-во последних скоров, принимает значение от <code>0</code> <em>(пустой массив)</em> до <code>100</code><br>
<strong>«p»</strong> page номер страницы, принимает от <code>1</code> до <code>n</code> <em>(до какой именно не проверял)</em><br>
<strong>«mode»</strong> mode игровой режим принимает значение <code>0</code>–<code>3</code> <em>(Что эти числа значат можно почитать в начале документации)</em><br>
<strong>«f»</strong> failed включать в список карты, которые были пройдены не до конца, принимает значение <code>0</code> или <code>1</code>, где <code>0</code> – показывать только до конца пройденные карты, а <code>1</code> соответственно общее.<br>
<strong>«ppf»</strong> ppFilter – принимает значение от <code>0</code> до <code>n</code>, где фильтр возвращает скоры, которые выше указанного значения.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="43" data-line-end="50"><strong><code>best_score</code></strong>, принимает значение о лучших скорах у пользователя<br>
<strong>Входные данные <code>u</code></strong>, <strong><code>l</code></strong>, <strong><code>p</code></strong>, <strong><code>mode</code></strong>, <strong><code>mods</code></strong><br>
<strong>«u»</strong> id пользователя, в формате <code>int</code>.<br>
<strong>«l»</strong> количество скоров, которые хотите видеть, формат <code>int</code>.<br>
<strong>«p»</strong> номер страницы, формат <code>int</code>.<br>
<strong>«mode»</strong> игровой режим, принимает значение от <code>0</code>–<code>3</code> <em>(Что эти числа значат можно почитать в начале документации)</em><br>
<strong>«mods»</strong> с какими модами нужны скоры. Все значение есть здесь: <a href="https://github.com/ppy/osu-api/wiki#mods">https://github.com/ppy/osu-api/wiki#mods</a></p>
</blockquote>

</body></html>
