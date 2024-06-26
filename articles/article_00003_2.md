---
title: "最小二乗法と仲良くなりたい②"
emoji: "🐷"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [統計,線型回帰,最小二乗法]
published: true
published_at: 2024-05-19 19:00
---

## 3行まとめ

1. 最小二乗法推定量の不偏性と一致性を確認するために最小二乗推定量の期待値と分散を求めたい
2. 誤差項に3つの仮定を敷くことでうまく導出と証明ができる。
3. この仮定によって最小二乗推定量は推定量として有効だと言えそう

## 今回は

https://zenn.dev/a_duty_rookie/articles/article_00003_1

前回は最小二乗法は何をしているのかというところから、回帰係数を推定するための最小二乗推定量の導出まで実施しました。
"推定量"と言われると、普遍性や一致性が気になりますね、ということで、今回は最小二乗推定量$\hat{\boldsymbol{\beta}}$について詳しく見ていきたいと思います。
簡単のため、前回同様に身長と牛乳摂取量というダミーデータを使って単回帰$Y_i = \beta_1 + \beta_2 X_i + \epsilon_i$を例に扱っていきます。

## 参考書籍

引き続き[統計学入門 a.k.a 赤本](https://amzn.to/4dmDECE) の範疇の内容でござい。

:::message
**免責事項**
間違いのないように理解したいという思いで学習をしていますが、なにぶん独学であり、専門ではありませんので、あくまでも私はこう解釈した、という内容であることご了承ください。
本文において断定調で記載している部分もありますが、いちいち「〜と私は理解しています」と記載すると冗長になってしまうので、体裁上「〜です」と記載しています。
決定的な誤りや、危険な解釈をしていると思われた場合は忌憚なくご指摘いただけますと幸いです。
:::

## 方針

[以前の投稿](https://zenn.dev/a_duty_rookie/articles/article_00002_2)にて、不偏性の確認には推定量の期待値が、一致性の確認にはそれに加えて推定量の分散[^1]が分かれば良さそうです。
そこで、前回以下のように導出された$\hat{\beta_1}$と$\hat{\beta_2}$の期待値、分散を考えていきます。
ちなみに、推定量$\hat{\beta_i}$は、すでに観測された$X$、$Y$の値を元に計算された値で、これは

$$
\begin{align*}
  \left \{
  \begin{align}
    \hat{\beta_2} &= \frac{\bar{XY} - \bar{X}\bar{Y}}{\bar{X^2} - \bar{X}^2} = \frac{\sum_{i=1}^{n} (X_i-\bar{X})(Y_i-\bar{Y})}{\sum_{i=1}^{n} (X_i-\bar{X})^2} = \frac{Cov(XY)}{V(X)} \\
    \hat{\beta_1} &= \bar{Y} - \hat{\beta_2} \bar{X}
  \end{align}
  \right .
\end{align*}
$$

$\hat{\beta_1}$は$\hat{\beta_2}$の線型式で表されるので、$\hat{\beta_2}$の期待値と分散が分かればなんとかなりそうですね。
ところで期待値や分散は、確率によって結果や揺らぐ**確率変数**について、期待される平均の値や、実際に得られる値が期待値の周辺でどれくらいばらつくか、という指標でした。
それでは今回の場合、確率変数は何になるでしょうか…？
今回の仮説は、

**$X_i$が得られた時、その$X$に$\beta_2$をかけて$\beta_1$を足したら大体$Y_i$になるだろう。ただしこれだけでは表現できない要素があるはずなので、それはまるっと誤差$\epsilon_i$としてまとめてしまおう。**

というものでした(ここから$Y_i = \beta_1 + \beta_2 X_i + \epsilon_i$と立式しましたね)。

この仮説の中においては、$X$はすでに得られている数なので、確率変数ではなく定数です[^2]。
$\epsilon_i$はどうでしょう。これは実際に得られた値ではないので、**確率変数**ですね。
確率によって誤差が大きかったり小さかったりするだろう、ということです。
そうなると、定数と確率変数の足し合わせによって表される$Y_i$**も確率変数**になります。
そして、$Y_i$によって表される$\hat{\beta_1}$や$\hat{\beta_2}$**も確率変数**ですね。
だからこそ、$\hat{\beta_1}$**と**$\hat{\beta_2}$**の期待値や分散が議論になっている**わけです。

と、いうことは、$\hat{\beta_1}$や$\hat{\beta_2}$の期待値、分散を考えるにあたっては、$\epsilon_i$の期待値や分散を考える必要がありそうです。
基本的に$\epsilon_i$は制御できる値ではないので、**いくつか仮定を敷いて**計算を進めていきます。

[^1]:期待値と分散が分かればシェビチェフの不等式を作って$n \to \infty$と極限を見ることで証明できそうだ、という考え方です。

[^2]:$X$がどのように得られるか、という点では$X$は確率変数たり得ますが、今は$X$を得て、それを元に$Y$を当てにいくことを考えていて、$X$は確定値なので定数として扱う、という意味です。

## $\hat{\beta_2}$の期待値を考える

(1)式を元に、$\hat{\beta_2}$の期待値$E(\hat{\beta_2})$を計算してみましょう。
そもそもの式である、$Y_i = \beta_1 + \beta_2 X_i + \epsilon_i$と、その平均を計算した$\bar{Y} = \beta_1 + \beta_2 \bar{X} + \bar{\epsilon}$を(1)式に代入することで以下の式を得ることができます。

$$
\begin{align}
  \hat{\beta_2} &= \frac{\sum_{i=1}^{n} (X_i-\bar{X})(Y_i-\bar{Y})}{\sum_{i=1}^{n} (X_i-\bar{X})^2} \notag \\
  &=\frac{\sum_{i=1}^{n} (X_i-\bar{X})((X_i-\bar{X})\beta_2+(\epsilon_i - \bar{\epsilon}))}{\sum_{i=1}^{n} (X_i-\bar{X})^2} \notag \\
  &=\beta_2 +
    \frac{\sum_{i=1}^{n} (X_i-\bar{X})\epsilon_i}{\sum_{i=1}^{n} (X_i-\bar{X})^2} -
    \frac{\bar{\epsilon}\sum_{i=1}^{n} (X_i-\bar{X})}{\sum_{i=1}^{n} (X_i-\bar{X})^2} \\
\end{align}
$$

ここで、しれっと登場した$\bar{\epsilon}$に対処するために、誤差$\epsilon_i$について、以下の仮定を敷きます。

**仮定①：誤差$\epsilon_i$の期待値は0であるものとする**

これは各$Y_i$について、個々に着目すると真の回帰式の値から正負大小ばらついた誤差が生じうるものの、全体ではキャンセルされて誤差の平均は0であるはずだ、という仮定です。

$$E(\epsilon_i) = \bar{\epsilon} = 0$$

この仮定のもとで、$X_i$は定数であることに注意しつつ(3)から期待値を計算していきます。

$$
\begin{align}
  \hat{\beta_2} &= \beta_2 +
    \frac{\sum_{i=1}^{n} (X_i-\bar{X})\epsilon_i}{\sum_{i=1}^{n} (X_i-\bar{X})^2} \\
  E(\hat{\beta_2})
    &= \beta_2
    + \frac{\sum_{i=1}^{n} (X_i-\bar{X})E(\epsilon_i)}{\sum_{i=1}^{n} (X_i-\bar{X})^2} \notag\\
    &= \beta_2
\end{align}
$$

以上から、仮定①の元では$\beta_2$の不偏性が示されました。

## $\hat{\beta_2}$の分散を考える

分散も同様に考えていきます…が、期待値とほとんど同じように考えられそうです。
ただネックは、期待値に加法性が成り立つことを使って式変形している(4)式から(5)式のところ。
そこで、誤差$\epsilon_i$に対してもう二つ仮定を敷きます。

**仮定②：誤差の分散は常に一定である** $\dotsi V(\epsilon_i) = \sigma^2$
**仮定③：誤差間に相関はないものとする** $\dotsi Cov(\epsilon_i, \epsilon_j)=0$

仮定③によって分散の加法性が保証され、仮定②によって分散の足し算がやりやすくなりますね。
意味合い的には、生じうる誤差は全て共通のばらつきを持っていて、他のサンプルによってその誤差は影響されないという仮定、という理解ができるかと思います。
これ、結構強力な仮定です[^3]。

兎にも角にもこの仮定を敷くことで(4)式から$V(\hat{\beta_2})$を導くことができます。

$$
\begin{align}
  V(\hat{\beta_2})
    &= \frac{V(\sum_{i=1}^{n} (X_i-\bar{X})\epsilon_i)}{(\sum_{i=1}^{n} (X_i-\bar{X})^2)^2} \notag\\
    &= \frac{\sum_{i=1}^{n} (X_i-\bar{X})^2V(\epsilon_i)}{(\sum_{i=1}^{n} (X_i-\bar{X})^2)^2} \notag\\
    &= \frac{\sigma^2}{\sum_{i=1}^{n} (X_i-\bar{X})^2}\\
\end{align}
$$

[^3]:たとえば$Y$がサンプルサイズが異なる何かの平均値だったりすると、その分散は元の値の分散を$\sigma^2$として$\frac{\sigma^2}{n}$になるので、分散一定を満たしません。また、たとえば日次売上などの時系列データだと前日の売上$Y_{i-1}$が翌日の売上$Y_{i}$に影響することが容易に考えられるので、相関があることになってしまいます。$X_i$が与えられたときの$Y_i$のばらつきは$\epsilon_i$によるので、$Y_i$が仮定②、③を満たさないということは$\epsilon_i$もまたそれらの仮定を満たさないということになります。

## $\hat{\beta_1}$の期待値と分散を考える

$\beta_1$に関しては、(2)式について期待値と分散をとっていくことで導出していくことが可能です。
その際に、これまでの誤差に関する仮定から、$\bar{Y}=\beta_1 + \beta_2\bar{X}$であることを使います.

$$
\begin{align*}
  \hat{\beta_1} &= \bar{Y} - \hat{\beta_2} \bar{X} \\
    &= \beta_1 + (\beta_2-\hat{\beta_2})\bar{X}
    \quad(\because \bar{Y}=\beta_1 + \beta_2\bar{X})\\
  \\
  E(\hat{\beta_1}) &= \beta_1 + (\beta_2-E(\hat{\beta_2}))\bar{X} \\
  &= \beta_1 \quad(\because E(\hat{\beta_2}) = \beta_2)\\
  \\
V(\hat{\beta_1}) &= V(\hat{\beta_2}\bar{X}) = \bar{X}^2V(\beta_1) \\
  &= \frac{\bar{X}^2}{\sum_{i=1}^{n} (X_i-\bar{X})^2}\sigma^2 \quad(\because V(\hat{\beta_2}) = \frac{\sigma^2}{\sum_{i=1}^{n} (X_i-\bar{X})^2})\\
\end{align*}
$$

## $\hat{\beta_1}$、$\hat{\beta_2}$の点推定量としての性質を考える

さて、いよいよ$\hat{\beta_1}$と$\hat{\beta_2}$の不偏性、一致性について考えていきましょう。
と言いつつも、これまでの導出で、それぞれ期待値が$\beta_1$と$\beta_2$に一致することが導出されましたので、**不偏性についてはいずれも満たしていることは確認済み**ですね。
一致性についてはどうでしょう。
一致性は、サンプルサイズ$n$を無限大にしたとき、推定量の期待値が母数に限りなく一致することであり、証明の戦略としては、$n$を無限大にしたときのシェビチェフの不等式を観察する、という方法がありましたね。

$$
\displaystyle P(|X-\mu|\geqq k\sigma) \leqq \frac{1}{k^2} \\
\footnotesize Xは母集団から独立に得られた確率変数 \\
\muはXの期待値(= E(X)) \\
\sigma^2はXの分散(= V(X)) \\
kは任意の正の整数
$$

簡単にしてしまえば、$n \to \infty$のとき$\sigma \to 0$であれば、$|X-\mu|>0$となる確率がほとんど0になる、ということでした。
https://zenn.dev/a_duty_rookie/articles/article_00002_2

ということで、それぞれの分散の極限を見てみましょう。

$$
\begin{align*}
  V(\hat{\beta_1})
    &= \frac{\bar{X}^2}{\sum_{i=1}^{n} (X_i-\bar{X})^2}\sigma^2 \\
  V(\hat{\beta_2})
    &= \frac{1}{\sum_{i=1}^{n} (X_i-\bar{X})^2}\sigma^2
\end{align*}
$$

いずれも分母は$\sum_{i=1}^{n} (X_i-\bar{X})^2$であり、これは$n \to \infty$のとき正の整数の無限和で無限大に発散します。
よって、$V(\beta_1)$、$V(\beta_2)$ともに$n \to \infty$のときは$0$に収束、平方根であるそれぞれの標準偏差も同様に収束することから、$\beta_1$と$\beta_1$の一致性を示すことができました。

## 終わりに

以上から、誤差に以下の3つの仮定を敷いて良いのであれば、標本から計算された$\hat{beta_1}$と$\hat{beta_2}$はそれぞれの真値に対して不偏性と一致性を持つので、推定量として使えそう、ということを示すことができました。

**仮定①：誤差$\epsilon_i$の期待値は0であるものとする**
**仮定②：誤差の分散は常に一定である**
**仮定③：誤差間に相関はないものとする**

この仮定を元にするともう一つ、$\bar{\beta_1}$、$\bar{\beta_2}$は$Y(=\beta_1+\beta_2X+\epsilon)$の線型変換で表すことができる$\beta_1$、$\beta_2$の推定量の中で最も分散が小さい推定量であることが知られています。
期待値が真値に一致することが保障されていたとて無限回も実験をするわけにはいかないので、各回の推定値は真値の近傍であって欲しい、ですよね？
と、いうことは、分散が最小な推定量ってベストな推定量ですよね！？
・・・ということで、**B**est(最良) **L**inier(線型) **U**nbiased(不偏) **E**stimator(推定量)の頭文字をとって**BLUE**と言ったりします。
かっこいいですね。

さてさて、こうやって計算すれば$\hat{\beta}$というベストな推定量が得られることがわかりました。ただ、(当たり前ではありますが)ベストな推定量とは言ったって、どうしても真値のズレは避けられなさそうです。
そうなると今度はたとえば「$\beta_2$は**絶対0より大きいってことでいいよね**、実は0でしたなんてこと、ないよね？」ということが気になってくるわけですね。
今回の例で言えば「**牛乳消費量に対する係数は4くらいだったけど、効果あるってことでいいんだよね**？」という観点です。

残念ながら真値は神にしかわからないのでなんともわかりません、というのが厳密な答えだとしても、まぁ確率的に考えたら0よりは大きいと捉えてもまぁ妥当なんちゃう？ということが、検定の考え方を適応すると議論できそうです。

次回はこの$\beta$に対する検定について、もう一つ強力な仮定を敷いて検討してみたいと思います。

以上、ご確認のほど、よろしくお願いいたします。
