### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStop players set @s f1-var-complete 1


# 変数の紹介


```template
// Edit the text (String) below to add your own message
my_variable = "Test" 

// This line below outputs the contents of your variable to game chat
player.say(my_variable)
```


## 変数とは何ですか？
プログラミングでは、`変数`は情報を一時的に保存する場所です。データを保存し、後でアクセスできるようにします。各`変数`には、あなたが付ける名前があります。   

変数を作成するには、下のコードを見てください：

`||variables:my_variable = "Hello world"||`


プログラムを実行して、何が起こるか見てみましょう。おそらく" "内のテキスト部分を調整してみてください。


## 変数の上書き

すでに作成した`変数`の内容も、同じプロセスで変更できます。例えば：

`||variables:my_variable = "Hello"||`

下の行は、"Hello"を"World"に置き換えます

`||variables:my_variable = "World"||`

`||my_variable||`を作成する場所と`||player:player.say(STRING)||`コマンドを使用する場所の間に新しい行を追加して、`||my_variable||`を変更してみてください。

```python

my_variable = "Hello"

// This line below will overwrite "Hello" with "World" instead

my_variable = "World"

```

## 変数のまとめ
変数は非常に強力で、コーディングのあらゆる場所で使用されています！   

Pythonでは、あらゆるデータ（文字列、整数、浮動小数点数、ブール値を含む）を保存でき、プログラム内の他の場所から簡単にアクセスできます。   

次の形式を常に使用することを覚えておいてください： 
`||variables:variable_name = data_being_stored||`

例えば：

`||variables:name = "bob"||`

`||variables:age = 5||`


**タスク完了！**
