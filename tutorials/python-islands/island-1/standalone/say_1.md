### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStop players set @s f1-say-complete 1


# Island-1-Say
```template
player.say("Hello world!")
```

## say()コマンドの使用 @showdialog

このアクティビティでは、Pythonの`||player:say()||`コマンドを深掘りします。`||player:say()||`コマンドは、チャットにメッセージを出力するために使用されます。

この通りにすると動きます。次のように書くと：

`||player:player.say("Hello world!")||`

出力は次のようになります：
![Say output](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/standalone/say1.jpg)

## 自分で試してみる
下のプログラムを実行ボタンを押して試してみてください。    
他に何を言いたいですか？" "の中のオレンジ色のテキスト部分を調整して、何が起こるか見てみましょう。
```python
player.say("Hello!")
```

## なぜ引用符が必要なのですか？ @showdialog
見ての通り、sayコマンド内のテキストの周りに引用符の" "（ダブルクオーテーション）を付けています。   

しかし、なぜこれらが必要なのでしょうか...?

これは、Pythonでは、テキスト（文字列とも呼ばれます）として扱われるコードは引用符で囲む必要があるためです。


## 他のデータ型には何がありますか？ @showdialog

文字列（テキスト）は、Python内のデータ型の1つに過ぎません。他にも興味深い**データ型**がいくつかあります。   
- 整数：整数、例えば、1、5、-2
- 浮動小数点数：小数、例えば、1.4、5.7、-3.8
- ブール値：TrueまたはFalse（大文字のTとFを含める必要があります）

`||player:say()||`コマンドは、引用符なしでこれらのそれぞれを出力することをサポートしています。

## 他のデータ型
`||player:player.say||`のかっこ内のすべてを削除し、引用符を含めて、かっこ内に別のデータ型を入れてみてください。

例えば、整数（5）、浮動小数点数（1.4）、またはブール値（True）を入れてみてください。

```diffpython
player.say()
----------------------
player.say(5)
```

## タスク完了
*esc*キーをクリックしてコードエディタを閉じ、変数に関するレッスンを見つけに行きましょう。
