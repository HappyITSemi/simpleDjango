### Description for Data Base
### フィールド・リファレンス一覧
### 参照
##### https://docs.djangoproject.com/ja/3.0/ref/models/fields/

select * from public.xxx_table;

insert into public.xxx_table(id, name) values(1, 'namae-1')

update

＞Djangoのモデル定義ファイル(models.py等）内で row = models.XXXField(～） のように使用します

|フィールド|説明|XXXXX|
|---|---|---|
|AutoField|xxx|xxx|
|Automatic primary key fields|xxx|xxx|
|BooleanField|xxx|xxx|
|CharField|文字列のフィールド|xxx|
|DateField|datetime.date インスタンスによって表される日付|xxx|
|DateTimeField|datetime.datetimeインスタンスによって表される日付と時刻|xxx|
|DurationField|時刻の期間を保持するフィールドで、Pythonのtimedeltaによってモデル化|xxx|



|フィールドの型|	説明|
|----|----|
|AutoField|	利用可能な ID に応じて、自動的にインクリメントする IntegerField です。通常は直接使う必要はありません; 指定しない場合は、主キーのフィールドが自動的にモデルに追加されます。Automatic primary key fields も参照してください。|
|BigAutoField|	64 ビットの数値です。1 から 9223372036854775807 までの数を扱える以外は、AutoField と同じです。|
|BigIntegerField|	64 ビットの数値です。-9223372036854775808 から 9223372036854775807 を扱える以外は IntegerField と同じです。このフィールドのデフォルトのフォームウィジェットは TextInput です。|
|BinaryField|	生のバイナリデータを保持するためのフィールドです。bytes` のアサインメントのみをサポートします。このフィールドには機能制限があります。例えば、BinaryField の値でクエリセットをフィルタすることはできません。また、BinaryField を ModelForm に含めることもできません。|
|BooleanField|	true/false のフィールドです。|
|CharField|	小 - 大サイズの文字列のフィールドです。|
|CommaSeparatedIntegerField|	バージョン 1.9 で撤廃:カンマによって区切られた数値のフィールドです。CharField と同じく、max_length 引数が必須で、そこで説明したデータベースの可搬性についての注意を考慮する必要があります。|
|DateField|	Python で datetime.date インスタンスによって表される日付です。多少の追加的な省略可能な引数を持ちます:|
|DateTimeField|	Python で datetime.datetime インスタンスによって表される日付と時刻です。DateField と同じくいくつかの追加的な引数を持ちます:|
|DecimalField|	Python で Decimal インスタンスによって表される固定精度の小数です。2 つの 必須の 引数があります:|
|DurationField|	時刻の期間を保持するフィールドで、 Python の timedelta によってモデル化されます。PostgreSQL で使われるときに用いられるデータ型は interval で、Oracle でのデータ型は INTERVAL DAY(9) TO SECOND(6)です。 それ以外では、マイクロ秒のbigint が使われます。|
|EmailField|	値が有効な E メールアドレスかチェックする CharField です。EmailValidator を使ってインプットを検証します。|
|FileField|	ファイルアップロードのフィールドです。|
|FileField と FieldFile|	モデル上の FileField にアクセスするとき、元となるファイルにアクセスするためのプロキシとして、FieldFile のインスタンスが与えられます。|
|FilePathField|	ファイルシステム上の特定のディレクトリ内のファイル名に選択肢が制限されている CharField です。3 つの特別な引数があり、最初の 1 つは 必須 です:|
|FloatField|	float インスタンスによって表される Python の浮動小数点数です。|
|ImageField|	FileField から全ての属性とメソッドを継承して、さらにアップロードされたオブジェクトが有効な画像であることを検証します。|
|IntegerField|	数値です。-2147483648 から 2147483647 までの値は、Django でサポートされているデータベース内では安全です。このフィールドのデフォルトのフォームウィジェットは、localize が False のときには NumberInput で、そうでなければ TextInput となります。|
|GenericIPAddressField|	IPv4 か IPv6 のアドレスで、文字列フォーマットです (例: 192.0.2.30 ないし 2a02:42fe::4)。このフィールドのデフォルトのフォームウィジェットは TextInput です。|
|NullBooleanField|	BooleanField とほぼ同じですが、オプションの 1 つとして NULL を許容します。BooleanField を null=True で使う代わりにこれを使ってください。このフィールドのデフォルトのフォームウィジェットは NullBooleanSelect です。|
|PositiveIntegerField|	IntegerField とほぼ同じですが、正の値かゼロ (0) でなければなりません。Django によってサポートされる全てのデータベースで、0 から 2147483647 までの値は安全です。後方互換性の理由から、値 0 が有効となっています。|
|PositiveSmallIntegerField|	PositiveIntegerField とほぼ同じですが、特定の (データベースに依存した) ポイントより下の値のみを許容します。Django でサポートされている全てのデータベースで、0 から 32767 までの値は安全です。|
|SlugField|	Slug は新聞の用語です。 スラグは、文字、数字、アンダースコア、またはハイフンのみを含む短いラベルです。 一般的に URL 内で使用されます。|
|SmallIntegerField|	IntegerField とほぼ同じですが、特定の (データベースに依存した) ポイントより下の値のみを許容します。Django でサポートされている全てのデータベースで、-32768 から 32767 までの値は安全です。|
|TextField|	多量のテキストのフィールドです。このフィールドのデフォルトのフォームウィジェットは Textarea です。|
|TimeField|	Python で datetime.time インスタンスによって表される時刻です。DateField と同じ自動入力されるオプションを受け入れます。|
|URLField|	URL のための CharField です。|
|UUIDField|	UUID (Universally Unique Identifier) を保持するためのフィールドです。Python’s UUID クラスを使います。 PostgreSQL 上で使われるとき、uuid データ型の中に保持します。それ以外は char(32) の中に保持します。|

