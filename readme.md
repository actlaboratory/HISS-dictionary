# HISS 読み辞書データ

[HISS](https://actlab.org/software/HISS) の読み辞書のデータです。実際にHISSに入っているものはコンパイル済みですが、この元データから生成したものです。

# ファイルの説明

- main.csv: メインの読み辞書データです。
- wordset_additional.txt: ここに追加した単語は、HISSがすでに知っている単語と見なされます。ここに登録されている単語は、推測読みの対象になりません。
- wordset_exclude.txt: wordset_additional.txt の逆です。ここに登録されている単語は、強制的に推測読みの対象になります。

# 変更方法

forkして、pull requestでお願いします。masterブランチには直接pushできないようにガードしてあります。

## main.csv

## 単語の追加方法

単語を追加していただける場合、 main.csv に行を追加してください。基本書式は、

`単語,読み,4`

です。

単語には、元々の単語を指定します。アルファベットを使うときは、半角の小文字を使ってください。

読みは、全角カタカナで指定します。アクセントを付けたいところには、全角の’ を付けます。文節を区切る場合、全角の＿を使用します。1つの単語のなかで2つ以上のアクセント指定はできません。

最後の 4 ですが、これは FineSpeech の内部で使用するコードなので、とりあえず一番使用頻度の多い 4 にしておいてください。中の人が必要に応じて直します。

## 単語の追加方針

基本的に、全て @yncat がレビューします。色々と基準があるのですが、今すぐ全部言語化できないので、とりあえず全部見ます。95%ぐらいは許可すると思います。

PRを出したときにCIがこける場合は、CSVを壊しているか、すでに登録されている単語を重複登録しようとしている可能性があります。CIのログを開いて詳細を確認し、修正してください。

以下の条件を満たしている場合、必ず拒否します。この条件は増える可能性があります。

- 文字から読みを想像できず、意味が一つに固定できない場合 (例: PS5 -> プレイステーションファイブ)
- 当て字である場合 (例: AAA -> トリプルエー)
- 2文字以下である場合(例: MR -> ミスター)

## HISSで使用する

これは、HISSの更新を待っていただく必要があります。この辞書データから、HISSで実際に使っている辞書データにコンパイルする必要があるのですが、そのコンパイラはFineSpeechの一部になるため、公開することができません。

# wordset_additional.txt および wordset_exclude.txt

## 単語の追加方法

1行に1単語書くだけです。

## 単語の追加方針

これは基本的に、 HISS が意図しない推測読みをしたり、推測読みしてほしいのにしてくれないときに適宜調整すれば十分です。

## HISSで使用する

アドオンの中に対応するファイルが入っているので、中身を置き換えれば動作します。
